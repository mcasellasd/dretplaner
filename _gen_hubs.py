#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate brutalist hub pages (dret-administratiu, dret-financer)."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FONTS_LINK = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">'

HUB_CSS = """
.page{max-width:1440px;margin:0 auto;}
.hub-section{border-top:2px solid var(--ink);}
.hub-section-head{padding:28px 32px 20px;display:flex;align-items:baseline;gap:16px;border-bottom:1px solid var(--ink);}
.hub-section-head h2{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:clamp(20px,2.5vw,32px);letter-spacing:-.025em;margin:0;text-transform:uppercase;}
.hub-section-head .note{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);}
.hub-grid{display:grid;border-left:1px solid var(--ink);}
.hub-grid.cols-5{grid-template-columns:repeat(5,1fr);}
.hub-grid.cols-4{grid-template-columns:repeat(4,1fr);}
.hub-grid.cols-3{grid-template-columns:repeat(3,1fr);}
.hub-card{border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);padding:32px 28px;display:flex;flex-direction:column;gap:8px;transition:background .15s,color .15s;color:var(--ink);text-decoration:none;min-height:220px;}
.hub-card:not(.disabled):hover{background:var(--ink);color:var(--paper);}
.hub-card:not(.disabled):hover .card-num,.hub-card:not(.disabled):hover .card-sub,.hub-card:not(.disabled):hover p{opacity:.7;}
.hub-card:not(.disabled):hover .cta{opacity:1;border-top-color:var(--paper);}
.hub-card.disabled{opacity:.4;cursor:default;}
.card-num{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.15em;text-transform:uppercase;opacity:.5;}
.card-sub{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.1em;text-transform:uppercase;opacity:.6;color:var(--accent);}
.hub-card h3{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:clamp(15px,1.5vw,20px);line-height:1.2;letter-spacing:-.02em;margin:8px 0 0;flex:1;}
.hub-card p{font-size:13px;line-height:1.55;opacity:.65;margin:0;}
.cta{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;margin-top:auto;padding-top:14px;border-top:1px solid var(--ink);opacity:.5;}
.pendent-chip{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;border:1px solid var(--ink);padding:3px 8px;display:inline-block;align-self:flex-start;}
.hub-note{border-top:2px solid var(--ink);display:grid;grid-template-columns:1fr 2fr;}
.hub-note-left{background:var(--ink);color:var(--paper);padding:40px 36px;display:flex;flex-direction:column;gap:12px;}
.hub-note-left h3{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:clamp(20px,2.5vw,30px);letter-spacing:-.025em;margin:0;text-transform:uppercase;}
.hub-note-left .num{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;opacity:.5;}
.hub-note-right{background:var(--paper-2);padding:40px 36px;}
.hub-note-right p{font-family:'Instrument Serif',serif;font-style:italic;font-size:18px;line-height:1.6;color:var(--ink);margin:0;}
@media(max-width:1100px){.hub-grid.cols-5{grid-template-columns:repeat(3,1fr);}.hub-grid.cols-4{grid-template-columns:repeat(2,1fr);}.hub-note{grid-template-columns:1fr;}}
@media(max-width:768px){.hub-grid.cols-5,.hub-grid.cols-4,.hub-grid.cols-3{grid-template-columns:repeat(2,1fr);}.hub-section-head{padding:20px 20px 14px;}.hub-card{padding:22px 18px;}}
@media(max-width:480px){.hub-grid.cols-5,.hub-grid.cols-4,.hub-grid.cols-3{grid-template-columns:1fr;}.hub-card{border-right:none;}}
"""

FOOTER = """<footer class="site-foot">
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
    <span>Tipografia: Space Grotesk &middot; Instrument Serif &middot; JetBrains Mono</span>
    <span>&copy; MMXXVI &middot; Dret Visual</span>
  </div>
</footer>"""

ALL_NAVLINKS = [
    ('index.html', 'Home'),
    ('dret-penal.html', 'Penal'),
    ('dret-civil.html', 'Civil'),
    ('dret-administratiu.html', 'Administratiu'),
    ('dret-financer.html', 'Financer'),
    ('dret-mercantil.html', 'Mercantil'),
]


