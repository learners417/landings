/* ═══════════════════════════════════════════════════════════════
   EDICIÓN LIBRES · lo que hace que la página se lea como un libro:
   la cabecera corriente, el índice y el estante. Corre después de base.js.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  var C = window.TCD || {};
  var pagina = document.body.getAttribute('data-pagina') || '';
  var quieto = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var caps = [].slice.call(document.querySelectorAll('[data-capitulo]'));

  /* ── la cabecera corriente: dice en qué capítulo estás ── */
  var rotulo = document.querySelector('.rotulo');
  if (rotulo && caps.length && 'IntersectionObserver' in window) {
    var visibles = new Set();
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { e.isIntersecting ? visibles.add(e.target) : visibles.delete(e.target); });
      var s = caps.filter(function (c) { return visibles.has(c); })[0];
      if (!s) { rotulo.classList.remove('on'); return; }
      var n = s.querySelector('.cap-n');
      rotulo.innerHTML = '';
      if (n) { var b = document.createElement('b'); b.textContent = n.textContent.trim(); rotulo.appendChild(b); }
      rotulo.appendChild(document.createTextNode(s.getAttribute('data-capitulo')));
      rotulo.classList.add('on');
    }, { rootMargin: '-40% 0px -55% 0px' });
    caps.forEach(function (c) { io.observe(c); });
  }

  /* ── el índice: los capítulos de esta página y las otras páginas ── */
  var OTRAS = [
    ['inicio', 'Inicio', 'quién soy y por dónde empezar'],
    ['camino', 'El camino', '90 días, del lago al bosque'],
    ['libros', 'Los libros', 'Tu nuevo precio'],
    ['capitulo', 'Los primeros capítulos', 'para leer aquí mismo'],
    ['recursos', 'Para empezar', 'seis herramientas'],
    ['agenda', 'Mentoría e instalación', 'tu diagnóstico'],
    ['laCima', 'La Cima', '4 días en Bariloche'],
    ['prensa', 'Prensa', 'para presentarme']
  ];
  var MIA = { inicio: 'inicio', camino: 'camino', libros: 'libros', capitulos: 'capitulo', recursos: 'recursos', 'la-cima': 'laCima', prensa: 'prensa' };
  var botones = document.querySelectorAll('[data-indice]');
  if (botones.length) {
    var ind = document.createElement('div');
    ind.className = 'indice'; ind.setAttribute('role', 'dialog'); ind.setAttribute('aria-modal', 'true'); ind.setAttribute('aria-label', 'Índice');
    var h = '<div class="indice-in"><div class="indice-cab"><span class="marca">Javo Katz</span>' +
      '<button type="button" class="indice-x" aria-label="Cerrar el índice">×</button></div>' +
      '<h2>Índice</h2><p class="ind-sub"></p><ol class="lideres">';
    caps.forEach(function (c, i) {
      if (!c.id) c.id = 'cap-' + (i + 1);
      var n = c.querySelector('.cap-n');
      h += '<li><a href="#' + c.id + '"><span class="n">' + (n ? n.textContent.trim() : i + 1) + '</span><span class="t"></span>' +
        '<span class="pg"></span><span class="d"></span></a></li>';
    });
    h += '</ol><p class="ind-otras">Más de Javo Katz</p><ul class="lideres otras">';
    OTRAS.forEach(function (o) {
      if (!C[o[0]] || MIA[pagina] === o[0]) return;
      h += '<li><a href="' + C[o[0]] + '"><span class="t">' + o[1] + '</span><span class="pg"></span><span class="d">' + o[2] + '</span></a></li>';
    });
    h += '</ul></div>';
    ind.innerHTML = h;
    ind.querySelector('.ind-sub').textContent = document.body.getAttribute('data-libro-titulo') || document.title.split(' · ')[0];
    var ts = ind.querySelectorAll('ol.lideres li');
    caps.forEach(function (c, i) {
      ts[i].querySelector('.t').textContent = c.getAttribute('data-capitulo');
      ts[i].querySelector('.d').textContent = c.getAttribute('data-dato') || '';
    });
    document.body.appendChild(ind);
    var antes = null;
    function abrir(b) {
      antes = b; ind.classList.add('on'); document.documentElement.style.overflow = 'hidden';
      setTimeout(function () { ind.querySelector('.indice-x').focus(); }, 60);
      if (window.pxc) pxc('Indice', { pagina: pagina });
    }
    function cerrar() { ind.classList.remove('on'); document.documentElement.style.overflow = ''; if (antes) antes.focus(); }
    botones.forEach(function (b) { b.addEventListener('click', function () { abrir(b); }); });
    ind.querySelector('.indice-x').addEventListener('click', cerrar);
    ind.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { if (a.getAttribute('href').charAt(0) === '#') cerrar(); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && ind.classList.contains('on')) cerrar(); });
  }

  /* ── el estante: los 8 libros. Al tocar un lomo, el libro sale y su ficha aparece abajo ── */
  document.querySelectorAll('[data-estante]').forEach(function (est) {
    var lomos = [].slice.call(est.querySelectorAll('.lomo'));
    var ficha = est.querySelector('.ficha-libro');
    if (!lomos.length || !ficha) return;
    var q = function (s) { return ficha.querySelector(s); };
    function elegir(b, porUsuario) {
      lomos.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var d = b.dataset;
      function poner() {
        var im = q('img'), E = window.TCD_IMGS || {};
        if (E[d.tapa]) im.src = E[d.tapa];
        im.alt = 'Tapa de ' + d.titulo;
        q('.fl-serie').textContent = d.serie;
        q('.fl-tit').textContent = d.titulo;
        q('.fl-sub').textContent = d.sub;
        q('.fl-frase').textContent = d.frase;
        var a = q('[data-cap-libro]');
        if (a) { a.href = (C.cap || '/capitulo-') + d.libro; a.textContent = d.leer || 'Leer el primer capítulo'; }
        var v = q('[data-ver-libro]'); if (v) v.href = '#' + d.libro;
        ficha.classList.remove('cambia');
      }
      if (porUsuario && !quieto) { ficha.classList.add('cambia'); setTimeout(poner, 170); } else poner();
      if (porUsuario && window.pxc) pxc('Estante', { libro: d.libro, pagina: pagina });
    }
    lomos.forEach(function (b, i) {
      b.addEventListener('click', function () { elegir(b, true); });
      b.addEventListener('keydown', function (e) {
        var k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!k) return;
        e.preventDefault(); var o = lomos[(i + k + lomos.length) % lomos.length]; o.focus(); elegir(o, true);
      });
    });
    window.TCD_ESTANTE = function (libro) { var b = est.querySelector('.lomo[data-libro="' + libro + '"]'); if (b) elegir(b, false); };
    var inicial = est.querySelector('.lomo[data-inicial]') || lomos[0];
    if (quieto || !('IntersectionObserver' in window)) { elegir(inicial, false); return; }
    /* la entrada: los libros se acomodan en el estante, uno por uno, y el primero sale */
    est.classList.add('llega');
    var vio = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return;
      vio.disconnect();
      lomos.forEach(function (b, i) { b.style.transitionDelay = (120 + i * 85) + 'ms'; });
      requestAnimationFrame(function () { requestAnimationFrame(function () { est.classList.remove('llega'); }); });
      setTimeout(function () {
        lomos.forEach(function (b) { b.style.transitionDelay = ''; });
        elegir(inicial, false);
      }, 120 + lomos.length * 85 + 560);
    }, { threshold: .3 });
    vio.observe(est);
  });
})();
