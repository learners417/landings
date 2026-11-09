/* Clarity (Microsoft): grabaciones y mapas de calor, proyecto en config.js.
   Si la página ya trae Clarity (el código de seguimiento de GHL), no se carga dos veces.
   Se mira el script de Clarity y no solo window.clarity: alguien puede dejar la cola armada
   sin cargarlo, y entonces sí hay que cargarlo. En las vistas previas no se carga. */
(function (w, d, id) {
  if (!id || ((w.__tcdCarga || {}).rama || 'main') !== 'main' || /claude\.ai|claudeusercontent|localhost|^file:/.test(location.href)) return;
  if (d.querySelector('script[src*="clarity.ms/"]')) return;
  w.clarity = w.clarity || function () { (w.clarity.q = w.clarity.q || []).push(arguments); };
  var s = d.createElement('script');
  s.async = true;
  s.src = 'https://www.clarity.ms/tag/' + id;
  (d.head || d.documentElement).appendChild(s);
})(window, document, (window.TCD || {}).clarity);
