/* ═══════════════════════════════════════════════════════════════
   Lo que hacen todas las páginas: precios y links desde config.js,
   el píxel, lo que aparece al bajar, las preguntas, los testimonios.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  var C = window.TCD || {};
  var P = C.precios || {};
  var pagina = document.body.getAttribute('data-pagina') || 'pagina';

  var NOMBRES = {
    numero: 'El Número', obra: 'Tu nuevo precio', verde: 'la app · Tu Sistema', negro: 'la app · El Programa Completo',
    sanadores: 'Sanadores Libres', lago: 'Lo que el lago te enseña', montana: 'Lo que la montaña te enseña',
    viento: 'Lo que el viento te enseña', rio: 'Lo que el río te enseña', bosque: 'Lo que el bosque te enseña',
    heroe: 'Héroe descapado', libertades: 'Las 7 libertades fundamentales',
    apaga: 'Apaga la cabeza de La Clínica del Líder', ejeSolo: 'El Eje Solo de La Clínica del Líder', ejeAcomp: 'El Eje Acompañado de La Clínica del Líder'
  };
  window.TCD_NOMBRES = NOMBRES;

  /* de dónde viene: la palabra del carrusel o del reel (?p=PALABRA) */
  var origen = '';
  try {
    var q = new URLSearchParams(location.search);
    origen = (q.get('p') || q.get('utm_content') || '').toUpperCase().replace(/[^A-ZÑ0-9_-]/g, '').slice(0, 24);
    if (origen) sessionStorage.setItem('tcd_origen', origen); else origen = sessionStorage.getItem('tcd_origen') || '';
  } catch (e) {}
  window.TCD_ORIGEN = origen;

  /* ── píxel ─────────────────────────────── */
  /* Solo al píxel de TCD: GHL puede tener otro píxel en la misma página.
     Cada evento va también a Clarity con el mismo nombre (PageView y ViewContent no: Clarity ya cuenta las visitas). */
  function cl(ev) { try { if (window.clarity && ev !== 'PageView' && ev !== 'ViewContent') clarity('event', ev); } catch (e) {} }
  function px(ev, datos) { cl(ev); try { if (window.fbq) C.pixel ? fbq('trackSingle', C.pixel, ev, datos || {}) : fbq('track', ev, datos || {}); } catch (e) {} }
  function pxc(ev, datos) { cl(ev); try { if (window.fbq) C.pixel ? fbq('trackSingleCustom', C.pixel, ev, datos || {}) : fbq('trackCustom', ev, datos || {}); } catch (e) {} }
  window.px = px; window.pxc = pxc;
  if (C.pixel && !/claude\.ai|claudeusercontent|localhost|^file:/.test(location.href)) {
    !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments) }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s) }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', C.pixel); px('PageView');
    px('ViewContent', { content_name: pagina, content_category: origen || 'directo' });
  }

  /* ── WhatsApp ──────────────────────────── */
  function wa(texto) { return 'https://wa.me/' + (C.whatsapp || '') + '?text=' + encodeURIComponent(texto); }
  window.wa = wa;

  /* ── precios ───────────────────────────── */
  document.querySelectorAll('[data-precio]').forEach(function (el) {
    var k = el.getAttribute('data-precio');
    if (P[k] != null) el.textContent = P[k];
  });
  document.querySelectorAll('[data-suma]').forEach(function (el) {
    var t = 0; el.getAttribute('data-suma').split(',').forEach(function (k) { t += +(P[k.trim()] || 0); });
    el.textContent = t;
  });

  /* ── botones de compra ─────────────────── */
  document.querySelectorAll('[data-compra]').forEach(function (a) {
    var k = a.getAttribute('data-compra');
    var link = (C.pagos || {})[k];
    if (link) { a.href = link; if (!/^\/|^https?:\/\/(www\.)?tuclinica\.digital/.test(link)) { a.target = '_blank'; a.rel = 'noopener'; } }
    else {
      var msg = 'Hola Javo, quiero ' + (NOMBRES[k] || k) + ' (' + (P[k] || '') + ' USD).' + (origen ? ' Vengo por ' + origen + '.' : '');
      a.href = wa(msg); a.target = '_blank'; a.rel = 'noopener';
    }
    a.addEventListener('click', function () {
      px('InitiateCheckout', { value: P[k] || 0, currency: 'USD', content_name: k, content_category: origen || 'directo' });
    });
  });
  document.querySelectorAll('[data-wa]').forEach(function (a) {
    a.href = wa(a.getAttribute('data-wa')); a.target = '_blank'; a.rel = 'noopener';
  });
  document.querySelectorAll('[data-link]').forEach(function (a) {
    var k = a.getAttribute('data-link'); if (C[k]) a.href = C[k] + (a.getAttribute('data-hash') || '');
  });
  /* imágenes: van dentro de la página (window.TCD_IMGS) */
  document.querySelectorAll('[data-img]').forEach(function (im) {
    var k = im.getAttribute('data-img'), E = window.TCD_IMGS || {};
    im.src = E[k] || ((C.img || '') + k);
    im.addEventListener('error', function () { if (im.hasAttribute('data-quita-si-falla')) im.style.display = 'none'; });
  });
  /* aviso de pago: PayPal si hay links, WhatsApp si todavía no */
  var claves = (document.body.getAttribute('data-pagos') || '').split(' ').filter(Boolean);
  var hayPago = claves.some(function (k) { return (C.pagos || {})[k]; });
  document.querySelectorAll(hayPago ? '.con-pago' : '.sin-pago').forEach(function (e) { e.style.display = 'flex'; });

  /* ── aparecer al bajar ─────────────────── */
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px', threshold: .12 }) : null;
  document.querySelectorAll('.rv,.frases li,.paso').forEach(function (el) { io ? io.observe(el) : el.classList.add('in'); });

  /* la barra de arriba gana su línea al bajar; la de abajo aparece pasada la portada */
  var top = document.querySelector('.top'), barra = document.querySelector('.barra');
  var desde = document.querySelector('[data-barra-desde]'), hasta = document.querySelector('[data-barra-hasta]');
  function alBajar() {
    var y = window.scrollY;
    if (top) top.classList.toggle('con-linea', y > 8);
    if (barra && desde) {
      var a = desde.getBoundingClientRect().bottom < 0;
      var b = hasta ? hasta.getBoundingClientRect().top < window.innerHeight * .9 && hasta.getBoundingClientRect().bottom > 0 : false;
      barra.classList.toggle('on', a && !b);
    }
    document.querySelectorAll('.ruta').forEach(function (r) {
      var rc = r.getBoundingClientRect(), h = window.innerHeight;
      var p = Math.min(1, Math.max(0, (h * .7 - rc.top) / rc.height));
      r.style.setProperty('--avance', (p * 100).toFixed(1) + '%');
    });
  }
  window.addEventListener('scroll', alBajar, { passive: true }); alBajar();

  /* ── preguntas ─────────────────────────── */
  document.querySelectorAll('.fq button').forEach(function (b) {
    b.setAttribute('aria-expanded', 'false');
    b.addEventListener('click', function () {
      var f = b.parentNode, o = f.classList.toggle('op');
      b.setAttribute('aria-expanded', o ? 'true' : 'false');
      if (o) pxc('Pregunta', { pregunta: b.textContent.trim().slice(0, 60) });
    });
  });

  /* ── imágenes livianas: el CDN de GHL las entrega en webp y al tamaño justo ── */
  function opt(u, w) { return 'https://images.leadconnectorhq.com/image/f_webp/q_72/r_' + w + '/u_' + u; }
  function imgOpt(im, u, w) {
    im.src = opt(u, w); im.decoding = 'async';
    im.addEventListener('error', function f() { im.removeEventListener('error', f); im.src = u; });
  }
  window.TCD_IMG = imgOpt;
  document.querySelectorAll('[data-foto]').forEach(function (i) { if (C.foto) imgOpt(i, C.foto, +(i.getAttribute('data-ancho') || 640)); });

  /* ── el muro de testimonios: se arma solo desde config.js ── */
  var M = C.media || '';
  document.querySelectorAll('[data-muro]').forEach(function (box) {
    var lista = (C.testimonios || []).slice();
    var desde = +(box.getAttribute('data-desde') || 0); if (desde) lista = lista.slice(desde).concat(lista.slice(0, desde));
    var max = +(box.getAttribute('data-max') || lista.length); lista = lista.slice(0, max);
    var ver = +(box.getAttribute('data-muro') || 8);
    lista.forEach(function (t, i) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'tv' + (i >= ver ? ' extra' : '');
      b.setAttribute('aria-label', 'Ver testimonio');
      if (t[0] === 'y') {
        b.setAttribute('data-yt', t[1]); b.setAttribute('data-horizontal', '');
        b.innerHTML = '<img loading="lazy" decoding="async" alt="" src="https://i.ytimg.com/vi/' + t[1] + '/hqdefault.jpg"><span class="play"></span>';
      } else {
        var u = M + t[1] + '.mp4'; b.setAttribute('data-mp4', u);
        b.innerHTML = '<video muted playsinline preload="none" data-src="' + u + '"></video><span class="play"></span>';
      }
      box.appendChild(b);
    });
    if (lista.length > ver) {
      var m = document.createElement('div'); m.className = 'mas';
      m.innerHTML = '<button type="button" class="btn claro"><span>Ver los ' + lista.length + ' testimonios</span></button>';
      box.parentNode.insertBefore(m, box.nextSibling);
      m.querySelector('button').addEventListener('click', function () {
        box.classList.add('todos'); m.remove(); pxc('MuroCompleto', { pagina: pagina });
        box.querySelectorAll('.extra video[data-src]').forEach(function (v) { if (vio) vio.observe(v); });
      });
    }
  });
  /* las capturas de mensajes */
  document.querySelectorAll('[data-capturas]').forEach(function (box) {
    (C.capturas || []).forEach(function (f) {
      var im = document.createElement('img'); im.alt = 'Mensaje de un cliente'; im.loading = 'lazy'; im.className = 'cap';
      imgOpt(im, M + f, 720); box.appendChild(im);
    });
  });
  /* las fotos de eventos y rodajes: una cinta que pasa sola */
  document.querySelectorAll('[data-fotos]').forEach(function (box) {
    var t = document.createElement('div'); t.className = 'cinta-fotos';
    var fs = C.fotos || [];
    fs.concat(fs).forEach(function (f, i) {
      var im = document.createElement('img'); im.alt = i < fs.length ? 'Javo Katz en eventos y rodajes' : ''; im.loading = 'lazy';
      imgOpt(im, M + f, 560); t.appendChild(im);
    });
    box.appendChild(t);
  });

  /* ── testimonios: el primer cuadro se carga al verse, el video se abre grande ── */
  var vio = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      var v = e.target; v.src = v.getAttribute('data-src') + '#t=0.6'; v.preload = 'metadata'; vio.unobserve(v);
    });
  }, { rootMargin: '200px' }) : null;
  document.querySelectorAll('.tv:not(.extra) video[data-src]').forEach(function (v) {
    v.muted = true; v.playsInline = true;
    v.addEventListener('error', function () { var b = v.closest('.tv'); if (b) b.style.display = 'none'; });
    vio ? vio.observe(v) : (v.src = v.getAttribute('data-src') + '#t=0.6');
  });
  document.querySelectorAll('img[data-quita-si-falla]').forEach(function (im) {
    im.addEventListener('error', function () { im.style.display = 'none'; });
  });
  var lb = document.querySelector('.lb');
  function cerrar() { if (!lb) return; lb.classList.remove('on'); lb.querySelector('.caja').innerHTML = ''; lb.querySelector('.caja').classList.remove('img'); document.body.style.overflow = ''; }
  if (lb) {
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('cerrar')) cerrar(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') cerrar(); });
    document.querySelectorAll('.tv').forEach(function (b) {
      b.addEventListener('click', function () {
        var caja = lb.querySelector('.caja'), mp4 = b.getAttribute('data-mp4'), yt = b.getAttribute('data-yt');
        caja.classList.toggle('h', !!yt && b.hasAttribute('data-horizontal'));
        caja.innerHTML = mp4 ? '<video src="' + mp4 + '" controls autoplay playsinline></video>'
          : '<iframe src="https://www.youtube-nocookie.com/embed/' + yt + '?autoplay=1&rel=0&playsinline=1" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="Testimonio"></iframe>';
        lb.classList.add('on'); document.body.style.overflow = 'hidden';
        pxc('Testimonio', { pagina: pagina });
      });
    });
  }

  /* ── capturas: se agrandan al tocar ── */
  document.querySelectorAll('img.cap').forEach(function (im) {
    im.addEventListener('click', function () { if (!lb) return; var c = lb.querySelector('.caja'); c.classList.add('img'); c.innerHTML = '<img src="' + im.src + '" alt="">'; lb.classList.add('on'); document.body.style.overflow = 'hidden'; });
  });
  /* ── los números cuentan al aparecer ── */
  var cuenta = 'IntersectionObserver' in window && !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
  document.querySelectorAll('[data-count]').forEach(function (b) {
    if (!cuenta) return;
    var n = +b.getAttribute('data-count'), suf = b.getAttribute('data-suf') || '';
    var o = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return; o.disconnect(); var t0 = null;
      function st(t) { if (!t0) t0 = t; var k = Math.min(1, (t - t0) / 1200); k = 1 - Math.pow(1 - k, 3); b.textContent = Math.round(n * k).toLocaleString('es') + suf; if (k < 1) requestAnimationFrame(st); }
      requestAnimationFrame(st);
    }, { threshold: .5 });
    o.observe(b);
  });

  /* ── aviso corto ───────────────────────── */
  window.aviso = function (t) {
    var a = document.querySelector('.aviso'); if (!a) { a = document.createElement('div'); a.className = 'aviso'; document.body.appendChild(a); }
    a.textContent = t; a.classList.add('on'); clearTimeout(a._t); a._t = setTimeout(function () { a.classList.remove('on'); }, 2400);
  };

  /* ── la cuenta: tu hora real neta ──────── */
  document.querySelectorAll('[data-cuenta]').forEach(function (box) {
    var $ = function (s) { return box.querySelector(s); };
    var ins = box.querySelectorAll('input[type=range]');
    var tocado = false;
    function plata(n) { return '$' + Math.round(n).toLocaleString('es'); }
    function calc() {
      var precio = +$('[name=precio]').value, ses = +$('[name=sesiones]').value, extra = +$('[name=extra]').value, gastos = +$('[name=gastos]').value;
      $('[data-o=precio]').textContent = plata(precio);
      $('[data-o=sesiones]').textContent = ses;
      $('[data-o=extra]').textContent = extra + ' h';
      $('[data-o=gastos]').textContent = plata(gastos);
      var semanas = 4.33, ingreso = precio * ses * semanas, horas = (ses + extra) * semanas;
      var real = horas ? (ingreso - gastos) / horas : 0;
      $('[data-o=cobras]').textContent = plata(precio);
      $('[data-o=real]').textContent = plata(Math.max(real, 0));
      var pct = precio ? Math.round(real / precio * 100) : 0;
      var anual = Math.round(extra * 48);
      $('[data-o=veredicto]').innerHTML = 'Por cada hora de tu vida que le das a tu trabajo te quedan <b>' + plata(Math.max(real, 0)) + '</b>: el <b>' + Math.max(pct, 0) + ' %</b> de lo que dice tu tarifa. Y al año trabajas <b>' + anual.toLocaleString('es') + ' horas</b> que nadie te paga.';
    }
    ins.forEach(function (i) { i.addEventListener('input', function () { calc(); if (!tocado) { tocado = true; pxc('Cuenta', { pagina: pagina }); } }); });
    calc();
  });

  /* ── el teléfono con la app ────────────── */
  document.querySelectorAll('[data-tel]').forEach(function (tel) {
    var vistas = tel.querySelectorAll('.vista'), tabs = tel.querySelectorAll('.tabs button');
    var afuera = document.querySelectorAll('[data-toca]');
    var chatHecho = false;
    function ir(id) {
      vistas.forEach(function (v) { v.classList.toggle('on', v.getAttribute('data-v') === id); });
      tabs.forEach(function (t) { t.classList.toggle('on', t.getAttribute('data-ir') === id); });
      afuera.forEach(function (t) { t.classList.toggle('on', t.getAttribute('data-toca') === id); });
      if (id === 'mentor') chat();
    }
    function chat() {
      if (chatHecho) return; chatHecho = true;
      var c = tel.querySelector('.chat'); if (!c) return;
      var guion = JSON.parse(c.getAttribute('data-guion') || '[]');
      guion.forEach(function (m, i) {
        setTimeout(function () {
          var d = document.createElement('div'); d.className = 'msg ' + m[0];
          d.innerHTML = (m[0] === 'ia' && m[2] ? '<i>' + m[2] + '</i>' : '') + m[1];
          c.appendChild(d); requestAnimationFrame(function () { requestAnimationFrame(function () { d.classList.add('in'); }); });
        }, 500 + i * 1500);
      });
    }
    tabs.forEach(function (t) { t.addEventListener('click', function () { ir(t.getAttribute('data-ir')); pxc('App', { vista: t.getAttribute('data-ir') }); }); });
    afuera.forEach(function (t) { t.addEventListener('click', function () { ir(t.getAttribute('data-toca')); pxc('App', { vista: t.getAttribute('data-toca') }); }); });
    /* la cuenta del teléfono */
    var f = tel.querySelectorAll('.campo input');
    function cuentaTel() {
      var p = +f[0].value || 0, s = +f[1].value || 0, x = +f[2].value || 0;
      var r = (s + x) ? (p * s) / (s + x) : 0;
      var o = tel.querySelector('[data-o=tel-real]'); if (o) o.textContent = '$' + Math.round(r);
      var n = tel.querySelector('[data-o=tel-nota]'); if (n) n.textContent = 'Cobras $' + Math.round(p) + ' por sesión. Al año, ' + Math.round(x * 48).toLocaleString('es') + ' horas sin cobrar.';
    }
    f.forEach(function (i) { i.addEventListener('input', cuentaTel); }); if (f.length) cuentaTel();
    ir(tel.getAttribute('data-inicio') || 'hoy');
  });
})();

