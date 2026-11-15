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

  /* la portada en movimiento: las fotos pasan despacio; si hay video (config.js · heroVideo), entra el video */
  var esc = d.querySelector('[data-escena]');
  if (esc) {
    var cs = [].slice.call(esc.querySelectorAll('img')), i = 0, reloj = 0;
    if (!quieto && cs.length > 1) {
      setTimeout(function () { cs[0].classList.add('zoom'); }, 60);
      reloj = setInterval(function () {
        cs[i].classList.remove('on', 'zoom');
        i = (i + 1) % cs.length;
        cs[i].classList.add('on', 'zoom');
      }, 7000);
    }
    var red = navigator.connection || {};
    if (C.heroVideo && !quieto && !red.saveData && !/2g/.test(red.effectiveType || '')) {
      var v = d.createElement('video');
      v.muted = true; v.loop = true; v.playsInline = true; v.autoplay = true; v.preload = 'auto';
      v.setAttribute('muted', ''); v.setAttribute('playsinline', ''); v.setAttribute('aria-hidden', 'true');
      if (C.heroPoster) v.poster = C.heroPoster;
      v.addEventListener('playing', function () {
        clearInterval(reloj);
        v.classList.add('on');
        setTimeout(function () { cs.forEach(function (c) { c.classList.remove('on', 'zoom'); }); }, 1300);
      }, { once: true });
      v.src = C.heroVideo;
      esc.appendChild(v);
      var pr = v.play(); if (pr && pr.catch) pr.catch(function () {});
    }
  }
})();

/* ═══════════════════════════════════════════════════════════════
   PAISAJE VIVO · la película, el recorrido con la app, el contraste
   y las cifras. Todo responde al dedo; con movimiento reducido, quieto.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  var d = document, quieto = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var verIO = 'IntersectionObserver' in window;
  function ev(n, x) { if (window.pxc) window.pxc(n, x || {}); }

  /* la agenda llena: un cuadradito por turno, de noviembre a mayo */
  var k = 0;
  d.querySelectorAll('[data-puntos-agenda]').forEach(function (s) {
    var n = +s.getAttribute('data-puntos-agenda'), h = '';
    for (var j = 0; j < n; j++) h += '<i style="--k:' + (k++) + '"></i>';
    s.innerHTML = h;
  });

  /* la película: pasa sola mientras se ve, se toca a los costados, se pausa */
  d.querySelectorAll('[data-peli]').forEach(function (peli) {
    var escs = [].slice.call(peli.querySelectorAll('.esc')), barras = [].slice.call(peli.querySelectorAll('.peli-barras i'));
    var DUR = [5200, 4600, 5200, 4400, 4400, 4400, 6000];
    var i = 0, reloj = 0, desde = 0, resta = 0, pausa = quieto, visible = false, termino = false;
    function dur(j) { return DUR[j] || 4600; }
    function pintar() {
      escs.forEach(function (e, j) { e.classList.toggle('on', j === i); });
      barras.forEach(function (b, j) {
        b.classList.toggle('lleno', j < i); b.classList.remove('va');
        b.style.setProperty('--d', dur(j) + 'ms');
      });
      void peli.offsetWidth;
      if (barras[i]) barras[i].classList.add('va');
      peli.setAttribute('data-tono', escs[i].getAttribute('data-tono') || 'oscuro');
      peli.classList.toggle('al-final', i === escs.length - 1);
    }
    function parar() { clearTimeout(reloj); reloj = 0; if (desde) { resta -= performance.now() - desde; desde = 0; } }
    function correr() {
      parar();
      if (pausa || !visible || termino) { peli.classList.toggle('pausa', true); return; }
      peli.classList.remove('pausa');
      desde = performance.now();
      reloj = setTimeout(function () { desde = 0; siguiente(true); }, Math.max(resta, 0));
    }
    function ir(j) {
      i = Math.max(0, Math.min(escs.length - 1, j)); resta = dur(i); termino = false;
      pintar(); correr();
    }
    function siguiente(solo) {
      if (i < escs.length - 1) return ir(i + 1);
      if (solo) { termino = true; parar(); barras[i].classList.add('lleno'); peli.classList.add('pausa'); ev('Pelicula', { fin: true }); }
    }
    peli.querySelector('.peli-sig').addEventListener('click', function () { siguiente(false); });
    peli.querySelector('.peli-ant').addEventListener('click', function () { ir(i - 1); });
    peli.querySelector('.peli-pausa').addEventListener('click', function () {
      if (termino) { ir(0); pausa = false; correr(); return; }
      pausa = !pausa;
      this.setAttribute('aria-label', pausa ? 'Seguir la historia' : 'Pausar la historia');
      correr();
    });
    var otra = peli.querySelector('.otra-vez');
    if (otra) otra.addEventListener('click', function (e) { e.stopPropagation(); pausa = false; ir(0); ev('Pelicula', { otra_vez: true }); });
    peli.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); siguiente(false); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); ir(i - 1); }
    });
    /* dejar el dedo apretado pausa, como en las historias */
    var apretado = 0;
    peli.addEventListener('pointerdown', function (e) {
      if (e.target.closest('.peli-pausa,.otra-vez')) return;
      apretado = setTimeout(function () { apretado = -1; parar(); peli.classList.add('pausa'); }, 260);
    });
    peli.addEventListener('pointerup', function (e) {
      if (apretado === -1) { e.preventDefault(); apretado = 0; correr(); peli.querySelectorAll('.peli-ant,.peli-sig').forEach(function (b) { b.dataset.trago = '1'; }); return; }
      clearTimeout(apretado); apretado = 0;
    });
    peli.querySelectorAll('.peli-ant,.peli-sig').forEach(function (b) {
      b.addEventListener('click', function (e) { if (b.dataset.trago) { delete b.dataset.trago; e.stopImmediatePropagation(); } }, true);
    });
    if (verIO) new IntersectionObserver(function (es) { visible = es[0].isIntersecting; correr(); }, { threshold: 0.45 }).observe(peli);
    else visible = true;
    d.addEventListener('visibilitychange', function () { if (d.hidden) parar(); else correr(); });
    resta = dur(0); pintar(); correr();
  });

  /* el recorrido: cada paisaje muestra su día en la app */
  d.querySelectorAll('[data-reco]').forEach(function (r) {
    var tabs = [].slice.call(r.querySelectorAll('[role=tab]')), imgs = [].slice.call(r.querySelectorAll('.tel .pant img'));
    function abrir(k, foco) {
      tabs.forEach(function (t, j) {
        var on = j === k; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1;
        var p = d.getElementById(t.getAttribute('aria-controls')); if (p) p.hidden = !on;
      });
      imgs.forEach(function (im, j) { im.classList.toggle('on', j === k); });
      r.setAttribute('data-paisaje', tabs[k].parentNode.className);
      if (foco) tabs[k].focus();
    }
    tabs.forEach(function (t, j) {
      t.addEventListener('click', function () {
        if (t.getAttribute('aria-selected') === 'true') return;
        abrir(j); ev('Paisaje', { paisaje: t.parentNode.className });
      });
      t.addEventListener('keydown', function (e) {
        var n = (e.key === 'ArrowRight' || e.key === 'ArrowDown') ? 1 : (e.key === 'ArrowLeft' || e.key === 'ArrowUp') ? -1 : 0;
        if (n) { e.preventDefault(); abrir((j + n + tabs.length) % tabs.length, true); }
      });
    });
  });

  /* el contraste se tacha y se tilda cuando llega a la vista; las cifras cuentan una vez */
  var revelar = d.querySelectorAll('[data-revela]'), contar = d.querySelectorAll('[data-contar]');
  if (!verIO || quieto) { revelar.forEach(function (x) { x.classList.add('visto'); }); return; }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      io.unobserve(e.target);
      var x = e.target;
      if (x.hasAttribute('data-revela')) { x.classList.add('visto'); return; }
      var hasta = +x.getAttribute('data-contar'), pre = x.getAttribute('data-pre') || '', t0 = performance.now();
      (function paso(t) {
        var p = Math.min(1, (t - t0) / 1100), v = Math.round(hasta * (1 - Math.pow(1 - p, 3)));
        x.textContent = pre + v;
        if (p < 1) requestAnimationFrame(paso);
      })(t0);
    });
  }, { threshold: 0.4 });
  revelar.forEach(function (x) { io.observe(x); });
  contar.forEach(function (x) { io.observe(x); });
})();

