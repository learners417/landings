"""Errores seguros de la agenda y la preparación, según el estándar.
No toca el mensaje: nombre público, nada bajo 16 px y el sello legible. Se puede correr varias veces."""
import pathlib, re

D = pathlib.Path('/home/claude/eco/dist')

def fix(nombre, cambios):
    p = D / nombre
    s = p.read_text()
    antes = s
    for a, b in cambios:
        if b.startswith(a) and b in s:
            continue  # una inserción que ya está
        s = s.replace(a, b)
    # nada por debajo de 16 px
    s = s.replace('font-size:15px', 'font-size:16px')
    p.write_text(s)
    print(nombre, 'cambió' if s != antes else 'sin cambios',
          '| Javier:', s.count('Javier Katz'), '| 15px:', s.count('font-size:15px'))

fix('agenda.html', [
    ('alt="Javier Katz en un rodaje con una clienta"', 'alt="Javo Katz en un rodaje con una clienta"'),
    ('alt="Javier Katz"', 'alt="Javo Katz"'),
    ('<p class="fn">Javier Katz</p>', '<p class="fn">Javo Katz</p>'),
    ('<p class="foot-brand">Javier Katz · Tu Clínica Digital</p>', '<p class="foot-brand">Javo Katz · Tu Clínica Digital</p>'),
    # el sello: más grande y con su texto a 16 px
    ('.sello{position:relative;z-index:3;width:124px;height:124px;margin:-62px auto 0}',
     '.sello{position:relative;z-index:3;width:168px;height:168px;margin:-84px auto 0}'),
    ('.sello text{font-family:var(--fd);font-weight:600;font-size:8.2px;letter-spacing:.06em;fill:var(--gold)}',
     '.sello text{font-family:var(--fd);font-weight:600;font-size:11.5px;letter-spacing:.06em;fill:var(--gold)}'),
    ('.sello text{font-family:var(--fb);font-weight:700;font-size:7.4px;letter-spacing:.1em}',
     '.sello text{font-family:var(--fb);font-weight:700;font-size:11.5px;letter-spacing:.1em}'),
    ('GARANTÍA DE RESULTADOS · 90 DÍAS · 5 SISTEMAS ·', 'GARANTÍA DE RESULTADOS · 90 DÍAS ·'),
    # la marca de la barra en una sola línea: en el teléfono no tapa la línea de profesiones
    ('.tb-marca small{display:block;font-family:var(--fb);font-size:16px;letter-spacing:.12em;color:var(--gold);font-weight:700;margin-top:2px;text-transform:none}\n',
     '.tb-marca small{display:block;font-family:var(--fb);font-size:16px;letter-spacing:.12em;color:var(--gold);font-weight:700;margin-top:2px;text-transform:none}\n'
     '/* marca en una línea */.tb-marca{white-space:nowrap}\n'
     '@media (max-width:520px){ .tb-marca{font-size:19px!important;letter-spacing:.14em} .tb-marca small{display:none} }\n'
     '@media (max-width:400px){ .topbar .tb-in{gap:10px;padding:9px 12px} .tb-marca{font-size:17px!important;letter-spacing:.1em} .tb-btn{padding:11px 14px!important} }\n'),
])

fix('preparacion.html', [
    ('<title>Espera: te falta un paso · Javier Katz</title>', '<title>Espera: te falta un paso · Javo Katz</title>'),
    ('<p class="marca">Javier Katz</p>', '<p class="marca">Javo Katz</p>'),
    ('<p class="foot-brand">Javier Katz · Tu Clínica Digital</p>', '<p class="foot-brand">Javo Katz · Tu Clínica Digital</p>'),
    # la palabra de la casa: diagnóstico
    ('antes de la llamada', 'antes de tu diagnóstico'),
    ('Te espero en la llamada.', 'Te espero en tu diagnóstico.'),
    ('súmalo a la llamada', 'súmalo al diagnóstico'),
    ('Antes de la llamada', 'Antes de tu diagnóstico'),
    ('llegas a la llamada', 'llegas a tu diagnóstico'),
    ('>La llamada<', '>Tu diagnóstico<'),
])
