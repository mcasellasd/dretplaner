const puppeteer = require('puppeteer');
const path = require('path');
const { pathToFileURL } = require('url');

const targetFile = path.resolve(__dirname, 'fiscalitat-directa.html');
const targetUrl = pathToFileURL(targetFile).href;

(async () => {
    let hasError = false;
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    page.on('console', msg => {
        if (msg.type() === 'error') {
            console.error('PAGE ERROR LOG:', msg.text());
            hasError = true;
        }
    });
    
    page.on('pageerror', err => {
        console.error('PAGE ERROR EXCEPTION:', err.toString());
        hasError = true;
    });
    
    await page.goto(targetUrl, { waitUntil: 'networkidle0' });
    
    if (!hasError) console.log("No JS errors detected on load.");
    await browser.close();
})();
