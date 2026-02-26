        const ICONS = {
            blueDoc: `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>`,
            book: `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>`,
            shield: `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>`,
            landmark: `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><line x1="3" y1="22" x2="21" y2="22"/><line x1="6" y1="18" x2="6" y2="11"/><line x1="10" y1="18" x2="10" y2="11"/><line x1="14" y1="18" x2="14" y2="11"/><line x1="18" y1="18" x2="18" y2="11"/><polygon points="12 2 20 7 4 7"/></svg>`,
            briefcase: `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>`,
            gitcommit: `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><circle cx="12" cy="12" r="3"/><line x1="3" y1="12" x2="9" y2="12"/><line x1="15" y1="12" x2="21" y2="12"/></svg>`,
            help: `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>`
        };

        const topics = {
            conceptes: {
                title: "Concepte i Antecedents",
                icon: ICONS.blueDoc,
                description: "La realització de la justícia ha evolucionat històricament, prohibint l'ús de la força privada i derivant en institucions pacífiques per administrar el dret objectiu.",
                sections: [
                    { label: "Autotutela (Prohibida)", text: "Basada en la llei del més fort on el subjecte es pren la justícia per la seva pròpia mà. Actualment erradicada com a norma, degut als perills de proporció i manca d'imparcialitat." },
                    { label: "Autocomposició", text: "Fórmula de solució mitjançat l'acord de voluntats (com la mediació). El tercer és neutral i només apropa o ajuda a les parts sense imposar directament una decisió per la força." },
                    { label: "Heterocomposició (Jurisdicció)", text: "Resolució definitiva que es deriva a un tercer que actua 'supra partes' sota imparcialitat i independència. En el cas del procés judicial, el jutge aplica rígidament l'ordenament jurídic." }
                ],
                color: "indigo"
            },
            jurisdiccio: {
                title: "Principis Constitucionals",
                icon: ICONS.landmark,
                description: "La Constitució espanyola (Art. 117) conforma la jurisdicció com el Poder Judicial (Potestat de jutjar i fer executar el jutjat), separant-la rigorosament d'administració i del legislatiu.",
                sections: [
                    { label: "Monopoli i Exclusivitat", text: "Només l'Estat manté la jurisdicció front els particulars (impossibilitat de jurisdiccions privades) i només els òrgans previstos a la LOPJ tenen aquesta potestat excepte casos del Tribunal Constitucional o Tribunals internacionals." },
                    { label: "Unitat Jurisdiccional", text: "Prohibició de tribunals excepcionals o tribunals integrats per jutges que no formin part de la jurisdicció ordinària, unificant tot sota un règim jurídic exclusiu amb la LOPJ (117.5 CE)." },
                    { label: "Govern Autònom: CGPJ", text: "El Consell General del Poder Judicial lidera la jurisdicció sense que el Poder Executiu i Ministeri de Justícia intervingui sobre els jutges, vetllant per l'estatut, formació i el sistema d'elecció (20 membres)." }
                ],
                color: "slate"
            },
            principis: {
                title: "Principis dels Òrgans",
                icon: ICONS.shield,
                description: "El text de la LOPJ protegeix i exigeix als titulars de l'òrgan estrictes requisits formals per protegir el veredicte final i separar qualsevol decisió de l'arbitrarietat personal.",
                sections: [
                    { label: "Independència, Submissió i Inamovibilitat", text: "Són independents perquè estan exclusivament sotmesos només a la Llei (no pas submissió a altres entitats). A més, cap jutge pot ser separat, suspès, obligat o jubilat sense causa i aforament legal previst." },
                    { label: "Imparcialitat Objectiva i Subjectiva", text: "El jutge manté una posició purament neutral enfront a parts asimètriques, arbitrant abstencions o recusacions immediates si recau incidència, parentiu, o factors alterats." },
                    { label: "Responsabilitat Total", text: "Costat oposat i raó directe de la Independència; pot reclamar-se Responsabilitat Disciplinària per errada greu davant el CGPJ, i evidentment Penal o Civil via tribunals pel seu propi exèrcici operatiu." }
                ],
                color: "amber"
            },
            organization: {
                title: "Estructura i 4 Ordres",
                icon: ICONS.briefcase,
                description: "Hi ha tribunals col·legiats i unipersonals, distribuïts dintre dels marcats Quatre Ordres Jurisdiccionals que reordenen l'activitat per complexitat temàtica de forma ramificada.",
                customHtml: `
                    <div class="space-y-4">
                        <div class="grid md:grid-cols-2 gap-4">
                            <div class="bg-indigo-50/70 p-4 border border-indigo-100 rounded-xl">
                                <h4 class="font-bold text-sm text-indigo-800 uppercase tracking-widest mb-1">Ordre Civil i Penal</h4>
                                <p class="text-sm text-slate-700">El Civil atén dret privat i exerceix activitat residual o <em>vis attractiva</em> (Art. 9.2 LOPJ). El Penal domina causes o judicis criminals excloent militars.</p>
                            </div>
                            <div class="bg-slate-50/70 p-4 border border-slate-100 rounded-xl">
                                <h4 class="font-bold text-sm text-slate-800 uppercase tracking-widest mb-1">C. Administratiu i Social</h4>
                                <p class="text-sm text-slate-700">El C. Administratiu processa accions sobre l'activitat pública governativa; l'Ordre Social regula branques i assumptes materials laborals i drets de la Seguretat Social (Art. 9.5 LOPJ).</p>
                            </div>
                        </div>
                        <ul class="text-sm text-slate-600 space-y-2 mt-4 ml-2 border-l-2 border-slate-200 pl-4">
                            <li><strong>Tribunal Suprem (TS):</strong> Cúspide nacional (casació, unificació jurisprudencial).</li>
                            <li><strong>Audiència Nacional (AN):</strong> Nacional, delictes molt greus (terrorisme, etc).</li>
                            <li><strong>Tribunals Superiors (TSJ):</strong> Culminació ordinària exclusivament dins la CA.</li>
                            <li><strong>Audiències Provincials (AP):</strong> Coneix segona instància dins l'àmbit provincial.</li>
                            <li><strong>Jutjats Unipersonals:</strong> Exemples com Jutjats de Primera Instància i Instrucció, Els Penals, Contenciosos, Jutjats de Pau, Violència sobre la dona...</li>
                        </ul>
                    </div>
                `,
                color: "indigo"
            },
            subjects: {
                title: "Subjectes del Procés",
                icon: ICONS.gitcommit,
                description: "Totes aquelles persones físiques que formen l'entramat orgànic col·laborador integrat a les instàncies judicials, classificat pel seu servei públic central o auxiliar i funcional.",
                sections: [
                    { label: "Personal Jurisdiccional (El jutge)", text: "Aquell qui utilitza potestat: jutges ordinaris, magistrats amb major experiència situats normalment en Audiències o el Suprem. La pertinença a la carrera confereix protecció màxima en tots ells." },
                    { label: "Lletrat Administració i Oficina", text: "Al marge del jutge, el LAJ és director tècnic de l'Oficina d'ordre, garant de la fe pública judicial a la sala. L'oficina aporta tot el gruix informàtic, el personal general del cos tramitador i cos auxiliar permanent." },
                    { label: "Personal Col·laborador (Fiscal/Lletrats)", text: "Ministeri Fiscal defensea legalitat des d'un eix apolític i social; mentres Policia Judicial, Advocat de l'Estat, professionals liberals (Advocats pel Dret a la defensa, o Procuradors pel repte de Termini i Representació física) suporten globalment." }
                ],
                color: "emerald"
            },
            accio: {
                title: "L'Acció i Tutela Efectiva",
                icon: ICONS.book,
                description: "L'Acció i dret constitucional de tota la ciutadania de l'Estat cap als mecanismes d'apelació a justícia garantits.",
                sections: [
                    { label: "Dret Procés vs Dret Subjectiu", text: "Mitjançant abstractes (dret mer a intervenir sense condemna garantitzada) i concrets (s'exigeix cert nivell i proves de raó formal abans i durant). Un procés efectiu lliga al ciutadà exigint el veredicte formal objectiu, sigui en la forma que sigui finalment." },
                    { label: "Tutela Judicial (Art. 24 CE)", text: "Dret fonamental inviolable (emparat en l'Article 24), base que inclou dret d'accés absolut (l'admissió al lloc legal), prohibició taxativa de generar espais d'indefensió (garantides garanties de contradiccions) i el lliurat complet de recurs processal segons l'ordenament en vigor." }
                ],
                color: "blue"
            },
            quiz: {
                title: "Avaluació Ràpida",
                icon: ICONS.help,
                description: "Darrera revisió: Prova d'interiorització sobre materials bàsics establerts generalment al temari del recurs d'aprenentatge del mòdul Processal I.",
                customHtml: `
                    <div class="space-y-6">
                        <div class="p-6 bg-white border border-slate-200 rounded-2xl shadow-sm">
                            <h4 class="font-bold mb-4 text-slate-800 flex items-center gap-2"><div class="w-6 h-6 bg-indigo-100 text-indigo-700 rounded-full flex items-center justify-center text-xs">1</div>La jurisdicció entesa com a potestat s'aplica exclusivament mitjançant monopoli per l'Estat. Tanmateix, permet tribunals consuetudinaris tals com el del Jurat i l'existència de Jurisdiccions "Especials" privades externes (excepte si intervenen militarment). És correcte aquesta definició parcial d'unitat?</h4>
                            <div class="space-y-2" id="quiz-1-options">
                                <button onclick="checkAnswer(1, 'A')" class="w-full text-left px-5 py-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition quiz-btn shadow-sm text-sm text-slate-600">A) Fals. La jurisdicció espanyola no tolera ni empara pas tribunals internacionals de cap tipologia per exclusivitat absoluta total.</button>
                                <button onclick="checkAnswer(1, 'B')" class="w-full text-left px-5 py-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition quiz-btn shadow-sm text-sm text-slate-600">B) Fals. Segons la Constitució i LOPJ, les jurisdiccions purament privades són il·legals i el principi d'unitat dictamina exclusivitat al Poder Judicial formal creat.</button>
                            </div>
                            <div id="quiz-1-result" class="mt-4 hidden p-4 rounded-xl font-medium text-sm border"></div>
                        </div>

                        <div class="p-6 bg-white border border-slate-200 rounded-2xl shadow-sm">
                            <h4 class="font-bold mb-4 text-slate-800 flex items-center gap-2"><div class="w-6 h-6 bg-indigo-100 text-indigo-700 rounded-full flex items-center justify-center text-xs">2</div>Pel que respecta al TSJ (Tribunal Superior de Justícia) quina àrea d'actuació principal i àmbit assumeix habitualment per davant de les Audiències Provincials?</h4>
                            <div class="space-y-2" id="quiz-2-options">
                                <button onclick="checkAnswer(2, 'A')" class="w-full text-left px-5 py-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition quiz-btn shadow-sm text-sm text-slate-600">A) Posseeix rang i control màxim exclusiu en qüestions ubicades en una província tancada (exemple AP Girona), només un lloc sense més abast d'Estatut propi.</button>
                                <button onclick="checkAnswer(2, 'B')" class="w-full text-left px-5 py-3.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition quiz-btn shadow-sm text-sm text-slate-600">B) Cobreix l'Esglaó Superior corresponent al conjunt d'aplecs i territori de tota la pròpia Comunitat Autònoma, sobre passant en rang provincial habitualitzant recursos propis com unificació de dret de CA on n'hi hagués.</button>
                            </div>
                            <div id="quiz-2-result" class="mt-4 hidden p-4 rounded-xl font-medium text-sm border"></div>
                        </div>
                    </div>
                `,
                color: "indigo"
            }
        };

        const quizData = {
            1: { correct: 'B', msgCorrect: 'Correcte! La justícia s\\'exerceix sota monopoli legal i estan rotundament prohibides les "jurisdiccions" de caire pur privada entre dos no ratificades; al seu lloc existeixen els mecanismes de conformitat d\\'Estat.', msgWrong: 'Vigila la A...! Sí que es permeten alguns tribunals internacionals externs pel principi subrogatòria (ex: Tribunal Europeu Drets Humans / TJUE) ratificats.' },
            2: { correct: 'B', msgCorrect: 'Totalment exacte! El TSJ esdevé l\\'ordre que absorbeix els recursos ordinaris finalitzadors autonòmicament de la jurisdicció abans que intervingui algun eix nacional com Suprem directament (AN, etc)...', msgWrong: 'Errada... les competències únicament provincials recauríen inicialment naturalment cap a les seccions de l\\'Audiència Provincial, just per sota d\\'un TSJ autonòmic central.' }
        };

        function showTopic(key) {
            const topic = topics[key];
            const area = document.getElementById('content-area');

            // Actualitzar estils pestanyes
            document.querySelectorAll('#tabs button').forEach(btn => {
                btn.classList.remove('active-tab', 'text-indigo-600', 'font-bold');
                btn.classList.add('text-slate-500');
            });
            const activeBtn = document.getElementById(`btn-${key}`);
            activeBtn.classList.add('active-tab', 'text-indigo-600');
            if (key === 'quiz') activeBtn.classList.add('font-bold');
            activeBtn.classList.remove('text-slate-500');

            // Renderitzar
            area.innerHTML = `
                <div class="md:col-span-1 space-y-4 fade-in">
                    <div class="p-6 bg-white rounded-3xl border border-slate-200 shadow-sm sticky top-24">
                        <div class="w-14 h-14 rounded-2xl bg-${topic.color}-100 text-${topic.color}-600 flex items-center justify-center mb-5">
                            ${topic.icon}
                        </div>
                        <h2 class="text-2xl font-bold mb-3 text-slate-800 tracking-tight">${topic.title}</h2>
                        <p class="text-slate-600 text-sm leading-relaxed">${topic.description}</p>
                    </div>
                </div>
                <div class="${topic.customHtml ? 'md:col-span-2 space-y-4 fade-in' : 'md:col-span-2 grid sm:grid-cols-2 gap-5 fade-in content-start'}">
                    ${topic.customHtml ? topic.customHtml : topic.sections.map(s => `
                        <div class="p-6 bg-white rounded-2xl border border-slate-100 shadow-sm topic-card">
                            <h4 class="text-xs font-bold text-${topic.color}-600 uppercase tracking-wider mb-2">${s.label}</h4>
                            <p class="text-sm text-slate-700 leading-relaxed">${s.text}</p>
                        </div>
                    `).join('')}
                </div>
            `;
        }

        function checkAnswer(questionId, selectedId) {
            const buttons = document.querySelectorAll(`#quiz-${questionId}-options button`);
            const resultDiv = document.getElementById(`quiz-${questionId}-result`);
            const correctOption = quizData[questionId].correct;
            const isCorrect = (selectedId === correctOption);

            buttons.forEach(btn => {
                btn.classList.remove('bg-red-50', 'bg-green-50', 'border-red-300', 'border-green-300', 'text-red-900', 'text-green-900', 'font-semibold');
                btn.classList.add('bg-white', 'text-slate-600');
            });

            const currentBtn = event.currentTarget;
            currentBtn.classList.remove('bg-white', 'text-slate-600');

            if (isCorrect) {
                currentBtn.classList.add('bg-green-50', 'border-green-300', 'text-green-900', 'font-semibold');
                resultDiv.className = 'mt-5 p-4 rounded-xl font-medium text-sm border flex items-start gap-3 text-green-700 bg-green-50 border-green-200 fade-in';
                resultDiv.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg> <span>${quizData[questionId].msgCorrect}</span>`;
            } else {
                currentBtn.classList.add('bg-red-50', 'border-red-300', 'text-red-900', 'font-semibold');
                resultDiv.className = 'mt-5 p-4 rounded-xl font-medium text-sm border flex items-start gap-3 text-red-700 bg-red-50 border-red-200 fade-in';
                resultDiv.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg> <span>${quizData[questionId].msgWrong}</span>`;
            }
            resultDiv.classList.remove('hidden');
        }

        // Init
        window.addEventListener('DOMContentLoaded', () => {
            showTopic('conceptes');
        });