/* La puerta de los primeros capítulos: nombre y correo antes de leer.
   Formulario de GHL «Lectores · primer capítulo» (TCD.formLectores); al enviarlo arranca el flujo
   «Lectores · 10 días». Quien ya lo dejó en este navegador, o llega desde un correo con ?lector=1,
   lee directo. Si el formulario no carga en 12 segundos, aparece un link para leer igual. */
(function () {
  var C = window.TCD || {};
  var ID = C.formLectores;
  var portada = document.querySelector('.hoja.inicio');
  if (!ID || !portada) return;
  var CLAVE = 'tcd_lector';
  var libro = document.body.getAttribute('data-libro') || '';
  function guardar() { try { localStorage.setItem(CLAVE, '1'); } catch (e) {} }
  function yaEs() { try { return localStorage.getItem(CLAVE) === '1'; } catch (e) { return false; } }
  try { if (new URLSearchParams(location.search).get('lector') === '1') guardar(); } catch (e) {}

  var caja = null, ifr = null, alAbrir = null, cargo = false;
  function armar() {
    if (caja) return;
    caja = document.createElement('div');
    caja.className = 'puerta';
    caja.innerHTML =
      '<p class="puerta-t">Antes de empezar</p>' +
      '<p class="puerta-b">Déjame tu nombre y tu correo. Lees este capítulo ahora mismo y, día por día, te mando el primer capítulo de mis otros libros, con su ejercicio.</p>' +
      '<iframe title="Tu nombre y tu correo" id="inline-' + ID + '" data-form-id="' + ID + '"' +
      ' data-layout="{\'id\':\'INLINE\'}" data-layout-iframe-id="inline-' + ID + '" data-trigger-type="alwaysShow"' +
      ' data-activation-type="alwaysActivated" data-deactivation-type="neverDeactivate" data-form-name="Lectores · primer capítulo"' +
      ' src="https://api.leadconnectorhq.com/widget/form/' + ID + '" style="width:100%;height:340px;border:none;display:block;background:transparent"></iframe>' +
      '<p class="puerta-alt" hidden>¿No ves el formulario? <a class="link" href="#" data-puerta-saltar>Empieza a leer aquí</a>.</p>';
    var btn = portada.querySelector('[data-ir="1"]');
    if (btn) { btn.insertAdjacentElement('afterend', caja); btn.style.display = 'none'; }
    else portada.appendChild(caja);
    ifr = caja.querySelector('iframe');
    if (!document.querySelector('script[src*="form_embed.js"]')) {
      var s = document.createElement('script'); s.src = 'https://link.msgsndr.com/js/form_embed.js'; s.async = true;
      document.body.appendChild(s);
    }
    setTimeout(function () { if (!cargo && caja) caja.querySelector('.puerta-alt').hidden = false; }, 12000);
    caja.querySelector('[data-puerta-saltar]').addEventListener('click', function (e) { e.preventDefault(); abrir(false); });
    if (window.pxc) pxc('VioPuerta', { content_name: libro });
  }
  function abrir(conCorreo) {
    if (conCorreo) { guardar(); if (window.px) px('Lead', { content_name: 'capitulo-' + libro }); }
    if (caja) { caja.remove(); caja = null; ifr = null; }
    var btn = portada.querySelector('[data-ir="1"]'); if (btn) btn.style.display = '';
    window.TCD_PUERTA.abierta = true;
    var f = alAbrir; alAbrir = null; if (f) f();
  }
  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!ifr || !Array.isArray(d) || e.source !== ifr.contentWindow) return;
    if (d[0] === 'highlevel.setHeight' && d[1] && d[1].height) { cargo = true; ifr.style.height = (d[1].height + 6) + 'px'; }
    if (d[0] === 'iframeLoaded' || d[0] === 'fetch-sticky-contacts' || d[0] === 'fetch-query-params') cargo = true;
    if (d[0] === 'set-sticky-contacts') abrir(true);
  });
  window.TCD_PUERTA = {
    abierta: yaEs(),
    pedir: function (cb, quieto) {
      alAbrir = cb; armar();
      if (!quieto) try { caja.scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (e) {}
    }
  };
})();

