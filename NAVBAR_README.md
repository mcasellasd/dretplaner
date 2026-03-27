# 🧭 Sistema de Navegació Global - Submenus Harmonitzats

## 📋 Descripció General

Sistema de navegació cohesiu amb submenus desplegables (dropdowns) i colors harmonitzats a través de tot el projecte. La navegació es carrega dinàmicament mitjançant JavaScript i es pot afegir a qualsevol pàgina.

## 📁 Fitxers del Sistema

### 1. **navbar.css**
Estils globals de la navegació amb:
- Variables CSS per a colors harmonitzats per secció
- Estils per a navbar sticky, submenus, breadcrumbs
- Animacions suaus i transicions
- Responsive design (mobile-first)

**Secció de Colors (Variables CSS):**
- `--color-home: #3b82f6` (Blau - Home)
- `--color-dret: #8b5cf6` (Morat - Dret)
- `--color-fiscalitat: #3b82f6` (Blau - Fiscalitat)
- `--color-altres: #6b7280` (Gris - Altres)

### 2. **_navbar.html**
Component HTML que conté:
- Logo/Home link
- Menu principal amb 4 seccions: HOME, DRET, FISCALITAT, ALTRES
- Submenus per a cada secció amb icones i descripcions
- Script JavaScript per a gestió d'interaccions (toggle, active states)
- Auto-detecció de página actual

**Estructura del Menú:**
```
HOME → Inici (index.html)

DRET ↓
  ├─ História del Dret
  ├─ Dret Constitucional
  ├─ Dret Civil
  ├─ Dret Mercantil
  ├─ Dret Processal
  └─ Dret Penal

FISCALITAT ↓
  ├─ Fiscalitat Directa
  ├─ Calculador IRPF
  ├─ IRPF Aprofundit
  ├─ IS Aprofundit
  ├─ IP Aprofundit
  └─ ISD Aprofundit

ALTRES ↓
  ├─ Visualitzacions
  └─ Prova
```

### 3. **_breadcrumb.html**
Component Breadcrumb que:
- Es carrega dinàmicament basant-se en meta tag `breadcrumbs`
- Mostra ruta de navegació actual
- Enllaços actius a pàgines anteriors

**Format Meta Tag:**
```html
<meta name="breadcrumbs" content='[{"label":"Home","url":"index.html"},{"label":"Fiscalitat","url":"#"},{"label":"Fiscalitat Directa"}]'>
```

### 4. **navbar-helper.js**
Classe JavaScript que:
- Carrega components HTML dinàmicament (fetch)
- Inicialitza breadcrumbs
- Gestiona el cicle de vida dels components

## 🚀 Com Integrar la Navegació en una Pàgina

### Pas 1: Afegir la línia CSS al `<head>`
```html
<link rel="stylesheet" href="navbar.css">
```

### Pas 2: Afegir Meta Tag per a Breadcrumbs (opcional)
```html
<meta name="breadcrumbs" content='[{"label":"Home","url":"index.html"},{"label":"Secció"},{"label":"Pàgina Actual"}]'>
```

### Pas 3: Afegir els Contenidors al `<body>`
```html
<body>
  <!-- Global Navbar Container -->
  <div id="navbar-container"></div>

  <!-- Breadcrumb Container -->
  <div id="breadcrumb-container" class="max-w-6xl mx-auto px-4 pt-24 pb-4"></div>

  <!-- Contingut principal de la pàgina -->
  <div class="max-w-6xl mx-auto px-4 pb-12">
    <!-- ...rest of content... -->
  </div>

  <!-- Script de navegació global al final -->
  <script src="navbar-helper.js"></script>
</body>
```

### Pas 4: Ajustar Padding/Margin del Contingut
Afegir `pt-24` (padding-top) o similar al contenidor principal jà que la navbar és sticky i ocupa espai.

## 🎨 Sistema de Colors Harmonitzats

Cada secció té un color primari que es mostra a:
- Pestanya del menú (hover/active)
- Text del submenu (hover)
- Icones del submenu
- Breadcrumb (links)

