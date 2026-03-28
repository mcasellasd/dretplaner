import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const inputFile = path.resolve(__dirname, 'impostos-directes.html');
const outputFile = path.resolve(__dirname, 'test_script.js');
const html = fs.readFileSync(inputFile, 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
    fs.writeFileSync(outputFile, scriptMatch[1]);
    console.log('Script extracted!');
}