/* ── La línea única de Tu nuevo precio (TCD.linea97) en cada [data-linea97] ── */
(function () {
  var C = window.TCD || {};
  if (!C.linea97) return;
  document.querySelectorAll('[data-linea97]').forEach(function (el) { el.textContent = C.linea97; });
})();

/* ── Lista de espera ── botones con data-espera="<lista>" y data-espera-nombre="<cómo se llama>".
   Con TCD.formEspera abre el formulario de GHL «Lista de espera» con la lista puesta; sin él, abre tu WhatsApp. */
(function () {
  var C = window.TCD || {};
  var bs = document.querySelectorAll('[data-espera]');
  if (!bs.length) return;
  function cerrar(f) { if (f && f.parentNode) f.parentNode.removeChild(f); document.documentElement.style.overflow = ''; }
  bs.forEach(function (b) {
    var lista = b.getAttribute('data-espera'), nom = b.getAttribute('data-espera-nombre') || lista;
    if (!C.formEspera) {
      b.href = 'https://wa.me/' + (C.whatsapp || '') + '?text=' + encodeURIComponent('Hola Javo, quiero estar en la lista de espera de ' + nom + '.');
      b.target = '_blank'; b.rel = 'noopener';
    }
    b.addEventListener('click', function (e) {
      if (window.pxc) pxc('ListaEspera', { content_name: lista });
      if (!C.formEspera) return;
      e.preventDefault();
      var f = document.createElement('div');
      f.className = 'espera-fondo'; f.setAttribute('role', 'dialog'); f.setAttribute('aria-modal', 'true'); f.setAttribute('aria-label', 'Lista de espera');
      f.innerHTML = '<div class="espera card"><button type="button" class="espera-x" aria-label="Cerrar">×</button>' +
        '<span class="eti">Lista de espera</span><b class="espera-t"></b><p>Te aviso por correo el día que abre.</p>' +
        '<iframe title="Lista de espera" src="https://api.leadconnectorhq.com/widget/form/' + C.formEspera + '?lista=' + encodeURIComponent(lista) +
        '" style="width:100%;height:300px;border:none;display:block;background:transparent"></iframe></div>';
      f.querySelector('.espera-t').textContent = nom;
      f.addEventListener('click', function (ev) { if (ev.target === f || ev.target.className === 'espera-x') cerrar(f); });
      document.addEventListener('keydown', function esc(ev) { if (ev.key === 'Escape') { cerrar(f); document.removeEventListener('keydown', esc); } });
      document.body.appendChild(f); document.documentElement.style.overflow = 'hidden';
      if (!document.querySelector('script[src*="form_embed.js"]')) {
        var sc = document.createElement('script'); sc.src = 'https://link.msgsndr.com/js/form_embed.js'; sc.async = true; document.body.appendChild(sc);
      }
    });
  });
})();
