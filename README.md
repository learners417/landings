# Las landings de Javo Katz · Tu Clínica Digital

Las páginas viven aquí. Vercel publica la carpeta `site/`, y cada página de GHL
(tuclinica.digital/ruta) trae su contenido desde ahí con una sola línea: el cargador.
Cuando se corrige una página, se arma y se sube; en un minuto está en vivo. En GHL no se toca nada.

## Cómo se corrige y se sube
1. Se edita la fuente: `pages/*.html` (las páginas), `src/` (la piel común y `config.js`:
   rutas, precios, links de pago, WhatsApp, píxel), `fijas/` (la agenda y la preparación).
2. Se arma: `python3 build.py && python3 publicar.py` (de `pages/` a `dist/`, y todo a `site/`).
3. Se revisa: `python3 chico.py 390 dist/*.html` (errores y letra menor a 16 px).
4. Push a `main`. Vercel publica solo.

## Una página nueva
1. `pages/<ruta>.html` → armar → push.
2. En GHL: página nueva con esa ruta exacta y un bloque «Código personalizado» con el
   contenido de `cargador-ghl.html`. Es el mismo para todas las páginas.

## Qué hay en cada carpeta
- `pages/` · las páginas · `src/` · base.css, base.js, config.js · `imgs/` · tapas e imágenes (van dentro de cada página)
- `fijas/` · agenda, preparación y la capa del generador (`/generador-pp` conserva su código; la capa se pega debajo)
- `tools.py` · arma las 6 páginas de herramientas · `port_capitulos.py` · arma los capítulos
- `panel.py` · el panel de montaje manual (respaldo) · `site/` · lo que se publica (no se edita a mano)

## Reglas del estándar
Letra de 16 px o más · papel, sin fondo negro, sin degradés ni brillos · oro solo en líneas de 1 px,
versalitas y numerales · castellano neutro, tuteo · nunca «gente» ni «gratis» · sin señales de falta de
dinero · datos con su fuente · sin emojis.
