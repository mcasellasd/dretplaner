/**
 * Global Navigation Helper
 * 
 * This script loads and initializes the global navbar and breadcrumbs
 * on pages. Include this script in your HTML pages.
 * 
 * Usage:
 * <script src="navbar-helper.js"></script>
 * 
 * Then call in your HTML body (after navbar placeholder):
 * <div id="navbar-container"></div>
 * 
 * For breadcrumbs, add meta tag in head:
 * <meta name="breadcrumbs" content='[{"label":"Home","url":"index.html"},{"label":"Current Page"}]'>
 */

class GlobalNavigation {
  constructor() {
    this.navbarLoaded = false;
    this.breadcrumbsLoaded = false;
  }

  /**
   * Load navbar component from _navbar.html
   */
  async loadNavbar() {
    if (this.navbarLoaded) return;

    const container = document.getElementById('navbar-container');
    if (!container) {
      console.warn('Navbar container (#navbar-container) not found');
      return;
    }

    try {
      const response = await fetch('_navbar.html');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      
      const html = await response.text();
      container.innerHTML = html;
      
      // Re-execute scripts from loaded HTML
      container.querySelectorAll('script').forEach(script => {
        const newScript = document.createElement('script');
        newScript.textContent = script.textContent;
        document.body.appendChild(newScript);
      });
      
      this.navbarLoaded = true;
    } catch (error) {
      console.error('Failed to load navbar:', error);
    }
  }

  /**
   * Load breadcrumb component from _breadcrumb.html
   */
  async loadBreadcrumbs() {
    if (this.breadcrumbsLoaded) return;

    const container = document.getElementById('breadcrumb-container');
    if (!container) {
      console.warn('Breadcrumb container (#breadcrumb-container) not found');
      return;
    }

    try {
      const response = await fetch('_breadcrumb.html');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      
      const html = await response.text();
      container.innerHTML = html;
      
      // Re-execute scripts from loaded HTML
      container.querySelectorAll('script').forEach(script => {
        const newScript = document.createElement('script');
        newScript.textContent = script.textContent;
        document.body.appendChild(newScript);
      });
      
      this.breadcrumbsLoaded = true;
    } catch (error) {
      console.error('Failed to load breadcrumbs:', error);
    }
  }

  /**
   * Load both navbar and breadcrumbs
   */
  async loadAll() {
    await Promise.all([
      this.loadNavbar(),
      this.loadBreadcrumbs()
    ]);
  }

  /**
   * Utility: Set breadcrumbs programmatically
   */
  setBreadcrumbs(crumbs) {
    const metaTag = document.querySelector('meta[name="breadcrumbs"]');
    if (metaTag) {
      metaTag.setAttribute('content', JSON.stringify(crumbs));
    } else {
      const newMeta = document.createElement('meta');
      newMeta.setAttribute('name', 'breadcrumbs');
      newMeta.setAttribute('content', JSON.stringify(crumbs));
      document.head.appendChild(newMeta);
    }
  }
}

// Create global instance
const globalNav = new GlobalNavigation();

// Auto-load on page load if containers exist
document.addEventListener('DOMContentLoaded', () => {
  const hasNavContainer = document.getElementById('navbar-container');
  const hasBreadContainer = document.getElementById('breadcrumb-container');
  
  if (hasNavContainer || hasBreadContainer) {
    globalNav.loadAll();
  }
});