def render_topbar(active):
    links_html = '\n'.join(
        f'      <a href="{href}"{" class=\"active\"" if href == active else ""}>{label}</a>'
        for href, label in ALL_NAVLINKS
    )
    return f"""<header class="topbar">
  <div class="topbar-row">
    <a href="index.html" class="tb-cell tb-brand">
      <span class="dot"></span>DRET <em style="font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;">visual</em>
    </a>
    <div class="tb-cell tb-grow" style="justify-content:flex-end;">
      <span class="mono" style="font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);">Repositori d'eines &middot; 2026</span>
    </div>
    <nav class="nav-links">
{links_html}
    </nav>
  </div>
</header>"""


def render_crumbs(items):
    parts = []
    for i, (label, url) in enumerate(items):
        if url and i < len(items) - 1:
            parts.append(f'<a href="{url}">{label}</a>')
        else:
            parts.append(f'<span class="here">{label}</span>')
    return '<nav class="crumbs">' + '<span class="sep">/</span>'.join(parts) + '</nav>'


def render_hero(eyebrow, title_html, lede, meta_cells, branch_color):
    cells = ''.join(f'<div class="cell"><b>{b}</b>{t}</div>' for b, t in meta_cells)
    return f"""<section class="hero" style="--branch:{branch_color};">
  <div class="hero-inner">
    <div class="eyebrow"><span class="sq"></span>{eyebrow}</div>
    <h1>{title_html}</h1>
    <p class="lede">{lede}</p>
  </div>
  <div class="hero-meta">{cells}</div>
</section>"""


def hub_card(num_label, sub_label, title, desc, cta_text, href=None, disabled=False):
    if disabled:
        return f"""    <div class="hub-card disabled">
      <div class="card-num">{num_label}</div>
      <div class="card-sub">{sub_label}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
      <div class="pendent-chip">Pendent</div>
    </div>"""
    return f"""    <a href="{href}" class="hub-card">
      <div class="card-num">{num_label}</div>
      <div class="card-sub">{sub_label}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
      <div class="cta">{cta_text} &rarr;</div>
    </a>"""


def it(text):
    return f"<span style=\"font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;\">{text}</span>"


