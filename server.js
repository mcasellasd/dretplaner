import express from 'express';
import cors from 'cors';
import { QdrantClient } from '@qdrant/js-client-rest';
import OpenAI from 'openai';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

// Serveix els fitxers de la carpeta actual (HTML, CSS, assets)
app.use(express.static(__dirname));

const MODEL_NAME = 'Xenova/paraphrase-multilingual-MiniLM-L12-v2';
const COLLECTION_NAME = process.env.QDRANT_COLLECTION || 'materials_docents';

const qdrant = new QdrantClient({
    url: process.env.QDRANT_URL,
    apiKey: process.env.QDRANT_API_KEY,
});

const openai = new OpenAI({
    apiKey: process.env.VITE_OPENAI_API_KEY,
});

let extractor;
async function getExtractor() {
    if (!extractor) {
        console.log("Cargant model de Transformers.js en memòria (pot trigar)...");
        const { pipeline, env } = await import('@xenova/transformers');
        
        // Configuració de Transformers.js per ús local
        env.localModelPath = './models';
        env.allowRemoteModels = true; 
        
        extractor = await pipeline('feature-extraction', MODEL_NAME, {
            quantized: true,
        });
        console.log("Model de Transformers carregat!");
    }
    return extractor;
}

app.post('/api/chat', async (req, res) => {
    try {
        const { message } = req.body;
        if (!message) {
            return res.status(400).json({ error: 'Message is required' });
        }

        // 1. Crear vector de la pregunta
        const extract = await getExtractor();
        const output = await extract(message, { pooling: 'mean', normalize: true });
        const vector = Array.from(output.data);

        // 2. Cercar a Qdrant
        const searchResults = await qdrant.search(COLLECTION_NAME, {
            vector: vector,
            limit: 10,    // Recuperar els 10 fragments més rellevants per donar més context legal
            with_payload: true,
        });

        const contextTexts = searchResults.map((hit) => {
            return `[Font: ${hit.payload.source || 'Desconeguda'}]\n${hit.payload.text}`;
        }).join('\n\n');

        const systemPrompt = `Ets un assistent IA expert en dret i actues com a professor particular de Dret. 
Respon a les preguntes dels estudiants utilitzant ÚNICAMENT el context proporcionat extret de la legislació i apunts del curs que t'adjuntem sota d'aquest prompt. 
Ara disposes dels textos legals literals (IRPF, IS, Successions, etc.). Si el context inclou el text literal de les lleis o articles pertinents, cita'ls i reprodueix-ne les parts essencials de manera literal si ajuda a l'explicació.
Si la resposta no es troba en absolut en el context, indica amablement que no ho saps d'acord amb els materials docents actuals i no inventis informació.
Respon sempre en català de manera educativa i accessible, utilitzant format markdown (*negretes*, llistes, etc) quan calgui per a més claredat.

CONTEXT DELS APUNTS I LLEIS (Resultats de RAG semàntic):
${contextTexts}
`;
        
        // 3. Demanar resposta a OpenAI amb el context
        const completion = await openai.chat.completions.create({
            model: 'gpt-4o-mini', 
            messages: [
                { role: 'system', content: systemPrompt },
                { role: 'user', content: message }
            ],
            temperature: 0.1,
        });

        const reply = completion.choices[0].message.content;

        // Extraure les fonts diferents per retornar-les
        const fontsRaw = searchResults.map(hit => hit.payload.source);
        const fontsUnique = [...new Set(fontsRaw)];

        res.json({
            reply,
            sources: fontsUnique
        });

    } catch (error) {
        console.error("Error al xat:", error);
        res.status(500).json({ error: "No s'ha pogut processar la consulta" });
    }
});

export default app;

if (process.env.NODE_ENV !== 'production') {
    const PORT = process.env.PORT || 3000;
    app.listen(PORT, () => {
        console.log(`🚀 Servidor i Web App en marxa a http://localhost:${PORT}`);
        console.log(`🤖 Chatbot API llest a http://localhost:${PORT}/api/chat`);
    });
}
