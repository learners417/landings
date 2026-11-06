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
  var ALIAS = { '': 'inicio' };
  var ruta = location.pathname.replace(/^\/+|\/+$/g, '').toLowerCase();
  var pagina = w.TCD_PAGINA || (ruta in ALIAS ? ALIAS[ruta] : ruta);
  var archivo = '/site/' + pagina + '.html';
  var FUENTES = [
    'https://cdn.jsdelivr.net/gh/' + REPO + '@main' + archivo,
    'https://raw.githubusercontent.com/' + REPO + '/main' + archivo
  ];
  var carga = w.__tcdCarga = { pagina: pagina, inicio: Math.round(performance.now()) };

  /* La tapa: oculta lo visible de GHL mientras llega la página. */
  var tapa = d.getElementById('tcd-tapa');
  if (!tapa) {
    tapa = d.createElement('style');
    tapa.id = 'tcd-tapa';
    tapa.textContent = '#__nuxt,#teleports{display:none!important}html{background:#F4EEE3}';
    d.head.appendChild(tapa);
  }

  function traer(url, ms) {
    return new Promise(function (ok, no) {
      var reloj = setTimeout(function () { no('tiempo'); }, ms);
      fetch(url, { cache: 'no-cache' })
        .then(function (r) { if (!r.ok) throw r.status; return r.text(); })
        .then(function (t) { clearTimeout(reloj); carga.fuente = url; ok(t); },
              function (e) { clearTimeout(reloj); no(e); });
    });
  }
  function primera(i) {
    if (i >= FUENTES.length) return Promise.reject('sin fuente');
    return traer(FUENTES[i], i ? 9000 : 6000).catch(function () { return primera(i + 1); });
  }

  /* Los estilos de GHL quedan apagados: la página trae los suyos. */
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
        cambios.forEach(function (c) { [].forEach.call(c.addedNodes, function (n) { if (esDeGHL(n)) apagar(n); }); });
      }).observe(d.head, { childList: true });
    } catch (e) {}
  }

  function copiarAtributos(de, a) {
    for (var i = 0; i < de.attributes.length; i++) a.setAttribute(de.attributes[i].name, de.attributes[i].value);
  }

  /* Un script nuevo con lo mismo: los que vienen del texto no corren solos. */
  function correr(viejo, sigue) {
    var s = d.createElement('script');
    for (var i = 0; i < viejo.attributes.length; i++) {
      var nombre = viejo.attributes[i].name;
      if (nombre !== 'type' && nombre !== 'data-tipo') s.setAttribute(nombre, viejo.attributes[i].value);
    }
    var tipo = viejo.getAttribute('data-tipo');
    if (tipo) s.type = tipo;
    if (viejo.getAttribute('src')) {
      s.async = false;
      s.onload = s.onerror = sigue;
      viejo.parentNode.replaceChild(s, viejo);
    } else {
      s.text = viejo.text;
      viejo.parentNode.replaceChild(s, viejo);
      sigue();
    }
  }

  function montar(html) {
    var x = new DOMParser().parseFromString(html, 'text/html');
    var titulo = x.title;

    /* Los scripts esperan hasta que la página entera esté puesta. */
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
      try { var meta = d.getElementById(decodeURIComponent(location.hash.slice(1))); if (meta) meta.scrollIntoView(); } catch (e) {}
    }
    /* GHL puede reescribir el título al terminar de cargar: vuelve el de la página. */
    if (titulo) {
      var poner = function () { if (d.title !== titulo) d.title = titulo; };
      try { new MutationObserver(poner).observe(d.head, { childList: true, subtree: true, characterData: true }); } catch (e) {}
      w.addEventListener('load', poner);
    }
  }

  function aviso() {
    carga.error = 1;
    tapa.textContent += 'body:before{content:"La página se está actualizando. Vuelve a abrirla en un momento.";display:block;font:20px/1.5 Georgia,serif;color:#2B2622;text-align:center;margin:30vh 24px 0}';
  }

  primera(0).then(montar).catch(aviso);
})(document, window);