### Combinacions de Gradients (en HTML específic):
- **IRPF**: Azul → Violeta (`from-blue-600 to-purple-600`)
- **IS**: Azul → Indi (`from-blue-600 to-indigo-600`)
- **IP**: Esmeralda → Teal (`from-emerald-600 to-teal-600`)
- **ISD**: Rose → Pink (`from-rose-600 to-pink-600`)

## 📱 Responsive Design

### Desktop:
- Navbar sticky al top
- Submenus desplegables al hover
- Breadcrumbs en fila horitzontal

### Mobile (< 768px):
- Navbar full-width
- Menú en flexbox vertical
- Submenus expandits (no hover)
- Breadcrumbs compactats

## 🔧 Personalització

### Afegir Nou Enllaç al Submenu
Editar `_navbar.html` i afegir:
```html
<li class="navbar-submenu-item">
  <a href="nova-pagina.html" class="navbar-submenu-link">
    <svg class="navbar-submenu-icon"><!-- SVG icon --></svg>
    <div>
      <div class="navbar-submenu-label">Nom del Enllaç</div>
      <div class="navbar-submenu-desc">Descripció breu</div>
    </div>
  </a>
</li>
```

### Canviar Colors de Secció
Editar `navbar.css` variables CSS:
```css
--color-dret: #7c3aed;  /* Nou color morat */
--color-dret-hover: #6d28d9;  /* Hover state */
```

### Afegir Nova Secció
1. Afegir nou `navbar-item` a `_navbar.html`
2. Afegir nou color a `navbar.css`
3. Afegir classe CSS específica para la nova secció
4. Actualitzar `pageToSection` mapping a `_navbar.html` script

## 🧪 Testing de la Navegació

### 1. Validar la Càrrega
Obrir DevTools (F12) → Console i verificar:
```javascript
console.log(globalNav.navbarLoaded); // true
console.log(globalNav.breadcrumbsLoaded); // true
```

### 2. Probar Submenus
- Click en "DRET" → ha de desplegarse
- Click fora → ha de tancar-se
- Click a un link del submenu → navegar a pàgina correcta

### 3. Probar Breadcrumbs
- Comprovar que es mostren breadcrumbs correctes
- Click en breadcrumb → navegar a pàgina
- Última breadcrumb sense link (pàgina actual)

### 4. Responsive
- Redimensionar finestra < 768px
- Comprovar que:
  - Navbar s'adapta a mobile
  - Menú es mostra verticalment
  - Submenus expandits per defecte
  - Breadcrumbs compactats

## 📊 Estado Actual d'Implementació

**✅ Completat:**
- `navbar.css` - Estils globals creats
- `_navbar.html` - Component HTML amb totes les seccions
- `_breadcrumb.html` - Component breadcrumbs
- `navbar-helper.js` - Script de càrrega dinàmica
- `fiscalitat-directa.html` - Integrada amb navegació

**⏳ Pendent:**
- Integrar navegació a altres pàgines actuals
- Links de breadcrumbs dynamiques per a cada pàgina
- Testing complet de totes les funcionalitats
- Pràctiques de Dark Mode (si s'afegeix en el futur)

## 🐛 Debugging

### La navbar no apareix
1. Comprovar que `id="navbar-container"` existeix al HTML
2. Comprovar que `navbar-helper.js` es carrega correctament
3. Obrir DevTools Network → veure si `_navbar.html` es descarrega
4. Console → veure errors de fetch

### Breadcrumbs no es mostren
1. Verificar format del meta tag `breadcrumbs`
2. Comprovar que `id="breadcrumb-container"` existeix
3. Comprovar JSON vàlid a la meta tag

### Colors no apliquen correctament
1. Comprovar que `navbar.css` es carrega
2. Verificar que les classes CSS es toquen a elements
3. Comprovar que no hi ha conflictes amb altres CSS

## 📝 Contribució

Per a afegir/modificar la navegació:
1. Editar `_navbar.html` per a canvis estructurals
2. Editar `navbar.css` per a estils
3. Testejar a diversos navegadors
4. Actualitzar aquesta documentació

--- 

**Última actualització:** Marzo 2026
**Versió:** 1.0 - Submenus Harmonitzats
