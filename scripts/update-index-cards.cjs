const fs = require('fs');

const file = 'index.html';
let content = fs.readFileSync(file, 'utf8');

const mapping = {
    '1. Dret Penal (Actiu) ': { color: 'red', videos: 'dret-penal.html', text: 'dret-penal-text.html' },
    '2. Dret Civil (Actiu) ': { color: 'purple', videos: 'dret-civil.html', text: 'dret-civil-text.html' },
    '3. Dret Financer i Tributari (Actiu als interactius) ': { color: 'blue', videos: 'dret-financer-videos.html', text: 'dret-financer.html' },
    '4. Dret Mercantil ': { color: 'amber', videos: 'dret-mercantil.html', text: 'dret-mercantil-text.html' },
    '5. Dret Públic (General) ': { color: 'emerald', videos: '#', text: '#' },
    '6. Fonaments del Dret / Història ': { color: 'stone', videos: 'historia-dret.html', text: 'historia-dret-text.html' },
    '7. Dret Processal Civil ': { color: 'rose', videos: 'dret-processal.html', text: 'dret-processal-text.html' }
};

for (const [key, cardRef] of Object.entries(mapping)) {
    const marker = '<!-- ' + key + '-->';
    const parts = content.split(marker);
    if (parts.length === 2) {
        let afterMarker = parts[1];
        
        const blockRegex = /^\s*<a href="[^"]*" class="block group">([\s\S]*?)<\/a>/;
        afterMarker = afterMarker.replace(blockRegex, (match, innerContent) => {
            const bottomDivRegex = /<div\s+class="mt-8 flex items-center[^>]*>[\s\S]*?<\/div>\n\s*<\/div>/;
            
            const buttonsHtml = `
                    <div class="mt-auto pt-4 flex gap-3 relative z-20 w-full opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 transition-all duration-300">
                        <a href="${cardRef.videos}" class="flex-1 flex justify-center items-center gap-2 py-2.5 rounded-xl bg-${cardRef.color}-500/20 hover:bg-${cardRef.color}-500/30 text-${cardRef.color}-400 font-semibold text-sm transition-colors border border-${cardRef.color}-500/30">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3" /></svg>
                            Vídeos
                        </a>
                        <a href="${cardRef.text}" class="flex-1 flex justify-center items-center gap-2 py-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 font-semibold text-sm transition-colors border border-slate-600/50">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20" /></svg>
                            Mòduls
                        </a>
                    </div>
                </div>`;
            return `\n            <div class="block group h-full">` + innerContent.replace(bottomDivRegex, buttonsHtml) + `</div>`;
        });
        
        content = parts[0] + marker + afterMarker;
    } else {
        console.warn('Did not find exactly one match for marker: ' + marker);
    }
}

fs.writeFileSync(file, content);
console.log('Fixed cards!');
