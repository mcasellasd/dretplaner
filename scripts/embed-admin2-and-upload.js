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
const INPUT_FILE = path.join(DATA_DIR, 'admin 2/PID_00278996_chunks.jsonl');

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
    const lines = fileContent.split('\n').filter(line => line.trim().length > 0);

    const documents = lines.map((line, index) => {
        try {
            return JSON.parse(line);
        } catch (error) {
            console.error(`Línia JSONL invàlida (${index + 1})`, error);
            return null;
        }
    }).filter(Boolean);

    console.log(`S'han llegit ${documents.length} documents del JSONL.`);

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
        if (!doc.text) {
            continue;
        }

        count++;
        if (count % 50 === 0) {
            console.log(`Processant document ${count}/${documents.length}...`);
        }

        let output;
        try {
            output = await extractor(doc.text, { pooling: 'mean', normalize: true });
        } catch (error) {
            console.error(`Error a l'extreure embeddings al doc ${count}`, error);
            continue;
        }

        const embeddingArray = Array.from(output.data);

        const hash = crypto.createHash('md5').update(doc.text).digest('hex');
        const uuid = `${hash.slice(0, 8)}-${hash.slice(8, 12)}-${hash.slice(12, 16)}-${hash.slice(16, 20)}-${hash.slice(20, 32)}`;

        points.push({
            id: uuid,
            vector: embeddingArray,
            payload: {
                text: doc.text,
                source: doc.source_file || doc.title || 'PID_00278996_chunks.jsonl',
                chunk_index: doc.chunk_id || doc.id || doc.page_start || count,
                doc_id: doc.doc_id || 'PID_00278996'
            }
        });
    }

    console.log('Embeddings generats. Connectant a Qdrant...');

    const qdrantUrl = process.env.QDRANT_URL ? process.env.QDRANT_URL.replace(/"/g, '') : '';
    const qdrantKey = process.env.QDRANT_API_KEY ? process.env.QDRANT_API_KEY.replace(/"/g, '') : undefined;

    if (!qdrantUrl) {
        console.error("Falta QDRANT_URL al fitxer .env");
        return;
    }

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
            console.log('Col·lecció lesta!');
        } else {
            console.log(`La col·lecció '${COLLECTION_NAME}' ja existeix. Afegint nous vectors sense eliminar els existents.`);
        }

        console.log('Pujant informació a Qdrant...');
        const BATCH_SIZE = 100;
        for (let i = 0; i < points.length; i += BATCH_SIZE) {
            const batch = points.slice(i, i + BATCH_SIZE);
            await client.upsert(COLLECTION_NAME, {
                wait: true,
                points: batch
            });
            console.log(`--> Pujats ${Math.min(i + BATCH_SIZE, points.length)} / ${points.length} punts.`);
        }

        console.log('\n✅ Procés finalitzat amb èxit! El fitxer JSONL d\'admin 2 ha estat incrustat i integrat a la base de coneixement.');
    } catch (error) {
        console.error("❌ S'ha produït un error:", error);
    }
}

main().catch(console.error);
