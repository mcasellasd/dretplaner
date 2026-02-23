const fs = require('fs');

const directes = fs.readFileSync('impostos-directes.html', 'utf-8');
const fiscalitat = fs.readFileSync('fiscalitat-directa.html', 'utf-8');

// 1. Get calculator section
const calcSectionMatch = directes.match(/<!-- Calculadora de Rendiments -->[\s\S]*?(?=<\/div>\s*<footer)/);
if (!calcSectionMatch) throw new Error("Could not find calc html");

// 2. Get the JS part
const jsMatch = directes.match(/\/\/ --- CALCULADORA PIONERA LÒGICA \(VANILLA JS\) ---[\s\S]*?\/\/ --- END CALCULADORA PIONERA LÒGICA ---/);
if (!jsMatch) throw new Error("Could not find calc js");

// Let's modify fiscalitat-directa.html
let newFiscalitat = fiscalitat.replace(
    /<button onclick="showTax\('irnr'\)" id="btn-irnr"[\s\S]*?<\/button>/,
    `$&
            <button onclick="showCalc()" id="btn-calc"
                class="px-6 py-3 text-sm text-slate-500 hover:text-blue-600">Calculadora</button>`
);

// We need to inject the calculator JS
newFiscalitat = newFiscalitat.replace(
    /function showTax\(key\) \{/,
    `${jsMatch[0]}

        function showCalc() {
            const area = document.getElementById('content-area');
            
            // Actualitzar pestanyes
            document.querySelectorAll('#tabs button').forEach(btn => {
                btn.classList.remove('active-tab');
                btn.classList.add('text-slate-500');
            });
            const btnCalc = document.getElementById('btn-calc');
            if (btnCalc) {
                btnCalc.classList.add('active-tab');
                btnCalc.classList.remove('text-slate-500');
            }
            
            // Set area to full width
            area.className = "w-full";
            
            area.innerHTML = \`<div class="bg-white p-6 md:p-10 rounded-3xl shadow-xl border border-slate-200 mt-0 w-full animate-fade-in" id="calculadora-section">
                <!-- Capçalera calculador -->
                <header class="mb-8 text-center">
                    <h2 class="text-3xl font-extrabold text-slate-800 mb-2 flex items-center justify-center gap-3">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-blue-600" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                            <rect width="16" height="20" x="4" y="2" rx="2" />
                            <line x1="8" x2="16" y1="6" y2="6" />
                            <line x1="16" x2="16" y1="14" y2="18" />
                            <path d="M16 10h.01" />
                            <path d="M12 10h.01" />
                            <path d="M8 10h.01" />
                            <path d="M12 14h.01" />
                            <path d="M8 14h.01" />
                            <path d="M12 18h.01" />
                            <path d="M8 18h.01" />
                        </svg>
                        Simulador Pràctic
                    </h2>
                    <p class="text-slate-500 text-sm">Calcula la quota tributària seguint les taules de l'Estat</p>
                </header>
                
                <!-- Tabs de Calculadora -->
                <div class="flex flex-wrap gap-2 mb-8 bg-slate-50 p-2 rounded-xl shadow-inner border border-slate-200">
                    <button onclick="calcTab('irpf')" id="calc-tab-irpf" class="flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-lg transition-all duration-300 bg-blue-600 text-white shadow-md font-semibold text-sm hover:scale-[1.02]">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M22 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>
                        IRPF
                    </button>
                    <button onclick="calcTab('is')" id="calc-tab-is" class="flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-lg transition-all duration-300 hover:bg-white border border-transparent hover:border-slate-200 text-slate-500 font-semibold text-sm">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2" ry="2" /><path d="M9 22v-4h6v4" /><path d="M8 6h.01" /><path d="M16 6h.01" /><path d="M12 6h.01" /><path d="M12 10h.01" /><path d="M12 14h.01" /><path d="M16 10h.01" /><path d="M16 14h.01" /><path d="M8 10h.01" /><path d="M8 14h.01" /></svg>
                        IS (Societats)
                    </button>
                    <button onclick="calcTab('ip')" id="calc-tab-ip" class="flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-lg transition-all duration-300 hover:bg-white border border-transparent hover:border-slate-200 text-slate-500 font-semibold text-sm">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12V7H5a2 2 0 0 1 0-4h14v4" /><path d="M3 5v14a2 2 0 0 0 2 2h16v-5" /><path d="M18 12a2 2 0 0 0 0 4h4v-4Z" /></svg>
                        IP (Patrimoni)
                    </button>
                </div>
                
                <main class="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
                    <div class="md:col-span-2 bg-slate-50 p-6 rounded-2xl border border-slate-200" id="calc-forms"></div>
                    <div class="bg-indigo-900 border border-slate-800 text-white p-6 rounded-2xl shadow-2xl flex flex-col h-fit sticky top-24" id="calc-results"></div>
                </main>
            </div>\`;
            
            calcTab('irpf');
        }

        function showTax(key) {`
);

// We must amend showTax to restore grid classes!
newFiscalitat = newFiscalitat.replace(
            /const area = document\.getElementById\('content-area'\);/,
            `const area = document.getElementById('content-area');
            area.className = "grid md:grid-cols-3 gap-8";`
);

fs.writeFileSync('fiscalitat-directa.html', newFiscalitat);
console.log('Modified fiscalitat-directa.html successfully.');

