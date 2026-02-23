import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { env, pipeline } from '@xenova/transformers';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

// Cargar variables d'entorn
dotenv.config();

// Configuració de Transformers.js per ús local exclusiu
env.localModelPath = './models';
env.allowRemoteModels = true; // Permetre descarregar el model la primera vegada

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Directoris
const DATA_DIR = path.join(__dirname, '../data');
const OUTPUT_FILE = path.join(DATA_DIR, 'corpus-embeddings.json');

// Configuració del model i chunking
const MODEL_NAME = 'Xenova/paraphrase-multilingual-MiniLM-L12-v2'; // Model multilingüe d'embeddings que suporta català natiu en format ONNX
// Altres alternatives en català que s'han de convertir en ONNX prèviament: 'projecte-aina/roberta-base-ca-v2'
const CHUNK_SIZE = 500; // Paraules per chunk aprox
const CHUNK_OVERLAP = 50; // Superposició de paraules per mantenir el context

/**
 * Neteja el text original d'un PDF convertit a TXT
 * Elimina salts de línia innecessaris, números de pàgina, etc.
 */
function cleanText(text) {
    return text
        // Eliminar capçaleres recurrents (ajustar segons el PDF)
        .replace(/© FUOC • PID_\d+\s+Fiscalitat directa/g, '')
        .replace(/© FUOC • PID_\d+\s+\d+\s+Fiscalitat directa/g, '')
        // Eliminar números de línia si el text s'ha copiat de l'editor
        // .replace(/^\d+:\s/gm, '') 
        // Eliminar múltiples salts de línia
        .replace(/\n{3,}/g, '\n\n')
        // Unir línies que pertanyen al mateix paràgraf (línies que no acaben en punt o similars)
        // Aquesta regex és bàsica, es pot millorar i adaptar al text
        .replace(/(?<![\.\?\!\]\n])\n(?!\n)(?![A-Z0-9])/g, ' ')
        .trim();
}

/**
 * Transforma un text llarg en chunks intel·ligents basats en paràgrafs i paraules
 */
function createChunks(text, filename) {
    const chunks = [];
    
    // Primer, dividir per paràgrafs dobles
    const paragraphs = text.split(/\n\n+/);
    
    let currentChunkWords = [];
    
    for (let p of paragraphs) {
        const words = p.split(/\s+/).filter(w => w.trim().length > 0);
        
        if (words.length === 0) continue;
        
        // Si afegir aquest paràgraf supera el límit
        if (currentChunkWords.length + words.length > CHUNK_SIZE && currentChunkWords.length > 0) {
            // Guardar el chunk actual
            const chunkText = currentChunkWords.join(' ');
            chunks.push({
                text: chunkText,
                metadata: {
                    source: filename,
                    wordCount: currentChunkWords.length
                }
            });
            
            // Iniciar nou chunk amb superposició (agafar les últimes N paraules de l'anterior)
            const overlap = currentChunkWords.slice(-CHUNK_OVERLAP);
            currentChunkWords = [...overlap, ...words];
        } else {
            // Afegir al chunk actual
            currentChunkWords = [...currentChunkWords, ...words];
        }
    }
    
    // Guardar l'últim chunk si en queda algun
    if (currentChunkWords.length > 0) {
        chunks.push({
            text: currentChunkWords.join(' '),
            metadata: {
                source: filename,
                wordCount: currentChunkWords.length
            }
        });
    }
    
    return chunks;
}

/**
 * Funció principal
 */
async function main() {
    console.log(`Iniciant pipeline RAG...`);
    
    // 1. Llegir fitxers
    const files = fs.readdirSync(DATA_DIR).filter(file => file.endsWith('.txt'));
    
    if (files.length === 0) {
         console.warn(`No s'han trobat fitxers .txt a la carpeta ${DATA_DIR}`);
         return;
    }
    
    console.log(`S'han trobat ${files.length} fitxers per processar.`);
    
    let allChunks = [];
    
    // 2. Processar cada fitxer i fer el chunking
    for (const file of files) {
        console.log(`Processant ${file}...`);
        const filePath = path.join(DATA_DIR, file);
        const text = fs.readFileSync(filePath, 'utf8');
        
        const cleanedText = cleanText(text);
        const chunks = createChunks(cleanedText, file);
        
        console.log(`  - Creats ${chunks.length} fragments (chunks).`);
        allChunks = [...allChunks, ...chunks];
    }
    
    console.log(`Total de fragments a processar: ${allChunks.length}`);
    
    // 3. Generar Embeddings amb Transformers.js
    console.log(`\nCarregant model: ${MODEL_NAME}... Això pot trigar una mica la primera vegada.`);
    try {
        // 'feature-extraction' genera els vectors
        const extractor = await pipeline('feature-extraction', MODEL_NAME, {
            quantized: true, // Usa menys RAM
        });
        
        console.log('Model carregat correctament. Generant embeddings...');
        
        const results = [];
        let count = 0;
        
        for (const chunk of allChunks) {
            count++;
            if (count % 10 === 0) {
                 console.log(`Processant chunk ${count}/${allChunks.length}...`);
            }
            
            // Generar vector. Amb pooling 'mean' o 'cls' per tenir un únic vector per text
            const output = await extractor(chunk.text, { pooling: 'mean', normalize: true });
            
            // Convertir el Tensor a Array pla
            const embeddingArray = Array.from(output.data);
            
            // Crear un ID únic per aquest chunk
            const id = crypto.createHash('md5').update(chunk.text).digest('hex');
            
            results.push({
                id,
                ...chunk,
                embedding: embeddingArray
            });
        }
        
        // 4. Guardar resultats
        console.log(`\nGuardant dades vectoritzades a ${OUTPUT_FILE}...`);
        fs.writeFileSync(OUTPUT_FILE, JSON.stringify(results, null, 2));
        console.log(`Process completat amb èxit! Mida del corpus: ${results.length} chunks.`);
        
    } catch (error) {
        console.error("Error generant embeddings:", error);
    }
}

main().catch(console.error);
