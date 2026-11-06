# Las landings de Javo Katz · Tu Clínica Digital

Aquí se guarda y se arma el código de las páginas. Las páginas viven en GHL (tuclinica.digital/ruta),
con sus calendarios, formularios, estadísticas y automatizaciones.

## Cómo llega cada página a GHL
Cada página de GHL tiene un solo bloque «Código personalizado» con una línea: `ghl-linea.html`.
Es la misma línea en todas. Esa línea trae `cargador.js`, y el cargador trae `site/<ruta>.html`
(la ruta de GHL decide el archivo: `/impostor` → `site/impostor.html`) y la monta dentro de la
página de GHL. GHL sigue haciendo lo suyo por detrás: estadísticas del embudo, atribución,
formularios y calendarios.

- Fuente principal: jsDelivr (`cdn.jsdelivr.net/gh/learners417/landings@main/...`). Respaldo: GitHub.
- La página se ve igual que sola: el cargador apaga los estilos de GHL y corre los scripts en orden.
- El píxel de TCD recibe sus eventos solo (`trackSingle`), aunque GHL tenga otro píxel en la página.

## Cómo se corrige y se sube
1. Se edita la fuente: `pages/*.html` (las páginas), `src/` (la piel común y `config.js`:
   rutas, precios, links de pago, WhatsApp, píxel), `fijas/` (la agenda y la preparación).
2. Se arma: `python3 build.py && python3 publicar.py` (de `pages/` a `dist/`, y todo a `site/`).
3. Se revisa: `python3 chico.py 390 dist/*.html` (errores y letra menor a 16 px).
4. Push a `main` y se purga jsDelivr de cada archivo que cambió:
   `https://purge.jsdelivr.net/gh/learners417/landings@main/site/<ruta>.html`.
   En un minuto está en vivo. GHL no se toca.

## Una página nueva
1. `pages/<ruta>.html` → armar → push → purga.
2. En GHL: se clona un paso que ya tenga la línea y se le pone la ruta exacta. Título y descripción
   en la configuración SEO del paso (es lo que muestran WhatsApp y Facebook al compartir).

## Qué hay en cada carpeta
- `pages/` · las páginas · `src/` · base.css, base.js, config.js · `imgs/` · tapas e imágenes (van dentro de cada página)
- `fijas/` · agenda, preparación y la capa del generador (`/generador-pp` conserva su código; la capa va debajo)
- `tools.py` · arma las 6 páginas de herramientas · `port_capitulos.py` · arma los capítulos
- `cargador.js` y `ghl-linea.html` · cómo llegan las páginas a GHL
- `panel.py` · el panel de montaje manual (respaldo) · `site/` · lo que sirve el cargador (no se edita a mano)

## Reglas del estándar
Letra de 16 px o más · papel, sin fondo negro, sin degradés ni brillos · oro solo en líneas de 1 px,
versalitas y numerales · castellano neutro, tuteo · nunca «gente» ni «gratis» · sin señales de falta de
dinero · datos con su fuente · sin emojis.