/* ═══ PAISAJE VIVO · la estantería de /libros: un libro a la vez ═══ */
(function () {
  var d = document, quieto = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var est = d.querySelector('[data-estanteria]');
  if (!est) return;
  var tabs = [].slice.call(est.querySelectorAll('[role=tab]'));
  function elegir(k, bajar, foco) {
    var i = -1;
    tabs.forEach(function (t, j) {
      var on = t.getAttribute('aria-controls') === k; if (on) i = j;
      t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1;
      var p = d.getElementById(t.getAttribute('aria-controls')); if (p) p.hidden = !on;
    });
    if (i < 0) return;
    var sel = est.querySelector('.tapas-sel'), t = tabs[i];
    if (sel) sel.scrollTo({ left: t.offsetLeft - (sel.clientWidth - t.clientWidth) / 2, behavior: quieto ? 'auto' : 'smooth' });
    if (foco) t.focus();
    if (bajar) { var y = est.getBoundingClientRect().top + scrollY - 90; window.scrollTo({ top: y, behavior: quieto ? 'auto' : 'smooth' }); }
    if (window.pxc) window.pxc('Libro', { libro: k });
  }
  window.TCD_LIBRO = elegir;
  tabs.forEach(function (t, j) {
    t.addEventListener('click', function () { if (t.getAttribute('aria-selected') !== 'true') elegir(t.getAttribute('aria-controls')); });
    t.addEventListener('keydown', function (e) {
      var n = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (n) { e.preventDefault(); elegir(tabs[(j + n + tabs.length) % tabs.length].getAttribute('aria-controls'), false, true); }
    });
  });
  /* los libros de la portada llevan a su ficha */
  d.querySelectorAll('a[data-libro]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); elegir(a.getAttribute('data-libro'), true); });
  });
})();
