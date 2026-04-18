#!/usr/bin/env python3
"""Batch shell swap: brutalist topbar/crumbs/footer per a totes les pàgines restants."""

import re
import os

# ─── Components reutilitzables ────────────────────────────────────────────────

FONTS_BRUTAL = """\
    <link rel="preconnect" href="https://fonts.googleapis.com">
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


def make_crumbs(label, parent_label=None, parent_url=None):
    if parent_label and parent_url:
        return (
            f'    <nav class="crumbs">\n'
            f'      <a href="index.html">Home</a><span class="sep">/</span>\n'
            f'      <a href="{parent_url}">{parent_label}</a><span class="sep">/</span>\n'
            f'      <span class="here">{label}</span>\n'
            f'    </nav>'
        )
    else:
        return (
            f'    <nav class="crumbs">\n'
            f'      <a href="index.html">Home</a><span class="sep">/</span>\n'
            f'      <span class="here">{label}</span>\n'
            f'    </nav>'
        )


def shell_swap(fname, crumbs_html):
    """Apply brutalist shell swap to a Tailwind page."""
    if not os.path.exists(fname):
        print(f'SKIP (not found): {fname}')
        return

    with open(fname, encoding='utf-8') as f:
        html = f.read()

    # 1. Remove navbar.css link (both with and without trailing spaces)
    html = re.sub(r'    <link rel="stylesheet" href="navbar\.css"[ /]*>\n', '', html)

    # 2. Add brutal.css + fonts before </head>
    html = html.replace('</head>', FONTS_BRUTAL + '\n</head>', 1)

    # 3. Remove navbar-container + breadcrumb-container divs
    #    Replace both together (they're usually consecutive) with topbar + crumbs
    pattern = (
        r'(\s*)<div id="navbar-container"><\/div>\n'
        r'\s*<div id="breadcrumb-container"[^>]*><\/div>'
    )
    replacement = '\n' + TOPBAR + '\n' + crumbs_html
    new_html, count = re.subn(pattern, replacement, html, count=1)

    if count == 0:
        # Fallback: try to insert topbar+crumbs just before </body> via separate removal
        html = re.sub(r'\s*<div id="navbar-container"><\/div>\n?', '', html)
        html = re.sub(r'\s*<div id="breadcrumb-container"[^>]*><\/div>\n?', '', html)
        # Insert after <body ...>
        html = re.sub(
            r'(<body[^>]*>)',
            r'\1\n' + TOPBAR + '\n' + crumbs_html,
            html, count=1
        )
        new_html = html
        print(f'  [fallback topbar insert] {fname}')

    html = new_html

    # 4. Replace old footer: find <footer ...> ... </footer> and replace with site-foot
    footer_pattern = r'(\s*<!-- Footer -->\s*)?\s*<footer\b[^>]*>.*?</footer>'
    new_html2, fcount = re.subn(footer_pattern, '\n' + SITE_FOOT, html, count=1, flags=re.DOTALL)

    if fcount == 0:
        print(f'  [no footer found, appending] {fname}')
        new_html2 = html

    html = new_html2

    # 5. Remove navbar-helper.js script
    html = re.sub(r'\n?\s*<script src="navbar-helper\.js"><\/script>\n?', '\n', html)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK {fname}')


# ─── Pàgines a processar ──────────────────────────────────────────────────────

PAGES = [
    # Pàgines de vídeos
    ('dret-processal-videos.html',       'Vídeos · Dret Processal',      'Dret Processal',         'dret-processal.html'),
    ('dret-constitucional-videos.html',  'Vídeos · Dret Constitucional', 'Dret Constitucional',    'dret-constitucional.html'),
    ('dret-financer-videos.html',        'Vídeos · Dret Financer',       'Dret Financer',          'dret-financer.html'),
    ('dret-administratiu-videos.html',   'Vídeos · Dret Administratiu',  'Dret Administratiu',     'dret-administratiu.html'),

    # Sub-pàgines de Processal
    ('dret-processal-ii.html',           'Mòdul II — El Procés',         'Dret Processal',         'dret-processal-moduls.html'),
    ('dret-processal-iii.html',          'Mòdul III — Pressupòsits',     'Dret Processal',         'dret-processal-moduls.html'),
    ('dret-processal-moduls.html',       'Mòduls — Selecció',            'Dret Processal',         'dret-processal.html'),

    # Sub-pàgines de Dret Administratiu
    ('dret-administratiu-i.html',        'Mòdul I',                       'Dret Administratiu',     'dret-administratiu.html'),
    ('dret-administratiu-ii.html',       'Mòdul II',                      'Dret Administratiu',     'dret-administratiu.html'),
    ('dret-administratiu-iii.html',      'Mòdul III',                     'Dret Administratiu',     'dret-administratiu.html'),
    ('dret-administratiu-iv.html',       'Mòdul IV',                      'Dret Administratiu',     'dret-administratiu.html'),
    ('dret-administratiu-contractacio-publica.html', 'Contractació Pública', 'Dret Administratiu',  'dret-administratiu.html'),

    # Sub-pàgines de Dret Civil
    ('dret-civil-familia.html',          'Família',                       'Dret Civil',             'dret-civil.html'),
    ('dret-civil-matrimoni-estudis.html','Matrimoni',                     'Dret Civil',             'dret-civil.html'),
    ('dret-civil-dissoluciomatrimoni.html', 'Dissolució del Matrimoni',  'Dret Civil',             'dret-civil.html'),
    ('dret-civil-filiacio.html',         'Filiació',                      'Dret Civil',             'dret-civil.html'),
    ('dret-civil-successori.html',       'Dret Successori',               'Dret Civil',             'dret-civil.html'),
    ('dret-civil-text.html',             'Textos Civils',                 'Dret Civil',             'dret-civil.html'),

    # Temes de Dret Penal Econòmic
    ('dret-penal-economic-tema4.html',   'Tema 4',                        'Penal Econòmic',         'dret-penal-economic.html'),
    ('dret-penal-economic-tema14.html',  'Tema 14',                       'Penal Econòmic',         'dret-penal-economic.html'),
    ('dret-penal-economic-tema15.html',  'Tema 15',                       'Penal Econòmic',         'dret-penal-economic.html'),

    # Sub-pàgines de Dret Financer
    ('fiscalitat-directa.html',          'Fiscalitat Directa',            'Dret Financer',          'dret-financer.html'),
    ('impostos-directes.html',           'Impostos Directes',             'Dret Financer',          'dret-financer.html'),
    ('impost-societats.html',            'Impost de Societats',           'Dret Financer',          'dret-financer.html'),
    ('impost-patrimoni.html',            'Impost sobre el Patrimoni',     'Dret Financer',          'dret-financer.html'),
    ('irpf.html',                        'IRPF',                          'Dret Financer',          'dret-financer.html'),
    ('isd.html',                         'ISD',                           'Dret Financer',          'dret-financer.html'),

    # Eines
    ('visuals.html',                     'Cerca Visuals',                 None,                     None),
    ('irpf-calculator.html',             'Calculadora IRPF',              None,                     None),
]

for fname, label, parent_label, parent_url in PAGES:
    crumbs = make_crumbs(label, parent_label, parent_url)
    shell_swap(fname, crumbs)

print('\nBatch shell swap completat.')
