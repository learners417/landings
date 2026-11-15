/* ═══════════════════════════════════════════════════════════════
   PAISAJE · lo que se mueve en las páginas de Tu Clínica Digital.
   Corre después de base.js (píxel, links, testimonios, visor).
   ═══════════════════════════════════════════════════════════════ */
(function () {
  var C = window.TCD || {}, d = document, M = C.media || '';
  var quieto = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rama = (window.__tcdCarga || {}).rama || 'main';
  var local = location.protocol === 'file:';

  /* las imágenes del repo (las tapas, la obra): desde jsDelivr, de la rama que se está mirando */
  d.querySelectorAll('img[data-repo]').forEach(function (im) {
    var p = im.getAttribute('data-repo');
    im.src = local ? '../' + p : 'https://cdn.jsdelivr.net/gh/learners417/landings@' + rama + '/' + p;
  });
  /* las fotos de la carpeta de GHL: en webp y al tamaño justo */
  d.querySelectorAll('img[data-media]').forEach(function (im) {
    var u = M + im.getAttribute('data-media'), w = +(im.getAttribute('data-ancho') || 800);
    if (window.TCD_IMG) window.TCD_IMG(im, u, w); else im.src = u;
  });

  /* los rieles con puntos: los puntos dicen dónde estás y llevan a cada tarjeta */
  d.querySelectorAll('[data-puntos]').forEach(function (puntos) {
    var riel = d.getElementById(puntos.getAttribute('data-puntos'));
    if (!riel) return;
    var items = [].slice.call(riel.children), bs = [].slice.call(puntos.querySelectorAll('button'));
    function marcar(i) { bs.forEach(function (b, j) { b.setAttribute('aria-current', j === i ? 'true' : 'false'); }); }
    marcar(0);
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) marcar(items.indexOf(e.target)); });
      }, { root: riel, threshold: 0.6 });
      items.forEach(function (it) { io.observe(it); });
    }
    bs.forEach(function (b, i) {
      b.addEventListener('click', function () {
        var it = items[i];
        riel.scrollTo({ left: it.offsetLeft - (riel.clientWidth - it.clientWidth) / 2, behavior: quieto ? 'auto' : 'smooth' });
      });
    });
  });

  /* el selector de formas: una forma a la vez */
  d.querySelectorAll('.selector').forEach(function (sel) {
    var bs = [].slice.call(sel.querySelectorAll('[role=tab]'));
    function abrir(b, foco) {
      bs.forEach(function (x) {
        var on = x === b, panel = d.getElementById(x.getAttribute('aria-controls'));
        x.setAttribute('aria-selected', on ? 'true' : 'false'); x.tabIndex = on ? 0 : -1;
        if (panel) panel.hidden = !on;
      });
      if (foco) b.focus();
    }
    bs.forEach(function (b, i) {
      b.addEventListener('click', function () {
        if (b.getAttribute('aria-selected') === 'true') return;
        abrir(b);
        if (window.pxc) window.pxc('Forma', { forma: b.getAttribute('data-forma') || b.textContent.trim() });
      });
      b.addEventListener('keydown', function (e) {
        var n = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (n) { e.preventDefault(); abrir(bs[(i + n + bs.length) % bs.length], true); }
      });
    });
  });

  /* los videos del canal: se abren en el visor, sin salir de la página */
  var lb = d.querySelector('.lb');
  d.querySelectorAll('[data-video]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!lb) return;
      var id = b.getAttribute('data-video'), caja = lb.querySelector('.caja');
      caja.classList.remove('img'); caja.classList.add('h');
      caja.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&playsinline=1" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="Video del canal de Tu Clínica Digital"></iframe>';
      lb.classList.add('on'); d.body.style.overflow = 'hidden';
      if (window.pxc) window.pxc('VideoCanal', { video: id });
    });
  });

  /* la barra de abajo se esconde donde ya hay un botón a la vista: el cierre y el pie */
  var barra = d.querySelector('.barra'), tapan = d.querySelectorAll('.cierre,.pie');
  if (barra && tapan.length && 'IntersectionObserver' in window) {
    var vistos = new Set();
    var ob = new IntersectionObserver(function (es) {
      es.forEach(function (e) { e.isIntersecting ? vistos.add(e.target) : vistos.delete(e.target); });
      barra.classList.toggle('fuera', vistos.size > 0);
    });
    tapan.forEach(function (t) { ob.observe(t); });
  }

  /* la portada: la foto queda quieta si la persona pidió menos movimiento */
  if (quieto) d.documentElement.classList.add('quieto');
})();
