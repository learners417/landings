/* ═══════════════════════════════════════════════════════════════
   Cargador de las páginas de Javo Katz en GHL (tuclinica.digital).

   En GHL, cada página tiene una sola línea (ghl-linea.html) que trae
   este archivo. Este archivo trae la página desde site/<ruta>.html y
   la monta dentro de la página de GHL, al lado de lo que GHL hace por
   detrás: estadísticas del embudo, atribución, formularios, calendarios.

   La ruta de GHL decide el archivo: /impostor → site/impostor.html.
   Fuente principal: jsDelivr. Respaldo: GitHub.
   ═══════════════════════════════════════════════════════════════ */
(function (d, w) {
  if (w.__tcdCargador) return;
  w.__tcdCargador = 1;

  var REPO = 'learners417/landings';
  var ALIAS = { '': 'inicio', 'retiros-2027': 'retiros' };
  /* La vista previa: ?rama=edicion trae la página de esa rama de GitHub, para mirarla antes de publicarla.
     En la vista previa no se cargan el píxel ni Clarity (base.js y clarity.js miran carga.rama). */
  var rama = 'main';
  try {
    var pedida = new URLSearchParams(location.search).get('rama');
    if (pedida && /^[a-z0-9-]{2,30}$/.test(pedida)) rama = pedida;
  } catch (e) {}

  var ruta = location.pathname.replace(/^\/+|\/+$/g, '').toLowerCase();
  /* Pasos clonados en GHL que heredan el TCD_PAGINA de su original: acá la ruta manda. */
  var RUTA_MANDA = { 'retiros-preparacion': 'retiros-preparacion' };
  var pagina = RUTA_MANDA[ruta] || w.TCD_PAGINA || (ruta in ALIAS ? ALIAS[ruta] : ruta);
  var archivo = '/site/' + pagina + '.html';
  var FUENTES = [
    'https://cdn.jsdelivr.net/gh/' + REPO + '@' + rama + archivo,
    'https://raw.githubusercontent.com/' + REPO + '/' + rama + archivo
  ];

  var carga = w.__tcdCarga = {
    pagina: pagina,
    rama: rama,
    inicio: Math.round(performance.now())
  };

  /* Respaldo de imágenes: si jsDelivr falla o tiene topes en un archivo del repo,
     pide la misma imagen una sola vez a raw.githubusercontent.com. */
  var CDN_IMG = 'https://cdn.jsdelivr.net/gh/' + REPO + '@';
  d.addEventListener('error', function (e) {
    var el = e.target;
    if (!el || el.tagName !== 'IMG' || el.getAttribute('data-tcd-gh')) return;
    var src = el.currentSrc || el.src || '';
    if (src.indexOf(CDN_IMG) !== 0) return;
    el.setAttribute('data-tcd-gh', '1');
    if (el.getAttribute('srcset')) el.removeAttribute('srcset');
    el.src = 'https://raw.githubusercontent.com/' + REPO + '/' + src.slice(CDN_IMG.length);
    carga.imgGitHub = (carga.imgGitHub || 0) + 1;
  }, true);

  /* La tapa: oculta lo visible de GHL mientras llega la página. */
  var tapa = d.getElementById('tcd-tapa');
  if (!tapa) {
    tapa = d.createElement('style');
    tapa.id = 'tcd-tapa';
    tapa.textContent = '#__nuxt,#teleports{display:none!important}html{background:#F4EEE3}';
    d.head.appendChild(tapa);
  }

  /* Precarga de Manrope para evitar saltos tipográficos al montar. */
  var SIN_MANROPE = /^(app|app-745191|el-numero|generador-pp|index|modelodenegocio|sharyl)$|^libro\//;
  var LATIN = 'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD';
  var letra = null;
  if (!SIN_MANROPE.test(pagina) && w.FontFace && d.fonts && w.fetch) {
    try {
      letra = fetch('https://fonts.gstatic.com/s/manrope/v23/xn7gYHE41ni1AdIRggexSg.woff2')
        .then(function (r) { if (!r.ok) throw r.status; return r.arrayBuffer(); })
        .then(function (b) { carga.letraLlego = Math.round(performance.now()); return b; }, function () { return null; });
    } catch (e) { letra = null; }
  }

  /* Conexiones previas para fuentes y píxel en producción. */
  if (rama === 'main') {
    ['https://fonts.googleapis.com', 'https://connect.facebook.net'].forEach(function (u) {
      try {
        var l = d.createElement('link');
        l.rel = 'preconnect';
        l.href = u;
        d.head.appendChild(l);
      } catch (e) {}
    });
  }

  function conLetra(html) {
    try {
      if (!letra) return html;
      var m = /fonts\.googleapis\.com\/css2\?[^"']*family=Manrope:wght@([0-9.;]+)/.exec(html);
      if (!m) return html;
      var pesos = m[1].indexOf('..') > 0 ? [m[1].replace('..', ' ')] : m[1].split(';');
      var pedido = 'family=Manrope:wght@' + m[1];
    } catch (e) { return html; }

    return new Promise(function (ok) {
      var hecho = false, t = performance.now();
      function sigue() {
        if (!hecho) {
          hecho = true;
          carga.esperaLetra = Math.round(performance.now() - t);
          ok(html);
        }
      }
      setTimeout(sigue, 250);
      letra.then(function (b) {
        if (!b) return;
        return Promise.all(pesos.map(function (p) {
          var f = new FontFace('Manrope', b, { weight: p, style: 'normal', display: 'swap', unicodeRange: LATIN });
          d.fonts.add(f);
          return f.loaded;
        })).then(function () {
          carga.letra = hecho ? 'tarde' : 'lista';
          if (!hecho) carga.manrope = pedido;
        });
      }).then(sigue, sigue);
    });
  }

  function traer(url, ms) {
    return new Promise(function (ok, no) {
      var reloj = setTimeout(function () { no('tiempo'); }, ms);
      fetch(url, { cache: 'no-cache' })
        .then(function (r) { if (!r.ok) throw r.status; return r.text(); })
        .then(function (t) { clearTimeout(reloj); ok(t); },
              function (e) { clearTimeout(reloj); no(e); });
    });
  }

  /* Compite jsDelivr y GitHub: si jsDelivr no responde en 1,5 s (o falla), dispara respaldo. */
  function primera() {
    return new Promise(function (ok, no) {
      var gano = false, fallas = 0, pedidas = 0, reserva = null;
      function pide(i) {
        if (i >= FUENTES.length || i < pedidas) return;
        pedidas = i + 1;
        traer(FUENTES[i], 12000).then(function (t) {
          if (gano) return;
          gano = true;
          clearTimeout(reserva);
          carga.fuente = FUENTES[i];
          carga.msFuente = Math.round(performance.now() - carga.inicio);
          ok(t);
        }, function (err) {
          fallas++;
          carga['errorFuente' + i] = String(err || 'error');
          if (gano) return;
          if (pedidas < FUENTES.length) {
            clearTimeout(reserva);
            pide(pedidas);
          } else if (fallas >= FUENTES.length) {
            no('sin fuente');
          }
        });
      }
      pide(0);
      reserva = setTimeout(function () { if (!gano) pide(1); }, 1500);
    });
  }

  /* Apaga hojas de estilo de GHL sin tocar su lógica ni conexiones. */
  function esDeGHL(n) {
    if (n.nodeType !== 1 || n.hasAttribute('data-tcd') || n.id === 'tcd-tapa') return false;
    if (n.tagName === 'LINK') return /stylesheet/.test(n.rel) && /leadconnectorhq\.com\/_preview\//.test(n.href);
    if (n.tagName === 'STYLE') return /hl_page-preview|c-section|--headlinefont|bg-fixed/.test(n.textContent);
    return false;
  }

  function apagar(n) { if (n.media !== 'not all') n.media = 'not all'; }

  function apagarGHL() {
    var l = d.querySelectorAll('head style, head link[rel~="stylesheet"], #__nuxt style, #teleports style');
    for (var i = 0; i < l.length; i++) {
      var n = l[i];
      if (n.hasAttribute('data-tcd') || n.id === 'tcd-tapa') continue;
      if (n.closest('#__nuxt, #teleports') || n.parentNode === d.head) apagar(n);
    }
    try {
      new MutationObserver(function (cambios) {
        cambios.forEach(function (c) {
          [].forEach.call(c.addedNodes, function (n) { if (esDeGHL(n)) apagar(n); });
        });
      }).observe(d.head, { childList: true });
    } catch (e) {}
  }

  function copiarAtributos(de, a) {
    for (var i = 0; i < de.attributes.length; i++) {
      a.setAttribute(de.attributes[i].name, de.attributes[i].value);
    }
  }

  function correr(viejo, sigue) {
    var s = d.createElement('script');
    for (var i = 0; i < viejo.attributes.length; i++) {
      var nombre = viejo.attributes[i].name;
      if (nombre !== 'type' && nombre !== 'data-tipo') s.setAttribute(nombre, viejo.attributes[i].value);
    }
    var tipo = viejo.getAttribute('data-tipo');
    if (tipo) s.type = tipo;

    if (viejo.getAttribute('src')) {
      if (viejo.hasAttribute('async') || tipo === 'module') {
        viejo.parentNode.replaceChild(s, viejo);
        sigue();
        return;
      }
      var hecho = false, seguir = function () { if (!hecho) { hecho = true; sigue(); } };
      s.async = false;
      s.onload = s.onerror = seguir;
      setTimeout(seguir, 4000);
      viejo.parentNode.replaceChild(s, viejo);
    } else {
      s.text = viejo.text;
      viejo.parentNode.replaceChild(s, viejo);
      sigue();
    }
  }

  function sinManropeDeGoogle(x) {
    if (!carga.manrope) return;
    var l = x.querySelectorAll('link[href*="fonts.googleapis.com/css2"]');
    for (var i = 0; i < l.length; i++) {
      var partes = (l[i].getAttribute('href') || '').split('?');
      if (partes.length !== 2) continue;
      var q = partes[1].split('&'), resto = q.filter(function (p) { return p !== carga.manrope; });
      if (resto.length === q.length) continue;
      if (!resto.some(function (p) { return p.indexOf('family=') === 0; })) l[i].parentNode.removeChild(l[i]);
      else l[i].setAttribute('href', partes[0] + '?' + resto.join('&'));
    }
  }

  function montar(html) {
    var x = new DOMParser().parseFromString(html, 'text/html');
    try { sinManropeDeGoogle(x); } catch (e) {}
    var titulo = x.title;

    var esperan = x.querySelectorAll('script');
    for (var i = 0; i < esperan.length; i++) {
      esperan[i].setAttribute('data-tipo', esperan[i].getAttribute('type') || '');
      esperan[i].setAttribute('type', 'text/tcd-espera');
    }

    apagarGHL();
    copiarAtributos(x.documentElement, d.documentElement);
    copiarAtributos(x.body, d.body);
    if (titulo) d.title = titulo;

    [].slice.call(x.head.childNodes).forEach(function (n) {
      if (n.nodeType !== 1 || n.tagName === 'TITLE') return;
      var m = d.importNode(n, true);
      m.setAttribute('data-tcd', '');
      d.head.appendChild(m);
    });

    var parte = d.createDocumentFragment();
    [].slice.call(x.body.childNodes).forEach(function (n) { parte.appendChild(d.importNode(n, true)); });
    var ghl = d.getElementById('__nuxt');
    d.body.insertBefore(parte, ghl && ghl.parentNode === d.body ? ghl : d.body.firstChild);

    var lista = d.querySelectorAll('script[type="text/tcd-espera"]');
    (function siguiente(k) {
      if (k < lista.length) return correr(lista[k], function () { siguiente(k + 1); });
      listo(titulo);
    })(0);
  }

  function listo(titulo) {
    carga.listo = Math.round(performance.now());
    d.documentElement.setAttribute('data-tcd-pagina', pagina);
    if (location.hash) {
      try {
        var meta = d.getElementById(decodeURIComponent(location.hash.slice(1)));
        if (meta) meta.scrollIntoView();
      } catch (e) {}
    }
    if (titulo) {
      var programado = false;
      var poner = function () {
        programado = false;
        if (d.title !== titulo) d.title = titulo;
      };
      var agendar = function () {
        if (programado || d.title === titulo) return;
        programado = true;
        w.requestAnimationFrame ? w.requestAnimationFrame(poner) : setTimeout(poner, 0);
      };
      try {
        new MutationObserver(agendar).observe(d.head, { childList: true, subtree: true, characterData: true });
      } catch (e) {}
      w.addEventListener('load', agendar);
    }
  }

  function aviso() {
    carga.error = 1;
    tapa.textContent += 'body:before{content:"La página se está actualizando. Vuelve a abrirla en un momento.";display:block;font:20px/1.5 Georgia,serif;color:#2B2622;text-align:center;margin:30vh 24px 0}';
  }

  primera().then(conLetra).then(montar).catch(aviso);
})(document, window);