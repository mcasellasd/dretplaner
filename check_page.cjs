const puppeteer = require('puppeteer');

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
    
    await page.goto('file:///Users/marccasellas/Desktop/docus2024/DOCUS 2026/legal data visualization/fiscalitat-directa.html', { waitUntil: 'networkidle0' });
    
    if (!hasError) console.log("No JS errors detected on load.");
    await browser.close();
})();
