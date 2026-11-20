/* Lo común de las páginas de «La decisión» (Roberto Páez · ropaez.com).
   KX.pago: los links de pago de El Consultorio (PayPal). Mientras estén vacíos, el botón avisa y no lleva a ningún lado.
   KX.calendario: el id del calendario «La decisión · sesión 1-1» (se usa en /la-decision-gracias).
   KX.capitulo: el PDF del capítulo 1 sin costo (se usa en /la-decision-capitulo-1). */
var KX = {
  pixel: '862806975907599',
  pago: { libro: '', libroMails: '', sesion: '' },
  calendario: 'Pbmndm4WLZsadIzbIj2j',
  capitulo: 'https://raw.githubusercontent.com/learners417/landings/main/imgs/roberto/la-decision-capitulo-1.pdf',
  rutas: { landing: '/la-decision', sesion: '/la-decision-sesion', gracias: '/la-decision-gracias' }
};
(function () {
  var d = document, w = window;
  var $ = function (s, r) { return (r || d).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || d).querySelectorAll(s)); };
  var vista = (w.__tcdCarga && w.__tcdCarga.rama && w.__tcdCarga.rama !== 'main');   /* ?rama=…: vista previa, sin píxel */
  var q = new URLSearchParams(location.search);

  /* ── el píxel de Roberto: si El Consultorio ya lo cargó, se usa ese; si no, se carga aquí ── */
  function pixel() {
    if (vista) return null;
    if (!w.fbq) {
      !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
        if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v;
        s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(w, d, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      w.fbq('init', KX.pixel); w.fbq('track', 'PageView');
    }
    return w.fbq;
  }
  function evento(nombre, datos, propio) {
    var f = pixel(); if (!f) return;
    try { f(propio ? 'trackSingleCustom' : 'trackSingle', KX.pixel, nombre, datos || {}); } catch (e) {}
  }
  /* una compra se cuenta una sola vez por navegador */
  function compra(clave, valor, nombre) {
    try { if (localStorage.getItem('kx_' + clave)) return; localStorage.setItem('kx_' + clave, '1'); } catch (e) {}
    evento('Purchase', { value: valor, currency: 'USD', content_name: nombre });
  }
  w.KXevento = evento; w.KXcompra = compra;

  /* ── aparecer al bajar ── */
  var quieto = w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in w && !quieto) {
    var io = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .12 });
    $$('.rv').forEach(function (el) { io.observe(el); });
  } else $$('.rv').forEach(function (el) { el.classList.add('in'); });

  /* ── la compra del libro, con o sin los correos de Roberto ── */
  var suma = $('#suma'), total = $('[data-total]');
  function conMails() { return !!(suma && suma.checked); }
  function pintar() { if (total) total.textContent = conMails() ? '44' : '27'; }
  if (suma) { suma.addEventListener('change', function () { pintar(); evento('SumaCorreos', { activo: conMails() }, true); }); pintar(); }
  $$('[data-comprar]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var tipo = a.getAttribute('data-comprar');
      if (tipo === 'ir') return;                         /* el botón de arriba baja hasta la oferta */
      var url = tipo === 'sesion' ? KX.pago.sesion : (conMails() ? KX.pago.libroMails : KX.pago.libro);
      var valor = tipo === 'sesion' ? 97 : (conMails() ? 44 : 27);
      evento('InitiateCheckout', { value: valor, currency: 'USD', content_name: tipo === 'sesion' ? 'Sesión La decisión' : 'La decisión' });
      if (!url) { e.preventDefault(); var av = $('.aviso', a.closest('section') || d); if (av) av.classList.add('ver'); return; }
      a.href = url;
    });
  });

  /* ── la barra fija del celular: aparece después de la portada y se esconde sobre la oferta ── */
  var fija = $('.fija'), portada = $('#portada'), oferta = $('#comprar');
  if (fija && portada && 'IntersectionObserver' in w) {
    var vis = { portada: true, oferta: false };
    var mira = function () { fija.classList.toggle('ver', !vis.portada && !vis.oferta); };
    new IntersectionObserver(function (en) { vis.portada = en[0].isIntersecting; mira(); }).observe(portada);
    if (oferta) new IntersectionObserver(function (en) { vis.oferta = en[0].isIntersecting; mira(); }).observe(oferta);
  }

  /* ── los videos: se cargan recién al tocarlos ── */
  $$('.video').forEach(function (c) {
    var v = $('video', c), b = $('button', c);
    if (!v || !b) return;
    b.addEventListener('click', function () {
      $$('.video video').forEach(function (o) { if (o !== v) o.pause(); });
      c.classList.add('sonando'); v.controls = true; v.preload = 'auto';
      var p = v.play(); if (p && p.catch) p.catch(function () {});
      evento('VideoTestimonio', { video: c.getAttribute('data-video') || '' }, true);
    });
  });

  /* ── lo que se compró viaja de una página a la otra (los links de pago no llevan datos) ── */
  if (q.get('m') === '1' || q.get('m') === '0') { try { localStorage.setItem('kx_mails', q.get('m')); } catch (e) {} }
  w.KXmails = function () { try { return localStorage.getItem('kx_mails') === '1'; } catch (e) { return false; } };

  /* ── la agenda de El Consultorio ── */
  var caja = d.getElementById('cal');
  if (caja) {
    var id = KX.calendario;
    var src = /^[a-z0-9]+(-[a-z0-9]+)*$/.test(id) ? 'https://api.leadconnectorhq.com/widget/bookings/' + id
      : (/^[A-Za-z0-9]{12,}$/.test(id) ? 'https://api.leadconnectorhq.com/widget/booking/' + id : '');
    if (!src) caja.innerHTML = '<p class="aviso ver">La agenda se abre en unas horas. Te escribimos a tu correo para que elijas tu horario.</p>';
    else {
      var f = d.createElement('iframe');
      f.src = src; f.id = id + '_kx'; f.title = 'Agenda tu sesión con Roberto'; f.setAttribute('scrolling', 'no');
      caja.appendChild(f);
      var s = d.createElement('script'); s.src = 'https://link.msgsndr.com/js/form_embed.js'; s.async = true; d.body.appendChild(s);
      var avisado = false;
      w.addEventListener('message', function (e) {
        if (typeof e.origin !== 'string' || e.origin.indexOf('leadconnectorhq') < 0) return;
        var x = e.data || {};
        if (x && typeof x === 'object') { var h = x.height || x.iframeHeight || (x.data && x.data.height); if (typeof h === 'number' && h > 300) f.style.minHeight = h + 'px'; }
        var t = String((typeof x === 'string') ? x : (x.type || x.event || '')).toLowerCase();
        if (!avisado && (t.indexOf('book') > -1 || t.indexOf('appointment') > -1)) { avisado = true; evento('Schedule', { content_name: 'Sesión La decisión' }); }
      }, false);
    }
  }

  /* ── el capítulo 1 ── */
  $$('[data-capitulo]').forEach(function (a) {
    if (KX.capitulo) a.href = KX.capitulo;
    a.addEventListener('click', function (e) {
      if (!KX.capitulo) { e.preventDefault(); var av = $('.aviso', a.closest('section') || d); if (av) av.classList.add('ver'); return; }
      evento('Lead', { content_name: 'Capítulo 1 · La decisión' });
    });
  });

})();
