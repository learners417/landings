/* Experiencias Patagónicas · lo que comparten las páginas (película, aparición, pestañas, agenda, píxel). */
(function () {
  var PIXEL = '2031253547512073';
  var d = document, w = window;
  function $$(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function evento(nombre, datos, propio) {
    if (!w.fbq) return;
    if (propio) w.fbq('trackSingleCustom', PIXEL, nombre, datos || {});
    else w.fbq('trackSingle', PIXEL, nombre, datos || {});
  }
  w.EP = { evento: evento };
  var quieto = w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── la película ── */
  $$('[data-pelicula]').forEach(function (peli) {
    var escenas = $$('.escena', peli), final = peli.querySelector('.final');
    var DUR = +(peli.getAttribute('data-duracion') || 5600);
    var barra = d.createElement('div'); barra.className = 'barra';
    var marcas = escenas.map(function (e, i) {
      var b = d.createElement('button'); b.type = 'button';
      b.setAttribute('aria-label', 'Escena ' + (i + 1) + ' de ' + escenas.length);
      var r = d.createElement('i'); b.appendChild(r); barra.appendChild(b);
      b.addEventListener('click', function () { ir(i, true); });
      return r;
    });
    var mandos = d.createElement('div'); mandos.className = 'mandos';
    var boton = d.createElement('button'); boton.type = 'button'; boton.className = 'redondo';
    mandos.appendChild(boton);
    peli.appendChild(barra); peli.appendChild(mandos);
    var PAUSA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
    var SIGUE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg>';
    var OTRA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>';
    var actual = -1, corriendo = !quieto, visible = true, t0 = 0, avance = 0, terminada = false;
    function pintarBoton() {
      if (terminada) { boton.innerHTML = OTRA; boton.setAttribute('aria-label', 'Ver de nuevo'); return; }
      boton.innerHTML = corriendo ? PAUSA : SIGUE;
      boton.setAttribute('aria-label', corriendo ? 'Pausar' : 'Seguir');
    }
    function ir(i, aMano) {
      terminada = false;
      if (final) final.hidden = true;
      escenas.forEach(function (e, k) { e.classList.toggle('activa', k === i); e.setAttribute('aria-hidden', k === i ? 'false' : 'true'); });
      marcas.forEach(function (m, k) { m.style.width = k < i ? '100%' : '0'; });
      actual = i; avance = 0; t0 = performance.now();
      if (aMano && !corriendo) corriendo = true;
      pintarBoton();
    }
    function terminar() {
      terminada = true; corriendo = false;
      marcas.forEach(function (m) { m.style.width = '100%'; });
      if (final) { final.hidden = false; }
      escenas.forEach(function (e) { e.classList.remove('activa'); });
      pintarBoton();
      evento('PeliculaCompleta', { pagina: peli.getAttribute('data-pelicula') }, true);
    }
    function cuadro(ahora) {
      if (corriendo && visible && !d.hidden && !terminada) {
        avance = Math.min(1, (ahora - t0) / DUR);
        if (marcas[actual]) marcas[actual].style.width = (avance * 100) + '%';
        if (avance >= 1) { if (actual < escenas.length - 1) ir(actual + 1); else terminar(); }
      } else { t0 = ahora - avance * DUR; }
      w.requestAnimationFrame(cuadro);
    }
    boton.addEventListener('click', function () {
      if (terminada) { ir(0, true); return; }
      corriendo = !corriendo; pintarBoton();
    });
    peli.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); if (actual < escenas.length - 1) ir(actual + 1, true); else terminar(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); ir(Math.max(0, terminada ? escenas.length - 1 : actual - 1), true); }
    });
    if ('IntersectionObserver' in w) {
      new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }, { threshold: .25 }).observe(peli);
    }
    if (final) final.hidden = true;
    ir(0); pintarBoton();
    w.requestAnimationFrame(cuadro);
  });

  /* ── la barra se marca al bajar; la barra del celular aparece después de la portada ── */
  var nav = d.querySelector('.nav'), movil = d.querySelector('.barra-movil');
  var portada = d.querySelector('[data-barra-desde]'), agenda = d.getElementById('agenda');
  var agendaVisible = false;
  if (agenda && 'IntersectionObserver' in w) {
    new IntersectionObserver(function (en) { agendaVisible = en[0].isIntersecting; mover(); }, { threshold: .05 }).observe(agenda);
  }
  function mover() {
    var y = w.scrollY || d.documentElement.scrollTop;
    if (nav) nav.classList.toggle('borde', y > 12);
    if (movil) {
      var desde = portada ? portada.getBoundingClientRect().bottom + y : 700;
      movil.classList.toggle('ver', y > desde - 200 && !agendaVisible);
    }
  }
  w.addEventListener('scroll', mover, { passive: true }); mover();

  /* ── aparición y tachado ── */
  var rv = $$('.rv, .tachados');
  if (!('IntersectionObserver' in w) || quieto) { rv.forEach(function (e) { e.classList.add('in'); if (e.classList.contains('tachados')) e.classList.add('tachar'); }); }
  else {
    var o = new IntersectionObserver(function (en) {
      en.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        if (e.target.classList.contains('tachados')) setTimeout(function () { e.target.classList.add('tachar'); }, 450);
        o.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    rv.forEach(function (e) { o.observe(e); });
  }

  /* ── pestañas ── */
  $$('[data-pestanas]').forEach(function (grupo) {
    var botones = $$('[role=tab]', grupo);
    function elegir(b) {
      botones.forEach(function (x) {
        var si = x === b; x.setAttribute('aria-selected', si ? 'true' : 'false'); x.tabIndex = si ? 0 : -1;
        var p = d.getElementById(x.getAttribute('aria-controls')); if (p) p.classList.toggle('activo', si);
      });
    }
    botones.forEach(function (b, i) {
      b.addEventListener('click', function () { elegir(b); evento('Pestana', { cual: b.getAttribute('aria-controls') }, true); });
      b.addEventListener('keydown', function (e) {
        var k = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : e.key === 'ArrowLeft' || e.key === 'ArrowUp' ? -1 : 0;
        if (!k) return; e.preventDefault(); var n = botones[(i + k + botones.length) % botones.length]; n.focus(); elegir(n);
      });
    });
  });

  /* ── botones: un evento por botón ── */
  $$('[data-cta]').forEach(function (a) {
    a.addEventListener('click', function () { evento('CTA', { ubicacion: a.getAttribute('data-cta') }, true); }, { once: true });
  });

  /* ── la agenda de GHL ── */
  var caja = d.getElementById('cal');
  if (caja) {
    var id = caja.getAttribute('data-cal') || '', nombre = caja.getAttribute('data-evento') || 'agenda';
    var src = /^[a-z0-9]+(-[a-z0-9]+)*$/.test(id) ? 'https://api.leadconnectorhq.com/widget/bookings/' + id
      : (/^[A-Za-z0-9]{12,}$/.test(id) ? 'https://api.leadconnectorhq.com/widget/booking/' + id : '');
    if (!src) caja.innerHTML = '<p class="aviso">La agenda abre en unos minutos. Volvé a entrar más tarde.</p>';
    else {
      var f = d.createElement('iframe');
      f.src = src; f.id = id + '_ads'; f.title = caja.getAttribute('data-titulo') || 'Agenda'; f.setAttribute('scrolling', 'no');
      caja.appendChild(f);
      var s = d.createElement('script'); s.src = 'https://link.msgsndr.com/js/form_embed.js'; s.async = true; d.body.appendChild(s);
      var avisado = false;
      w.addEventListener('message', function (e) {
        if (typeof e.origin !== 'string' || e.origin.indexOf('leadconnectorhq') < 0) return;
        var x = e.data || {};
        if (x && typeof x === 'object') { var h = x.height || x.iframeHeight || (x.data && x.data.height); if (typeof h === 'number' && h > 300) f.style.minHeight = h + 'px'; }
        var t = (typeof x === 'string') ? x : (x.type || x.event || ''); t = String(t).toLowerCase();
        if (!avisado && (t.indexOf('book') > -1 || t.indexOf('appointment') > -1)) { avisado = true; evento('Schedule', { content_name: nombre }); }
      }, false);
    }
  }

  /* ── el video de Ailu: arranca mudo al verse; con el botón vuelve al inicio con sonido ── */
  $$('[data-vsl]').forEach(function (caja) {
    var v = caja.querySelector('video'), b = caja.querySelector('.sonido'), activo = false;
    if (!v) return;
    if ('IntersectionObserver' in w && !quieto) {
      new IntersectionObserver(function (en) {
        if (activo) return;
        if (en[0].isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause();
      }, { threshold: .4 }).observe(caja);
    }
    if (b) b.addEventListener('click', function () {
      activo = true; caja.classList.add('sonando');
      v.muted = false; v.loop = false; v.controls = true; try { v.currentTime = 0; } catch (e) {}
      var p = v.play(); if (p && p.catch) p.catch(function () {});
      evento('VideoConSonido', { pagina: location.pathname }, true);
    });
    v.addEventListener('ended', function () { evento('VideoCompleto', { pagina: location.pathname }, true); });
  });
  /* ── el video de venta en Wistia: se monta acá, porque el cargador de GHL no corre scripts de tipo módulo ── */
  $$('[data-wistia]').forEach(function (caja) {
    var id = caja.getAttribute('data-wistia'); if (!/^[a-z0-9]{6,14}$/.test(id)) return;
    var p = d.createElement('wistia-player'); p.setAttribute('media-id', id); p.setAttribute('aspect', '1.7777777777777777');
    p.style.backgroundImage = "url('https://fast.wistia.com/embed/medias/" + id + "/swatch')";
    caja.appendChild(p);
    var a = d.createElement('script'); a.src = 'https://fast.wistia.com/player.js'; a.async = true; d.head.appendChild(a);
    var b = d.createElement('script'); b.src = 'https://fast.wistia.com/embed/' + id + '.js'; b.async = true; b.type = 'module'; d.head.appendChild(b);
    var visto = false;
    p.addEventListener('play', function () { if (!visto) { visto = true; evento('VideoConSonido', { pagina: location.pathname }, true); } });
    p.addEventListener('ended', function () { evento('VideoCompleto', { pagina: location.pathname }, true); });
  });

  /* ── los testimonios: suena uno por vez ── */
  var videos = $$('.testis video');
  videos.forEach(function (v) {
    v.addEventListener('play', function () { videos.forEach(function (x) { if (x !== v) x.pause(); }); });
    v.addEventListener('play', function () { evento('Testimonio', { cual: v.getAttribute('data-nombre') || '' }, true); }, { once: true });
  });
})();
