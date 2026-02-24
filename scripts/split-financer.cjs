const fs = require('fs');

const fileVideos = 'dret-financer-videos.html';
const fileText = 'dret-financer.html';

let contentV = fs.readFileSync(fileVideos, 'utf8');
let contentT = fs.readFileSync(fileText, 'utf8');

// For videos: keep Audiovisual, REMOVE Distribuïdor de Continguts
// Distribuïdor starts with <!-- Títol de Secció --> and ends just before <!-- Script per a funcionalitat del Chatbot RAG -->
const distRegex = /<!-- Títol de Secció -->([\s\S]*?)<!-- Script per a funcionalitat del Chatbot RAG -->/;
contentV = contentV.replace(distRegex, '<!-- Script per a funcionalitat del Chatbot RAG -->');

// Also update the title to "Vídeos Dret Financer"
contentV = contentV.replace('<title>Dret Financer i Tributari | Dret Català Visual</title>', '<title>Vídeos - Dret Financer | Dret Català Visual</title>');

// For texts: keep Distribuïdor, REMOVE Audiovisual
// Audiovisual starts with <!-- Contingut Audiovisual --> and ends just before the next <!-- Títol de Secció --> (the Distribuïdor one)
const audioRegex = /<!-- Contingut Audiovisual -->([\s\S]*?)(?=<!-- Títol de Secció -->)/;
contentT = contentT.replace(audioRegex, '');

fs.writeFileSync(fileVideos, contentV);
fs.writeFileSync(fileText, contentT);
console.log('Split financer files successfully.');
