/**
 * Ex-tense Navigation Controller
 * Desktop: Click-based dropdowns with auto-positioning and keyboard support.
 * Mobile:  Hamburger → slide-out panel with accordion sub-menus.
 * Also includes scroll-entrance animations.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {

    /* ═══════════════════════════════════════════
       DESKTOP NAV  — click-based dropdowns
       ═══════════════════════════════════════════ */
    var navItems = document.querySelectorAll('header nav > ul > li');

    navItems.forEach(function (li) {
      var link = li.querySelector(':scope > a');
      var dropdown = li.querySelector('.dropdown-content');

      if (!dropdown || !link) return;

      link.setAttribute('data-dropdown', '');
      link.textContent = link.textContent.replace(/\s*▾\s*$/, '');

      link.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var isOpen = li.classList.contains('open');
        closeAll();
        if (!isOpen) {
          li.classList.add('open');
          positionDropdown(li, dropdown);
        }
      });
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('header nav')) closeAll();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        closeAll();
        closeMobileNav();
      }
    });

    function closeAll() {
      document.querySelectorAll('header nav ul li.open').forEach(function (li) {
        li.classList.remove('open');
      });
      document.querySelectorAll('.dropdown-content.dropdown-right').forEach(function (dd) {
        dd.classList.remove('dropdown-right');
      });
    }

    function positionDropdown(li, dropdown) {
      dropdown.classList.remove('dropdown-right');
      var rect = dropdown.getBoundingClientRect();
      if (rect.right > window.innerWidth - 10) {
        dropdown.classList.add('dropdown-right');
      }
    }

    /* ═══════════════════════════════════════════
       MOBILE NAV  — hamburger + slide-out panel
       ═══════════════════════════════════════════ */
    var hamburger = document.querySelector('.hamburger');
    var mobileNav = document.querySelector('.mobile-nav');
    var overlay = document.querySelector('.nav-overlay');
    var closeBtn = document.querySelector('.mobile-nav-close');

    if (hamburger && mobileNav) {
      hamburger.addEventListener('click', function () {
        mobileNav.classList.add('active');
        if (overlay) overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
      });

      if (closeBtn) {
        closeBtn.addEventListener('click', closeMobileNav);
      }

      if (overlay) {
        overlay.addEventListener('click', closeMobileNav);
      }

      // Accordion sub-menus
      mobileNav.querySelectorAll('.mob-trigger').forEach(function (trigger) {
        trigger.addEventListener('click', function (e) {
          e.preventDefault();
          var li = trigger.closest('li');
          var isOpen = li.classList.contains('mob-open');
          // Close all others
          mobileNav.querySelectorAll('li.mob-open').forEach(function (el) {
            el.classList.remove('mob-open');
          });
          if (!isOpen) li.classList.add('mob-open');
        });
      });

      // Close mobile nav when a link is tapped
      mobileNav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          closeMobileNav();
        });
      });
    }

    function closeMobileNav() {
      if (mobileNav) mobileNav.classList.remove('active');
      if (overlay) overlay.classList.remove('active');
      document.body.style.overflow = '';
    }

    /* ═══════════════════════════════════════════
       SCROLL ENTRANCE ANIMATIONS
       ═══════════════════════════════════════════ */
    var animElements = document.querySelectorAll('.card, .flow-step, .stat-item, .tool-card, .accordion-item, .event-card, .circle-item, .ops-stack-item');

    if ('IntersectionObserver' in window && animElements.length) {
      animElements.forEach(function (el) {
        el.classList.add('animate-on-scroll');
      });

      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

      animElements.forEach(function (el) { observer.observe(el); });
    }

  });
})();
