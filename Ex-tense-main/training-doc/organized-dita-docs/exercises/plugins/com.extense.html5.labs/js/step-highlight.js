/**
 * step-highlight.js — Lab 2: Step anchor highlighting
 *
 * When a user navigates to a URL with #step-N in the hash,
 * this script scrolls to that step and highlights it.
 *
 * Usage: Include this JS file in your HTML5 output.
 * It works with the step anchor XSLT template from Lab 2.
 *
 * Uncomment the code below after completing Lab 2.
 */

/*
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    var hash = window.location.hash;

    // Check if hash points to a step anchor
    if (hash && hash.startsWith('#step-')) {
      var el = document.querySelector(hash);
      if (el) {
        // Add highlight class
        el.classList.add('highlighted');

        // Smooth scroll to the element
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Remove highlight after 5 seconds
        setTimeout(function () {
          el.classList.remove('highlighted');
        }, 5000);
      }
    }

    // Also handle clicks on step links within the page
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="#step-"]');
      if (!link) return;

      var targetId = link.getAttribute('href');
      var target = document.querySelector(targetId);
      if (target) {
        // Remove any existing highlights
        document.querySelectorAll('.task-step.highlighted').forEach(function (el) {
          el.classList.remove('highlighted');
        });

        // Add highlight to target
        target.classList.add('highlighted');

        // Auto-remove after 5 seconds
        setTimeout(function () {
          target.classList.remove('highlighted');
        }, 5000);
      }
    });
  });
})();
*/
