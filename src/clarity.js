/* Clarity (Microsoft): grabaciones y mapas de calor, proyecto en config.js.
   Si la página ya lo trae (el código de seguimiento de GHL), no se carga dos veces.
   En las vistas previas no se carga. */
(function (w, d, id) {
  if (!id || w.clarity || /claude\.ai|claudeusercontent|localhost|^file:/.test(location.href)) return;
  w.clarity = function () { (w.clarity.q = w.clarity.q || []).push(arguments); };
  var s = d.createElement('script');
  s.async = true;
  s.src = 'https://www.clarity.ms/tag/' + id;
  (d.head || d.documentElement).appendChild(s);
})(window, document, (window.TCD || {}).clarity);
