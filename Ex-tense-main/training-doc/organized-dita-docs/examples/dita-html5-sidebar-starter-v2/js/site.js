/* site.js — Copy code + highlight current TOC page */

(function () {
  function onCopyClick(btn) {
    var container = btn.closest('.codeblock');
    if (!container) return;
    var pre = container.querySelector('pre');
    if (!pre) return;
    var text = pre.innerText || '';
    navigator.clipboard.writeText(text).then(function () {
      var prev = btn.innerText;
      btn.innerText = 'Copied';
      setTimeout(function () { btn.innerText = prev; }, 900);
    }).catch(function () {});
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.copy-btn');
    if (btn) onCopyClick(btn);
  });

  function highlightToc() {
    var here = (window.location.pathname.split('/').pop() || '').split('?')[0];
    var nav = document.querySelector('nav');
    if (!nav) return;

    var links = nav.querySelectorAll('a[href]');
    links.forEach(function (a) {
      var href = a.getAttribute('href') || '';
      var file = href.split('#')[0].split('/').pop();
      if (file && file === here) a.classList.add('current-page');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', highlightToc);
  } else {
    highlightToc();
  }
})();
