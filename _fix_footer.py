#!/usr/bin/env python3
"""Afegeix site-foot a les pàgines que en manquen."""

SITE_FOOT = """    <footer class="site-foot">
      <div class="site-foot-inner">
        <div class="ff-cell">
          <h4>Sobre el projecte</h4>
          <div class="ff-brand">Dret <span class="amp">&amp;</span> <em>visual</em></div>
          <p style="margin:14px 0 0;color:#a8a8a0;font-family:'Instrument Serif',serif;font-style:italic;font-size:15px;letter-spacing:0;text-transform:none;line-height:1.5;">Una biblioteca lliure d'apunts, esquemes i vídeos del Dret espanyol i català.</p>
        </div>
        <div class="ff-cell">
          <h4>Matèries</h4>
          <ul>
            <li><a href="dret-penal.html">Penal</a></li>
            <li><a href="dret-civil.html">Civil</a></li>
            <li><a href="dret-administratiu.html">Administratiu</a></li>
            <li><a href="dret-constitucional.html">Constitucional</a></li>
            <li><a href="dret-processal.html">Processal</a></li>
            <li><a href="dret-financer.html">Financer</a></li>
            <li><a href="dret-mercantil.html">Mercantil</a></li>
          </ul>
        </div>
        <div class="ff-cell">
          <h4>Eines</h4>
          <ul>
            <li><a href="visuals.html">Cerca visuals</a></li>
            <li><a href="irpf-calculator.html">Calculadora IRPF</a></li>
            <li><a href="historia-dret.html">Fonaments</a></li>
          </ul>
        </div>
      </div>
      <div class="site-foot-bottom">
        <span>Tipografia: Space Grotesk · Instrument Serif · JetBrains Mono</span>
        <span>© MMXXVI · Dret Visual</span>
      </div>
    </footer>"""

pages = [
    'dret-processal-videos.html',
    'dret-constitucional-videos.html',
    'dret-financer-videos.html',
    'dret-administratiu-videos.html',
    'fiscalitat-directa.html',
    'irpf-calculator.html',
]

for fname in pages:
    with open(fname, encoding='utf-8') as f:
        html = f.read()
    if 'site-foot' not in html:
        html = html.replace('\n    <!-- Global Navigation Helper -->\n', '\n')
        html = html.replace('\n</body>', '\n' + SITE_FOOT + '\n</body>', 1)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Fixed {fname}')
    else:
        print(f'Already OK {fname}')