def build_hub(filename, title, crumb_json, active, crumbs_list,
              eyebrow, title_html, lede, meta, branch,
              sections_html, extra_css=''):
    css = HUB_CSS + extra_css
    head = f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="breadcrumbs" content='{crumb_json}'>
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS_LINK}
<link rel="stylesheet" href="brutal.css">
<style>{css}</style>
</head>"""
    body = f"""<body class="grid-bg">
{render_topbar(active)}
{render_crumbs(crumbs_list)}
<div class="page">
{render_hero(eyebrow, title_html, lede, meta, branch)}
{sections_html}
</div>
{FOOTER}
</body>
</html>"""
    return head + '\n' + body


# ============================================================
# DRET ADMINISTRATIU
# ============================================================
admin_cards = '\n'.join([
    hub_card('M&ograve;dul I', 'Fonts i Reglament', 'Dret Administratiu I',
             "Fonaments de l'Administraci&oacute; p&uacute;blica, sistema de fonts, potestat reglament&agrave;ria, actes administratius i mecanismes de control.",
             'Entrar al M&ograve;dul I', 'dret-administratiu-i.html'),
    hub_card('M&ograve;dul II', 'Garanties Jurisdiccionals', 'Dret Administratiu II',
             "Jurisdicci&oacute; contenciosa administrativa, pretensions, procediments, mesures cautelars, recursos i glossari processal.",
             'Entrar al M&ograve;dul II', 'dret-administratiu-ii.html'),
    hub_card('M&ograve;dul III', 'Expropiaci&oacute; For&ccedil;osa', 'Dret Administratiu III',
             "Guia completa d'expropiaci&oacute; for&ccedil;osa: fonament constitucional, elements, procediment ordinari i d'urg&egrave;ncia, i garanties del cidad&agrave;.",
             'Entrar al M&ograve;dul III', 'dret-administratiu-iii.html'),
    hub_card('M&ograve;dul IV', 'Responsabilitat Patrimonial', 'Dret Administratiu IV',
             "Responsabilitat patrimonial de l'Administraci&oacute;: fonaments, requisits del dany, causalitat, procediment i indemnitzaci&oacute;.",
             'Entrar al M&ograve;dul IV', 'dret-administratiu-iv.html'),
    hub_card('Tema Extra', 'LCSP, SARA i Recursos', 'Contractaci&oacute; P&uacute;blica',
             "S&iacute;ntesi ampliada de GES i PID sobre contractes del sector p&uacute;blic, procediments d'adjudicaci&oacute;, prerrogatives i recurs especial.",
             'Obrir Contractaci&oacute; P&uacute;blica', 'dret-administratiu-contractacio-publica.html'),
])

admin_note = """  <div class="hub-note">
    <div class="hub-note-left">
      <div class="num">Com estudiar-ho</div>
      <h3>Itinerari recomanat</h3>
    </div>
    <div class="hub-note-right">
      <p>Comença pel Mòdul I per consolidar les bases del sistema de fonts. Continua amb el Mòdul II per la jurisdicció i la tutela judicial. Treballa el Mòdul III per dominar l'expropiació forçosa i tanca amb el Mòdul IV sobre responsabilitat patrimonial. Utilitza Contractació Pública com a bloc específic sobre LCSP i adjudicació.</p>
    </div>
  </div>"""

admin_sections = f"""  <section class="hub-section">
    <div class="hub-section-head">
      <h2>M&ograve;duls i {it("Continguts")}</h2>
      <span class="note">5 blocs tematics</span>
    </div>
    <div class="hub-grid cols-5">
{admin_cards}
    </div>
  </section>
{admin_note}
  <section class="hub-section">
    <div class="hub-section-head">
      <h2>V&iacute;deos</h2>
      <span class="note">Material audiovisual complementari</span>
    </div>
    <div class="hub-grid cols-3">
    <a href="dret-administratiu-videos.html" class="hub-card">
      <div class="card-num">Recursos</div>
      <div class="card-sub">V&iacute;deos</div>
      <h3>V&iacute;deos de Dret Administratiu</h3>
      <p>Material audiovisual complementari per consolidar els conceptes dels m&ograve;duls.</p>
      <div class="cta">Veure v&iacute;deos &rarr;</div>
    </a>
    </div>
  </section>"""

admin_html = build_hub(
    'dret-administratiu.html',
    'Dret Administratiu | Dret Visual',
    '[{"label":"Home","url":"index.html"},{"label":"Dret","url":"#"},{"label":"Dret Administratiu"}]',
    'dret-administratiu.html',
    [('Home', 'index.html'), ('Dret', '#'), ('Dret Administratiu', None)],
    'Assignatura &middot; Dret Administratiu',
    'Dret <span class="em" style="color:var(--b-administ)">Administratiu</span>',
    "L'Administraci&oacute; p&uacute;blica i el ciutad&agrave;: fonts, jurisdicci&oacute;, expropiaci&oacute;, responsabilitat patrimonial i contractaci&oacute; p&uacute;blica.",
    [('5', 'M&ograve;duls'), ('4', 'Blocs DA I-IV'), ('LCSP', 'Contractaci&oacute;'), ('2026', 'Actualitzat')],
    'var(--b-administ)',
    admin_sections,
)

with open(os.path.join(BASE, 'dret-administratiu.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)
print('OK dret-administratiu.html')


# ============================================================
# DRET FINANCER
# ============================================================
financer_cards = '\n'.join([
    hub_card('M&ograve;dul 1', 'Fiscalitat Directa', 'La Fiscalitat Directa',
             "An&agrave;lisi visual interactiu de l'IRPF, IS, Impost sobre el Patrimoni, Successions i Donacions i Renda de No Residents.",
             'Obrir Manual', 'fiscalitat-directa.html'),
    hub_card('M&ograve;dul 2', 'IVA &middot; ITP &middot; AJD', 'La Fiscalitat Indirecta',
             "Impost sobre el Valor Afegit (IVA), Impost sobre Transmissions Patrimonials i Actes Jur&iacute;dics Documentats (ITP i AJD).",
             '', disabled=True),
    hub_card('M&ograve;dul 3', 'LGT', 'Procediments Tribut&agrave;ris',
             "Llei General Tribut&agrave;ria: aplicaci&oacute; dels tributs, gesti&oacute;, inspecci&oacute;, recaptaci&oacute; i r&egrave;gim d'infraccions i sancions.",
             '', disabled=True),
    hub_card('M&ograve;dul 4', 'Cicle Pressupostari', 'Dret Pressupostari',
             "Estudi del cicle pressupostari, elaboraci&oacute;, aprovaci&oacute;, execuci&oacute; i control de la despesa de les Administracions P&uacute;bliques.",
             '', disabled=True),
])

financer_note = """  <div class="hub-note">
    <div class="hub-note-left">
      <div class="num">Estat del contingut</div>
      <h3>Disponible ara</h3>
    </div>
    <div class="hub-note-right">
      <p>La Fiscalitat Directa ja és disponible amb anàlisi visual completa de l'IRPF, IS, Impost sobre el Patrimoni i l'ISD. Els mòduls de Fiscalitat Indirecta, Procediments Tributaris i Dret Pressupostari s'estan construint i s'habilitaran progressivament.</p>
    </div>
  </div>"""

financer_sections = f"""  <section class="hub-section">
    <div class="hub-section-head">
      <h2>M&ograve;duls i {it("Continguts")}</h2>
      <span class="note">4 blocs &middot; 1 disponible</span>
    </div>
    <div class="hub-grid cols-4">
{financer_cards}
    </div>
  </section>
{financer_note}
  <section class="hub-section">
    <div class="hub-section-head">
      <h2>Eines {it("fiscals")}</h2>
      <span class="note">Calculadores i recursos</span>
    </div>
    <div class="hub-grid cols-3">
    <a href="irpf-calculator.html" class="hub-card">
      <div class="card-num">Eina</div>
      <div class="card-sub">IRPF</div>
      <h3>Calculadora IRPF</h3>
      <p>Calcula la quota &iacute;ntegra i la tarifa progressiva de l'IRPF de forma interactiva.</p>
      <div class="cta">Obrir calculadora &rarr;</div>
    </a>
    <a href="dret-financer-videos.html" class="hub-card">
      <div class="card-num">Recursos</div>
      <div class="card-sub">V&iacute;deos</div>
      <h3>V&iacute;deos de Dret Financer</h3>
      <p>Material audiovisual complementari per consolidar els conceptes tribut&agrave;ris.</p>
      <div class="cta">Veure v&iacute;deos &rarr;</div>
    </a>
    </div>
  </section>"""

financer_html = build_hub(
    'dret-financer.html',
    'Dret Financer i Tributari | Dret Visual',
    '[{"label":"Home","url":"index.html"},{"label":"Fiscalitat","url":"#"},{"label":"Dret Financer i Tributari"}]',
    'dret-financer.html',
    [('Home', 'index.html'), ('Fiscalitat', '#'), ('Dret Financer i Tributari', None)],
    'Assignatura &middot; Dret Financer i Tributari',
    'Dret <span class="em" style="color:var(--b-financer)">Financer</span>',
    "Regula l'establiment i l'aplicaci&oacute; dels tributs (Dret Tribut&agrave;ri) i la gesti&oacute; dels ingressos p&uacute;blics (Dret Pressupostari).",
    [('4', 'M&ograve;duls'), ('15+', 'Conceptes clau'), ('LGT', 'Llei General'), ('2026', 'Actualitzat')],
    'var(--b-financer)',
    financer_sections,
)

with open(os.path.join(BASE, 'dret-financer.html'), 'w', encoding='utf-8') as f:
    f.write(financer_html)
print('OK dret-financer.html')

print('\nHub pages done.')
