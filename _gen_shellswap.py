#!/usr/bin/env python3
"""Shell swap: afegir topbar/crumbs/footer brutalist a pàgines Tailwind complexes."""

FONTS_BRUTAL = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="brutal.css">"""

TOPBAR = """\
    <header class="topbar">
      <div class="topbar-row">
        <a href="index.html" class="tb-cell tb-brand">
          <span class="dot"></span>DRET <em style="font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;">visual</em>
        </a>
        <div class="tb-cell tb-grow" style="justify-content:flex-end;">
          <span class="mono" style="font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);">Repositori d'eines · 2026</span>
        </div>
        <nav class="nav-links">
          <a href="index.html">Home</a>
          <a href="dret-penal.html">Penal</a>
          <a href="dret-civil.html">Civil</a>
          <a href="dret-administratiu.html">Administratiu</a>
          <a href="dret-financer.html">Financer</a>
          <a href="dret-mercantil.html">Mercantil</a>
        </nav>
      </div>
    </header>"""

SITE_FOOT = """\
    <footer class="site-foot">
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


def swap(fname, crumbs_html, head_marker, body_marker, footer_start_marker, nav_link_href=None):
    """Read fname, apply shell swap transformations, write back."""
    with open(fname, encoding='utf-8') as f:
        html = f.read()

    # 1. Remove navbar.css link
    html = html.replace('    <link rel="stylesheet" href="navbar.css">\n', '')

    # 2. Add brutal.css + fonts just before </head>
    html = html.replace('</head>', FONTS_BRUTAL + '\n</head>', 1)

    # 3. Remove navbar/breadcrumb containers
    html = html.replace('    <div id="navbar-container"></div>\n', '')
    # breadcrumb may have variable class attr — use the specific line from file
    for bc in [
        '    <div id="breadcrumb-container" class="max-w-7xl mx-auto px-6 pt-24"></div>\n',
        '    <div id="breadcrumb-container" class="max-w-7xl mx-auto px-6 pt-24"></div>',
    ]:
        html = html.replace(bc, '')

    # 4. Insert topbar + crumbs before the first page-specific element
    topbar_crumbs = TOPBAR + '\n' + crumbs_html + '\n'
    html = html.replace(body_marker, topbar_crumbs + body_marker, 1)

    # 5. Replace old footer block (from footer_start_marker to </footer>) + navbar-helper
    #    Find footer start, then find its closing </footer>
    fi = html.find(footer_start_marker)
    if fi != -1:
        # find closing </footer> after fi
        fe = html.find('</footer>', fi)
        if fe != -1:
            fe += len('</footer>')
            html = html[:fi] + SITE_FOOT + html[fe:]

    # 6. Remove navbar-helper.js script line
    html = html.replace('\n    <script src="navbar-helper.js"></script>', '')
    html = html.replace('    <script src="navbar-helper.js"></script>\n', '')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK {fname}')


# ── dret-constitucional.html ──────────────────────────────────────────────────
CRUMBS_CONSTIT = """\
    <nav class="crumbs">
      <a href="index.html">Home</a><span class="sep">/</span>
      <a href="#">Dret</a><span class="sep">/</span>
      <span class="here">Dret Constitucional</span>
    </nav>"""

swap(
    'dret-constitucional.html',
    crumbs_html=CRUMBS_CONSTIT,
    head_marker=None,  # unused
    body_marker='    <!-- Header Section -->',
    footer_start_marker='    <!-- Footer -->\n    <footer class="relative z-10 bg-slate-900/50',
)

# ── dret-processal.html ───────────────────────────────────────────────────────
CRUMBS_PROCESSAL = """\
    <nav class="crumbs">
      <a href="index.html">Home</a><span class="sep">/</span>
      <a href="#">Dret</a><span class="sep">/</span>
      <span class="here">Dret Processal</span>
    </nav>"""

# processal has no explicit <footer> — we insert site-foot before </body>
def swap_processal(fname, crumbs_html):
    with open(fname, encoding='utf-8') as f:
        html = f.read()

    # 1. Remove navbar.css
    html = html.replace('    <link rel="stylesheet" href="navbar.css">\n', '')

    # 2. Add brutal.css + fonts before </head>
    html = html.replace('</head>', FONTS_BRUTAL + '\n</head>', 1)

    # 3. Remove navbar/breadcrumb containers
    html = html.replace('    <div id="navbar-container"></div>\n', '')
    html = html.replace('    <div id="breadcrumb-container" class="max-w-7xl mx-auto px-6 pt-24"></div>\n', '')
    html = html.replace('    <div id="breadcrumb-container" class="max-w-7xl mx-auto px-6 pt-24"></div>', '')

    # 4. Insert topbar + crumbs before <!-- Header -->
    marker = '    <!-- Header -->'
    topbar_crumbs = TOPBAR + '\n' + crumbs_html + '\n'
    html = html.replace(marker, topbar_crumbs + marker, 1)

    # 5. Insert site-foot + remove navbar-helper before </body>
    html = html.replace(
        '\n    <script src="navbar-helper.js"></script>\n</body>',
        '\n' + SITE_FOOT + '\n</body>'
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK {fname}')

swap_processal('dret-processal.html', CRUMBS_PROCESSAL)

print('Shell swap done.')
