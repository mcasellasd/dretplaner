#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate brutalist video pages for the Dret Visual site."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

FONTS_LINK = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">'

PAGE_CSS = """
.page{max-width:1440px;margin:0 auto;}
.vid-section{border-top:2px solid var(--ink);}
.vid-section-head{padding:28px 32px 20px;display:flex;align-items:baseline;gap:16px;border-bottom:1px solid var(--ink);}
.vid-section-head h2{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:clamp(22px,3vw,36px);letter-spacing:-.025em;margin:0;text-transform:uppercase;}
.vid-section-head .count{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);}
.vid-grid{display:grid;grid-template-columns:repeat(4,1fr);border-left:1px solid var(--ink);}
.vid-card{border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);display:flex;flex-direction:column;transition:background .15s;cursor:pointer;text-decoration:none;color:var(--ink);}
.vid-card:hover{background:var(--paper-2);}
.vid-card .thumb{position:relative;aspect-ratio:16/9;overflow:hidden;border-bottom:1px solid var(--ink);}
.vid-card .thumb img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s;}
.vid-card:hover .thumb img{transform:scale(1.04);}
.vid-card .thumb .play{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(10,10,10,.3);transition:background .15s;}
.vid-card:hover .thumb .play{background:rgba(10,10,10,.55);}
.vid-card .body{padding:16px 18px 20px;flex:1;}
.vid-card .body .tag{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:8px;}
.vid-card .body h3{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:16px;line-height:1.25;letter-spacing:-.015em;margin:0;}
@media(max-width:900px){.vid-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:560px){.vid-grid{grid-template-columns:1fr;}.vid-section-head{padding:20px 20px 14px;}.vid-card .body{padding:12px 14px 16px;}}
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

MODAL_JS = """<script>
(function(){
  var m=document.createElement('div');
  m.id='_vm';
  m.style.cssText='display:none;position:fixed;inset:0;z-index:500;background:rgba(0,0,0,.92);align-items:center;justify-content:center;';
  m.innerHTML='<div style="position:relative;width:90%;max-width:960px;aspect-ratio:16/9;"><button id="_vc" style="position:absolute;top:-44px;right:0;background:rgba(255,255,255,.15);border:1.5px solid rgba(255,255,255,.4);color:#fff;padding:8px 14px;cursor:pointer;font-family:JetBrains Mono,monospace;font-size:11px;letter-spacing:.1em;text-transform:uppercase;">TANCAR &#x2715;</button><iframe id="_yt" style="width:100%;height:100%;border:none;" allowfullscreen allow="autoplay; encrypted-media"></iframe></div>';
  document.body.appendChild(m);
  function close(){m.style.display='none';document.getElementById('_yt').src='';}
  document.getElementById('_vc').addEventListener('click',close);
  m.addEventListener('click',function(e){if(e.target===m)close();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  document.querySelectorAll('a[href*="youtube.com"],a[href*="youtu.be"]').forEach(function(a){
    a.addEventListener('click',function(e){
      e.preventDefault();
      var url=a.href,id='';
      if(url.indexOf('watch?v=')>-1)id=new URL(url).searchParams.get('v');
      else if(url.indexOf('/shorts/')>-1)id=url.split('/shorts/')[1].split('?')[0];
      else if(url.indexOf('youtu.be/')>-1)id=url.split('youtu.be/')[1].split('?')[0];
      if(id){document.getElementById('_yt').src='https://www.youtube.com/embed/'+id+'?autoplay=1';m.style.display='flex';}
    });
  });
})();
</script>"""

ALL_NAVLINKS = [
    ('index.html', 'Home'),
    ('dret-penal.html', 'Penal'),
    ('dret-civil.html', 'Civil'),
    ('dret-administratiu.html', 'Administratiu'),
    ('dret-financer.html', 'Financer'),
    ('dret-mercantil.html', 'Mercantil'),
]


def it(text):
    return f"<span style=\"font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;\">{text}</span>"


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


def vc(vid_id, title, tag='V&iacute;deo', url=None):
    """Render a single video card."""
    if url is None:
        url = f'https://www.youtube.com/watch?v={vid_id}'
    thumb = f'https://img.youtube.com/vi/{vid_id}/hqdefault.jpg'
    play = '<svg width="32" height="32" viewBox="0 0 24 24" fill="#fff"><polygon points="5 3 19 12 5 21 5 3"/></svg>'
    return f"""      <a href="{url}" target="_blank" class="vid-card">
        <div class="thumb"><img src="{thumb}" alt="{title}" loading="lazy"><div class="play">{play}</div></div>
        <div class="body"><div class="tag">{tag}</div><h3>{title}</h3></div>
      </a>"""


def render_section(title_html, count, cards):
    count_str = f'{count} v&iacute;deo{"s" if count != 1 else ""}'
    cards_html = '\n'.join(cards)
    return f"""  <section class="vid-section">
    <div class="vid-section-head">
      <h2>{title_html}</h2>
      <span class="count">{count_str}</span>
    </div>
    <div class="vid-grid">
{cards_html}
    </div>
  </section>"""


def build_page(filename, title, crumb_json, active, crumbs_list,
               eyebrow, title_html, lede, meta, branch, sections,
               extra_css='', extra_after_hero=''):
    css_block = PAGE_CSS + extra_css
    head_block = f"""<!DOCTYPE html>
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
<style>{css_block}</style>
</head>"""
    body = f"""<body class="grid-bg">
{render_topbar(active)}
{render_crumbs(crumbs_list)}
<div class="page">
{render_hero(eyebrow, title_html, lede, meta, branch)}
{extra_after_hero}
<main>
{chr(10).join(sections)}
</main>
</div>
{FOOTER}
{MODAL_JS}
</body>
</html>"""
    return head_block + '\n' + body


# ============================================================
# DRET PENAL
# ============================================================
penal_secs = [
    render_section(f'Introducci&oacute; i {it("Teoria del Delicte")}', 2, [
        vc('qt8nYMw63hc', 'Introducci&oacute; al Dret Penal', 'V&iacute;deo &middot; Conceptes'),
        vc('wGyVxccve4w', "L'anatomia d'un Delicte", 'V&iacute;deo &middot; Teoria'),
    ]),
    render_section(f'Delictes contra {it("la persona")}', 7, [
        vc('rNHjzPAKZt4', 'Delictes contra la vida: qu&egrave; diu el Codi Penal'),
        vc('C2z2C1xfFIw', 'Homicidi vs Assassinat', 'V&iacute;deo &middot; Cas'),
        vc('EG8m-NYDNEo', 'Delictes Contra la Salut i Integritat'),
        vc('Db4RIsTLDmE', 'Delictes Contra la Llibertat'),
        vc('4Cm3Or6a27Q', 'Delictes contra la Llibertat Sexual a Espanya'),
        vc('kgcv1z1n0Bw', 'Delictes contra la fam&iacute;lia'),
        vc('-nvhTeUNxgc', "Delictes Contra la Intimitat i l'Honor"),
    ]),
    render_section(f'Responsabilitat penal de {it("les persones jur&iacute;diques")}', 1, [
        vc('y3TFGW4iy5o', 'Responsabilitat penal de les persones jur&iacute;diques',
           'V&iacute;deo &middot; RPPJ', 'https://youtu.be/y3TFGW4iy5o'),
    ]),
    render_section(f'Delictes {it("patrimonials")}', 3, [
        vc('BpiqGtyPRI8', 'Delictes Contra el Patrimoni: An&agrave;lisi Jur&iacute;dica'),
        vc('_fWSpqd9JnI', 'Furt vs. Robatori: la Difer&egrave;ncia Jur&iacute;dica Clau', 'V&iacute;deo &middot; Cas'),
        vc('aIkDLUI8X6w', "Doctrina de l'Autotutela &ndash; La paradoxa de l'estafador"),
    ]),
    render_section(f'Altres {it("b&eacute;ns jur&iacute;dics")}', 3, [
        vc('QfS-naVKWsk', 'Delicte contra la Seguretat Vi&agrave;ria'),
        vc('01BXRFuLdC4', 'El delicte de tr&agrave;fic de drogues'),
        vc('n9CqraOgItQ', 'Delictes sobre Drogues', 'Short',
           'https://www.youtube.com/shorts/n9CqraOgItQ'),
    ]),
]

penal = build_page(
    'dret-penal.html',
    'Dret Penal | Dret Visual',
    '[{"label":"Home","url":"index.html"},{"label":"Dret","url":"#"},{"label":"Dret Penal"}]',
    'dret-penal.html',
    [('Home', 'index.html'), ('Dret', '#'), ('Dret Penal', None)],
    'Assignatura &middot; Dret Penal',
    'Dret <span class="em" style="color:var(--b-penal)">Penal</span>',
    "Descobreix els l&iacute;mits del <em>ius puniendi</em> de l'Estat. Compr&egrave;n l'estructura dels delictes, els seus elements essencials i com s'apliquen les penes al Codi Penal espanyol.",
    [('16', 'V&iacute;deos'), ('5', 'Seccions'), ('CP', 'Codi Penal'), ('2026', 'Actualitzat')],
    'var(--b-penal)',
    penal_secs,
)
with open(os.path.join(BASE, 'dret-penal.html'), 'w', encoding='utf-8') as f:
    f.write(penal)
print('OK dret-penal.html')

# ============================================================
# DRET CIVIL
# ============================================================
CIVIL_SUBNAV_CSS = """
.sub-nav{max-width:1440px;margin:0 auto;display:flex;flex-wrap:wrap;border-bottom:2px solid var(--ink);}
.sub-nav a{padding:13px 18px;font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;border-right:1px solid var(--ink);transition:background .15s;color:var(--ink);}
.sub-nav a.active,.sub-nav a:hover{background:var(--ink);color:var(--paper);}
@media(max-width:900px){.sub-nav a{padding:10px 12px;font-size:9px;}}
"""

civil_subnav_html = """<nav class="sub-nav" aria-label="Sub-seccions Civil">
  <a href="dret-civil.html" class="active">V&iacute;deos</a>
  <a href="dret-civil-text.html">M&ograve;duls</a>
  <a href="dret-civil-familia.html">Fam&iacute;lia</a>
  <a href="dret-civil-matrimoni-estudis.html">Matrimoni</a>
  <a href="dret-civil-dissoluciomatrimoni.html">Dissoluci&oacute;</a>
  <a href="dret-civil-filiacio.html">Filiaci&oacute;</a>
  <a href="dret-civil-successori.html">Successions</a>
</nav>"""

civil_secs = [
    render_section(f'Fonaments i {it("Conceptes Generals")}', 2, [
        vc('UDRFAdTs6VU', 'Dret P&uacute;blic vs Dret Privat', 'V&iacute;deo &middot; Fonaments'),
        vc('o9dmq9UHmvM', 'Dret Civil: El negoci jur&iacute;dic', 'V&iacute;deo &middot; Teoria'),
    ]),
    render_section(f'Drets Reals i {it("Propietat")}', 9, [
        vc('9dcKzcXwDYc', 'Els drets reals de garantia'),
        vc('6MG_o_8DFl8', 'El Registre de la Propietat'),
        vc('QXrkNn7MGMY', "Dret d'adquisici&oacute; preferent"),
        vc('VF6f-I0oekw', 'Drets Reals: Gaudi i C&agrave;rregues'),
        vc('c3dvcCCnEvo', 'La Propietat Horitzontal'),
        vc('y9CnaVhOyHM', "L'adquisici&oacute; de la propietat a Catalunya"),
        vc('cn_otkfcNqA', 'La defensa de la possessi&oacute;'),
        vc('QYzy2YEZIcQ', 'Les immissions'),
        vc('KImCmJ9IoOc', 'Propietat dels b&eacute;ns mobles al s. XXI'),
    ]),
    render_section(f'Obligacions i {it("Contractes")}', 2, [
        vc('BACnb9ZHQJ8', 'La llei del lloguer a Catalunya', 'V&iacute;deo &middot; Arrendament'),
        vc('sJeuLl3MFW0', "Llei 5/2025 de l'asseguran&ccedil;a a motor", 'V&iacute;deo &middot; 2025'),
    ]),
    render_section(f'Dret de Fam&iacute;lia i {it("Successions")}', 4, [
        vc('QMOvEYQuIcQ', 'El matrimoni a Catalunya', 'V&iacute;deo &middot; Fam&iacute;lia'),
        vc('Smcs9Fixr9k', 'La filiaci&oacute;', 'V&iacute;deo &middot; Filiaci&oacute;'),
        vc('VLkXP75Wp04', 'Successions i donacions a Catalunya', 'V&iacute;deo &middot; Successions'),
        vc('QrLFPSxmJ9M', "Inefic&agrave;cia i Dissoluci&oacute; del Matrimoni",
           'V&iacute;deo', 'https://youtu.be/QrLFPSxmJ9M'),
    ]),
]

civil = build_page(
    'dret-civil.html',
    'Dret Civil | Dret Visual',
    '[{"label":"Home","url":"index.html"},{"label":"Dret","url":"#"},{"label":"Dret Civil"}]',
    'dret-civil.html',
    [('Home', 'index.html'), ('Dret', '#'), ('Dret Civil', None)],
    'Assignatura &middot; Dret Civil',
    'Dret <span class="em" style="color:var(--b-civil)">Civil</span>',
    "Drets reals, propietat, obligacions, contractes, fam&iacute;lia i successions sota el prisma del Dret Civil espanyol i catal&agrave;.",
    [('16', 'V&iacute;deos'), ('4', 'Seccions'), ('CCCat', 'Catalunya'), ('2026', 'Actualitzat')],
    'var(--b-civil)',
    civil_secs,
    extra_css=CIVIL_SUBNAV_CSS,
    extra_after_hero=civil_subnav_html,
)
with open(os.path.join(BASE, 'dret-civil.html'), 'w', encoding='utf-8') as f:
    f.write(civil)
print('OK dret-civil.html')

# ============================================================
# DRET MERCANTIL
# ============================================================
mercantil_secs = [
    render_section(f'Fonaments del {it("Dret Mercantil")}', 4, [
        vc('1-naVGf5oa4', 'Qu&egrave; &eacute;s el Dret Mercantil', 'V&iacute;deo &middot; Fonaments'),
        vc('10nuCbERYPE', "L'estructura jur&iacute;dica del mercat"),
        vc('ToIB9tw5j80', 'La compet&egrave;ncia lliure i lleial', 'V&iacute;deo &middot; Compet&egrave;ncia'),
        vc('Sc22kjTNQ6w', 'La Propietat Industrial', 'V&iacute;deo &middot; Protecci&oacute;'),
    ]),
    render_section(f'Contractaci&oacute; Mercantil i {it("Consumidors")}', 3, [
        vc('QHQj_oMj0lA', "L'acceptaci&oacute; informal. L'ok com a requisit de validesa",
           'V&iacute;deo &middot; Contractes'),
        vc('Ki4yxK2NDIU', 'El Consumidor en el Dret Mercantil 1', 'V&iacute;deo &middot; Consum'),
        vc('H_4Z3v6a_rA', 'Cl&agrave;usules Abusives'),
    ]),
    render_section(f'T&iacute;tols Valor i {it("Noves Tecnologies")}', 2, [
        vc('LcJbEM0oaCo', 'La Lletra de Canvi', 'V&iacute;deo &middot; T&iacute;tols Valor'),
        vc('OdfZ5Gjkklg', 'Del Paper al Codi'),
    ]),
]

mercantil = build_page(
    'dret-mercantil.html',
    'Dret Mercantil | Dret Visual',
    '[{"label":"Home","url":"index.html"},{"label":"Dret","url":"#"},{"label":"Dret Mercantil"}]',
    'dret-mercantil.html',
    [('Home', 'index.html'), ('Dret', '#'), ('Dret Mercantil', None)],
    'Assignatura &middot; Dret Mercantil',
    'Dret <span class="em" style="color:var(--b-mercantil)">Mercantil</span>',
    "El dret dels empresaris i dels mercats. Compr&egrave;n la contractaci&oacute; mercantil, la protecci&oacute; del consumidor, la propietat industrial i els t&iacute;tols valor.",
    [('9', 'V&iacute;deos'), ('3', 'Seccions'), ('CCo', 'Codi de Comer&ccedil;'), ('2026', 'Actualitzat')],
    'var(--b-mercantil)',
    mercantil_secs,
)
with open(os.path.join(BASE, 'dret-mercantil.html'), 'w', encoding='utf-8') as f:
    f.write(mercantil)
print('OK dret-mercantil.html')

# ============================================================
# HISTORIA DRET / FONAMENTS
# ============================================================
historia_secs = [
    render_section(f'Fonaments del {it("Dret")}', 3, [
        vc('pZewFd9TX4c', 'Dret: El Codi Font de la Civilitzaci&oacute;', 'V&iacute;deo &middot; Teoria'),
        vc('UEXIFvYP-_I', "El Problema de l'Obedi&egrave;ncia al Dret", 'V&iacute;deo &middot; Filosofia'),
        vc('PqNfL3k5MvM', "L'Ordre Social i el Dret", 'Short &middot; Teoria',
           'https://www.youtube.com/shorts/PqNfL3k5MvM'),
    ]),
    render_section(f"Hist&ograve;ria del Dret i {it('de l\'Estat')}", 3, [
        vc('D77p-A8ykBc', "L'Europa medieval i el ius commune", 'V&iacute;deo &middot; Dret Medieval'),
        vc('68ZOvJVRB9Y', 'Dels Pactes al Poder: Maquiavel, Bodin i l\'Humanisme',
           'V&iacute;deo &middot; Absolutisme'),
        vc('jJRllZ461vQ', "La Il&middot;lustraci&oacute; i el Naixement del Dret Modern",
           'V&iacute;deo &middot; Dret Modern'),
    ]),
]

historia = build_page(
    'historia-dret.html',
    'Fonaments i Historia del Dret | Dret Visual',
    '[{"label":"Home","url":"index.html"},{"label":"Dret","url":"#"},{"label":"Fonaments i Historia"}]',
    'historia-dret.html',
    [('Home', 'index.html'), ('Dret', '#'), ('Fonaments i Hist&ograve;ria', None)],
    'Assignatura &middot; Fonaments del Dret',
    'Fonaments <span class="em" style="color:var(--b-fonaments)">&amp; Hist&ograve;ria</span>',
    "Filosofia del Dret, evoluci&oacute; de l'Estat modern, dret medieval i la interpretaci&oacute; jur&iacute;dica. Compr&egrave;n d'on ve i per qu&egrave; existeix el Dret.",
    [('6', 'V&iacute;deos'), ('2', 'Seccions'), ('Fil.', 'Filosofia'), ('2026', 'Actualitzat')],
    'var(--b-fonaments)',
    historia_secs,
)
with open(os.path.join(BASE, 'historia-dret.html'), 'w', encoding='utf-8') as f:
    f.write(historia)
print('OK historia-dret.html')

print('\nAll 4 video pages generated successfully.')
