/* PAISAJE VIVO · lo que se mueve en las páginas de la Edición (16 nov 2026) */
(function () {
  var d = document, quieto = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  d.documentElement.classList.add('vv');
  /* la secuencia y las listas entran cuando llegan a la vista */
  var items = d.querySelectorAll('.secuencia li,.lideres li,.mapa li');
  if (!quieto && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return; io.unobserve(e.target);
        var el = e.target, i = [].indexOf.call(el.parentNode.children, el);
        setTimeout(function () { el.classList.add('dentro'); }, Math.min(i, 6) * 90);
      });
    }, { threshold: 0.15 });
    items.forEach(function (x) { io.observe(x); });
  } else items.forEach(function (x) { x.classList.add('dentro'); });

  /* la barra de lectura, en los capítulos */
  var pag = (d.body.getAttribute('data-pagina') || '');
  var top = d.querySelector('.top');
  if (/^capitulo-/.test(pag) && top) {
    var b = d.createElement('i'); b.className = 'progreso'; top.appendChild(b);
    var mover = function () { var h = d.documentElement.scrollHeight - innerHeight; b.style.width = (h > 0 ? Math.min(100, scrollY / h * 100) : 0) + '%'; };
    addEventListener('scroll', mover, { passive: true }); mover();
  }


  /* el ejemplo de la herramienta: el resultado se cuenta desde cero cuando llega a la vista */
  d.querySelectorAll('.cap .oferta .lideres li:last-child .d b').forEach(function (b) {
    var m = b.textContent.match(/^([^\d]*)([\d.]+)(.*)$/); if (!m) return;
    var fin = parseInt(m[2].replace(/\./g, ''), 10); if (!fin) return;
    b.closest('.oferta').classList.add('cuenta-viva');
    if (quieto || !('IntersectionObserver' in window)) return;
    var fmt = function (n) { return m[1] + String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.') + m[3]; };
    b.textContent = fmt(0);
    var o = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return; o.disconnect();
      var t0 = null, dur = 1100;
      setTimeout(function () {
        requestAnimationFrame(function paso(t) {
          if (t0 === null) t0 = t; var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
          b.textContent = fmt(Math.round(fin * e)); if (k < 1) requestAnimationFrame(paso);
        });
      }, 500);
    }, { threshold: 0.6 });
    o.observe(b);
  });

  /* la mesa: las sillas se ocupan una por una y al final se marca la tuya */
  d.querySelectorAll('.mesa').forEach(function (m) {
    m.classList.add('vv-mesa');
    var sillas = m.querySelectorAll('.m-silla');
    sillas.forEach(function (s, i) { s.style.transitionDelay = (i * 0.12) + 's'; });
    if (quieto || !('IntersectionObserver' in window)) { m.classList.add('dentro'); return; }
    var o = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { m.classList.add('dentro'); o.disconnect(); } }, { threshold: 0.4 });
    o.observe(m);
  });
})();
