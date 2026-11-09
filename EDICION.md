# Edición Libres · la piel nueva de las páginas (9 nov 2026)

Pedido de Javo (8 nov, 22:00): «máxima versión final, diseño propio, que no sea otra landing prefabricada,
acorde a los libros, a mi voz, con la autoridad y los casos; y bien cableadas todas las landings».

## La idea
La página es un libro de la colección. Tiene portadilla, índice, capítulos, láminas y colofón.
Cada página tiene un objeto que se toca (el estante, el mapa, la cuenta, la tapa).

## Lo que no cambia (es de Javo)
Papel, tinta y un hilo de oro (1 px). Cormorant Garamond para titular. 16 px como piso.
Sin negro de fondo, sin degradés, sin brillos. Tuteo neutro. Un botón por página.

## Lo que cambia (y por qué)
- Texto en Literata (la letra de los libros que se leen en el teléfono) en lugar de Manrope:
  la página se lee como uno de sus libros.
- Fuera los tics de página hecha por IA: la etiqueta en mayúsculas arriba de cada título, la palabra
  en cursiva dorada dentro del título, la flecha en cada botón, las tarjetas iguales con la misma sombra
  y el «aparecer al bajar» en cada bloque.
- En su lugar: número de capítulo (solo donde hay orden), título y subtítulo como en un libro,
  cabecera corriente con el capítulo en que estás, índice con puntos guía, láminas, colofón.
- Un solo movimiento orquestado por página (en /libros: los 8 libros se acomodan en el estante).
- El botón es el único objeto oscuro de la página: rectángulo de esquinas suaves con filete de oro adentro.
- La única tarjeta de la página es la oferta (la ficha), con puntos guía.

## Tokens
papel #F4EEE3 · papel-claro #FBF8F1 · papel-hondo #EDE5D6 · tinta #2B2724 · tinta-suave #5A534A
linea #DCD2C1 · hilo #A8875A (solo 1 px) · oro-texto #7A5F33 · verde #2F5638 · rojo #9C3626
Lomos (de las tapas): sanadores #F2EFE7/#344B48 · lago #2B4E68 · montaña #904932 · viento #B48B3F
río #418D93 · bosque #294637 · héroe #F5EFE5 · libertades #E6E1D5

## Archivos
src/edicion.css (la piel) · src/edicion.js (cabecera, índice, estante) · build.py inyecta
EDICION_CSS / EDICION_JS en las páginas que los piden; las demás siguen con base.css.
