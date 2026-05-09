/**
 * sidebar-toggle.js — Lab 4: Collapsible sidebar TOC
 *
 * Adds toggle behavior for the sidebar TOC on mobile.
 * Works with the toc-override.xsl and brand.css sidebar styles.
 *
 * Uncomment the code below after completing Lab 4.
 */

/*
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    var toggleBtn = document.querySelector('.sidebar-toc__toggle');
    var tocBody = document.querySelector('.sidebar-toc__body');

    if (!toggleBtn || !tocBody) return;

    toggleBtn.addEventListener('click', function () {
      var isCollapsed = tocBody.classList.toggle('collapsed');
      toggleBtn.setAttribute('aria-expanded', !isCollapsed);
      toggleBtn.textContent = isCollapsed ? '☰ Show Contents' : '☰ Contents';
    });

    // Auto-collapse on mobile
    if (window.innerWidth <= 768) {
      tocBody.classList.add('collapsed');
      toggleBtn.setAttribute('aria-expanded', 'false');
      toggleBtn.textContent = '☰ Show Contents';
    }
  });
})();
*/
