import fs from 'fs';
import path from 'path';
import { QdrantClient } from '@qdrant/js-client-rest';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DATA_DIR = path.join(__dirname, '../data');
const INPUT_FILE = path.join(DATA_DIR, 'corpus-embeddings.json');
const COLLECTION_NAME = process.env.QDRANT_COLLECTION || 'materials_docents';
const VECTOR_SIZE = 384; // Mida per al model Xenova/paraphrase-multilingual-MiniLM-L12-v2

async function main() {
    if (!fs.existsSync(INPUT_FILE)) {
        console.error(`El fitxer ${INPUT_FILE} no existeix. Si us plau, executa primer el procés de generar els embeddings.`);
        return;
    }

    const data = JSON.parse(fs.readFileSync(INPUT_FILE, 'utf8'));
    console.log(`Carregats ${data.length} embeddings locals llestos per pujar.`);

    // Connexió a Qdrant
    // Agafarà valors per defecte si no en tens a un .env local, dirigint-se al teu docker local (http://localhost:6333)
    const client = new QdrantClient({
        url: process.env.QDRANT_URL || 'http://localhost:6333',
        apiKey: process.env.QDRANT_API_KEY || undefined,
    });

    try {
        console.log(`Connectant a Qdrant en ${process.env.QDRANT_URL || 'http://localhost:6333'}...`);
        
        // Comprovar si existeix la col·lecció
        const collections = await client.getCollections();
        const exists = collections.collections.some((c) => c.name === COLLECTION_NAME);

        if (exists) {
            console.log(`La col·lecció '${COLLECTION_NAME}' ja existeix. Recreant-la manualment per forçar la càrrega des de zero.`);
            await client.deleteCollection(COLLECTION_NAME);
            console.log("Col·lecció esborrada amb èxit.");
        }
        
        console.log(`Creant la col·lecció nova '${COLLECTION_NAME}'...`);
        await client.createCollection(COLLECTION_NAME, {
            vectors: {
                size: VECTOR_SIZE,
                distance: 'Cosine',
            },
        });
        console.log("Col·lecció lesta!");

        console.log("Pujant tots els fragments de text amb el seu embedding a Qdrant...");
        
        // Formatatge de l'UUID. Qdrant necessita números positius o UUIDs per a l'ID.
        // Transformem els nostres IDs de md5 (hexadecimal de 32 de longitud) a un format UUID estàndard.
        const formattedPoints = data.map((item) => {
            const hash = item.id;
            const uuid = `${hash.slice(0, 8)}-${hash.slice(8, 12)}-${hash.slice(12, 16)}-${hash.slice(16, 20)}-${hash.slice(20, 32)}`;
            return {
                id: uuid,
                vector: item.embedding,
                payload: {
                    text: item.text,
                    source: item.metadata.source,
                    wordCount: item.metadata.wordCount
                }
            };
        });

        // Pugem la informació ràpidament fent paquets
        const BATCH_SIZE = 100;
        for (let i = 0; i < formattedPoints.length; i += BATCH_SIZE) {
            const batch = formattedPoints.slice(i, i + BATCH_SIZE);
            await client.upsert(COLLECTION_NAME, {
                wait: true,
                points: batch
            });
            console.log(`--> Pujats ${i + batch.length} / ${formattedPoints.length} punts.`);
        }

        console.log("\n✅ Procés finalitzat amb èxit! Tots els teus apunts docents estan carregats i indexats en Qdrant.");
    } catch (error) {
        console.error("❌ S'ha produït un error de connexió amb Qdrant:", error.message);
        console.log("\nHas configurat el URL correcte (i l'API Key, si es tracta de Cloud) al directori '.env'?");
    }
}

main().catch(console.error);
