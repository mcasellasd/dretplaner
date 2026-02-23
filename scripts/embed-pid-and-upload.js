import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { env, pipeline } from '@xenova/transformers';
import { QdrantClient } from '@qdrant/js-client-rest';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

dotenv.config();

env.localModelPath = './models';
env.allowRemoteModels = true;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DATA_DIR = path.join(__dirname, '../data');
const INPUT_FILE = path.join(DATA_DIR, 'pid_00302181_chunks_20260223_170718.json');

const MODEL_NAME = 'Xenova/paraphrase-multilingual-MiniLM-L12-v2';
const COLLECTION_NAME = process.env.QDRANT_COLLECTION ? process.env.QDRANT_COLLECTION.replace(/"/g, '') : 'materials_docents';
const VECTOR_SIZE = 384;

async function main() {
    if (!fs.existsSync(INPUT_FILE)) {
        console.error(`El fitxer ${INPUT_FILE} no existeix.`);
        return;
    }

    console.log(`Llegint ${INPUT_FILE}...`);
    const fileContent = fs.readFileSync(INPUT_FILE, 'utf8');
    
    let documents;
    try {
        documents = JSON.parse(fileContent);
    } catch(e) {
        console.error("No s'ha pogut parsejar el fitxer JSON", e);
        return;
    }

    console.log(`S'han llegit ${documents.length} documents del JSON.`);

    console.log(`\nCarregant model: ${MODEL_NAME}...`);
    let extractor;
    try {
        extractor = await pipeline('feature-extraction', MODEL_NAME, {
            quantized: true,
        });
    } catch (e) {
        console.error("Error al carregar el model:", e);
        return;
    }

    console.log('Model carregat correctament. Generant embeddings...');

    const points = [];
    let count = 0;

    for (const doc of documents) {
        count++;
        if (count % 50 === 0) {
            console.log(`Processant document ${count}/${documents.length}...`);
        }
        
        let output;
        try {
            output = await extractor(doc.text, { pooling: 'mean', normalize: true });
        } catch(e) {
             console.error(`Error a l'extreure embeddings al doc ${count}`, e);
             continue;
        }

        const embeddingArray = Array.from(output.data);
        
        // Crear un ID únic (hash md5) basat en el text (com es feia en l'script original) i convertir a UUID
        const hash = crypto.createHash('md5').update(doc.text).digest('hex');
        const uuid = `${hash.slice(0, 8)}-${hash.slice(8, 12)}-${hash.slice(12, 16)}-${hash.slice(16, 20)}-${hash.slice(20, 32)}`;
        
        points.push({
            id: uuid,
            vector: embeddingArray,
            payload: {
                text: doc.text,
                source: doc.meta && doc.meta.source_pdf ? doc.meta.source_pdf : 'pid_00302181_chunks_20260223_170718.json',
                chunk_index: doc.id
            }
        });
    }

    console.log('Embeddings generats. Connectant a Qdrant...');
    
    // Netejar la URL i la Col·lecció (en el .env hi havia cometes)
    const qdrantUrl = process.env.QDRANT_URL.replace(/"/g, '');
    const qdrantKey = process.env.QDRANT_API_KEY ? process.env.QDRANT_API_KEY.replace(/"/g, '') : undefined;
    
    const client = new QdrantClient({
        url: qdrantUrl,
        apiKey: qdrantKey,
    });

    try {
        const collections = await client.getCollections();
        const exists = collections.collections.some((c) => c.name === COLLECTION_NAME);

        if (!exists) {
            console.log(`Creant la col·lecció nova '${COLLECTION_NAME}'...`);
            await client.createCollection(COLLECTION_NAME, {
                vectors: {
                    size: VECTOR_SIZE,
                    distance: 'Cosine',
                },
            });
            console.log("Col·lecció lesta!");
        } else {
            console.log(`La col·lecció '${COLLECTION_NAME}' ja existeix. Afegint nous vectors sense eliminar els existents.`);
        }

        console.log("Pujant informació a Qdrant...");
        const BATCH_SIZE = 100;
        for (let i = 0; i < points.length; i += BATCH_SIZE) {
            const batch = points.slice(i, i + BATCH_SIZE);
            await client.upsert(COLLECTION_NAME, {
                wait: true,
                points: batch
            });
            console.log(`--> Pujats ${Math.min(i + BATCH_SIZE, points.length)} / ${points.length} punts.`);
        }

        console.log("\n✅ Procés finalitzat amb èxit! El fitxer JSON ha estat incrustat i integrat a la base de coneixement.");
        
    } catch (error) {
        console.error("❌ S'ha produït un error:", error);
    }
}

main().catch(console.error);
