# Las landings de Javo Katz · Tu Clínica Digital

Aquí se guarda y se arma el código de las páginas. Las páginas viven en GHL (tuclinica.digital/ruta),
con sus calendarios, formularios y automatizaciones: cada una es un bloque «Código personalizado»
con el archivo de `site/` que lleva su nombre. Claude lo carga en GHL desde la sesión de Javo.

## Cómo se corrige y se sube
1. Se edita la fuente: `pages/*.html` (las páginas), `src/` (la piel común y `config.js`:
   rutas, precios, links de pago, WhatsApp, píxel), `fijas/` (la agenda y la preparación).
2. Se arma: `python3 build.py && python3 publicar.py` (de `pages/` a `dist/`, y todo a `site/`).
3. Se revisa: `python3 chico.py 390 dist/*.html` (errores y letra menor a 16 px).
4. Push a `main`, y se carga en GHL el archivo de `site/` de cada página que cambió.

## Una página nueva
1. `pages/<ruta>.html` → armar → push.
2. En GHL: página nueva con esa ruta exacta, un bloque «Código personalizado» a ancho completo
   con `site/<ruta>.html`, y el título y la descripción en la configuración SEO.

## Qué hay en cada carpeta
- `pages/` · las páginas · `src/` · base.css, base.js, config.js · `imgs/` · tapas e imágenes (van dentro de cada página)
- `fijas/` · agenda, preparación y la capa del generador (`/generador-pp` conserva su código; la capa se pega debajo)
- `tools.py` · arma las 6 páginas de herramientas · `port_capitulos.py` · arma los capítulos
- `panel.py` · el panel de montaje manual (respaldo) · `site/` · lo que va a GHL (no se edita a mano)

## Reglas del estándar
Letra de 16 px o más · papel, sin fondo negro, sin degradés ni brillos · oro solo en líneas de 1 px,
versalitas y numerales · castellano neutro, tuteo · nunca «gente» ni «gratis» · sin señales de falta de
dinero · datos con su fuente · sin emojis.
