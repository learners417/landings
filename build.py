import os,re,base64,json,pathlib,sys
# Las imágenes viven en este repo. La ruta salía clavada a mano
# (/home/claude/eco/imgs/) y el `if os.path.exists` de abajo hacía que, clonado
# en cualquier otra carpeta, el build se armara igual y SIN NINGUNA IMAGEN:
# 34 páginas publicadas con las tapas vacías y ningún error. Ahora la ruta sale
# del repo, y lo que falte se avisa en pantalla y corta el build.
I=os.path.join(os.path.dirname(os.path.abspath(__file__)),'imgs')+os.sep
FALTAN=[]
def imgs(s):
    # las imágenes van dentro de la página: data-img (las <img>) y data-tapa (los lomos del estante)
    ks=sorted(set(re.findall(r'data-(?:img|tapa)="([^"]+)"',s)))
    for k in ks:
        if not os.path.exists(I+k) and k not in FALTAN: FALTAN.append(k)
    m={k:'data:image/webp;base64,'+base64.b64encode(open(I+k,'rb').read()).decode() for k in ks if os.path.exists(I+k)}
    return '<script>window.TCD_IMGS='+json.dumps(m)+';</script>'
css=open('src/base.css').read(); cfg=open('src/config.js').read(); js=open('src/base.js').read(); cla=open('src/clarity.js').read()
ecss=open('src/edicion.css').read(); ejs=open('src/edicion.js').read(); estante=open('src/estante.html').read()
pcss=open('src/paisaje.css').read(); vcss=open('src/vivo.css').read(); vjs=open('src/vivo.js').read(); pjs=open('src/paisaje.js').read()   # la piel Paisaje (14 nov 2026)
cabeza='<script>\n'+cfg+'\n</script>\n<script>\n'+cla+'\n</script>'
# Paisaje vivo sobre la Edición (16 nov 2026): lo que se mira pasa a Manrope y las versalitas a letra normal.
# Cormorant queda solo para lo que se cita (frases, poemas, dedicatorias, la firma).
CITA=re.compile(r'blockquote|cita|epigrafe|poema|dedi|firma|frase')
def a_paisaje(c):
    def regla(m):
        sel,cuerpo=m.group(1),m.group(2)
        if sel.strip().startswith('@') or ':root' in sel: return m.group(0)
        tit=('var(--f-titulo)' in cuerpo) or ('Cormorant' in cuerpo and 'font-family' in cuerpo)
        if tit:
            if CITA.search(sel):
                cuerpo=cuerpo.replace('var(--f-titulo)','var(--f-cita)')
            else:
                cuerpo=re.sub(r'font-family:[^;}]*','font-family:var(--vista)',cuerpo)
                cuerpo=cuerpo.replace('font-style:italic','font-style:normal')
                cuerpo=re.sub(r'font-weight:(?:400|500|600)\b','font-weight:700',cuerpo)
                if 'font-weight' not in cuerpo: cuerpo+=';font-weight:700'
                if 'letter-spacing' not in cuerpo: cuerpo+=';letter-spacing:-.02em'
        if 'uppercase' in cuerpo and not CITA.search(sel):
            cuerpo=cuerpo.replace('text-transform:uppercase','text-transform:none')
            cuerpo=re.sub(r'letter-spacing:\s*\.?\d*\.?\d+em','letter-spacing:0',cuerpo)
            cuerpo=re.sub(r'font-family:[^;}]*','font-family:var(--vista)',cuerpo)
            if 'font-family' not in cuerpo: cuerpo+=';font-family:var(--vista)'
            cuerpo=re.sub(r'font-weight:(?:400|500|600)\b','font-weight:700',cuerpo)
            if 'font-weight' not in cuerpo: cuerpo+=';font-weight:700'
        if not CITA.search(sel):
            # en Paisaje la letra no se espacia: sin versalitas no hace falta aire entre letras
            cuerpo=re.sub(r'letter-spacing:\s*\.(?:0[5-9]|[1-9])\d*em','letter-spacing:0',cuerpo)
        if re.search(r'\bbtn\b',sel):
            # los botones son redondos y sin el doble filete de la Edición
            cuerpo=re.sub(r'box-shadow:\s*inset[^;}]*','box-shadow:none'+(' !important' if 'box-shadow' in cuerpo and '!important' in cuerpo.split('box-shadow',1)[1].split(';',1)[0] else ''),cuerpo)
            cuerpo=re.sub(r'border-radius:\s*\d+px','border-radius:999px',cuerpo)
        return sel+'{'+cuerpo+'}'
    return re.sub(r'([^{}]+)\{([^{}]*)\}',regla,c)
os.makedirs('dist',exist_ok=True)
for f in sorted(p.stem for p in pathlib.Path('pages').glob('*.html')):
    s=open('pages/%s.html'%f).read()
    s=s.replace('<!--ESTANTE-->',estante)
    # el precio en los botones: en el celular baja a su propia línea («Quiero Tu nuevo precio» / «97 USD»), nunca se parte
    if f!='gracias': s=re.sub(r' · <span data-precio="(\w+)">(\d+)</span> USD',r'<span class="pr"><span class="sep"> · </span><span data-precio="\1">\2</span>&nbsp;USD</span>',s)
    if '/*PAISAJE_CSS*/' in s:   # la piel Paisaje de Tu Clínica Digital (14 nov 2026): las imágenes van por jsDelivr, no dentro de la página
        s=s.replace('<style>/*PAISAJE_CSS*/</style>','<style>\n'+pcss+'\n</style>\n'+cabeza,1)
        s=s.replace('<script>/*PAISAJE_JS*/</script>','<script>\n'+js+'\n</script>\n<script>\n'+pjs+'\n</script>',1)
        for k in re.findall(r'data-repo="([^"]+)"',s):
            if not os.path.exists(os.path.join(os.path.dirname(I.rstrip(os.sep)),k)) and k not in FALTAN: FALTAN.append(k)
    elif '/*EDICION_CSS*/' in s:   # la Edición Libres (9 nov 2026) vestida de Paisaje vivo (16 nov 2026)
        s=s.replace('<style>/*EDICION_CSS*/</style>','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400..800&display=swap">\n<style>\n'+ecss+'\n'+vcss+'\n</style>\n'+cabeza,1)
        if f!='clinica-del-lider':   # La Clínica del Líder es otra marca (para líderes): conserva «Javo Katz»
            s=re.sub(r'(<a class="marca"[^>]*>)\s*Javo Katz\s*</a>', r'\1<span class="lomos" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>Tu Clínica Digital</a>', s)
        s=s.replace('Compuesto en Cormorant Garamond y Literata.','Compuesto en Manrope y Literata.')
        s=re.sub(r'<style>(.*?)</style>', lambda m: '<style>'+a_paisaje(m.group(1))+'</style>', s, flags=re.S)
        s=s.replace('<script>/*EDICION_JS*/</script>',imgs(s)+'\n<script>\n'+js+'\n</script>\n<script>\n'+ejs+'\n</script>\n<script>\n'+vjs+'\n</script>',1)
    else:
        s=s.replace('<style>/*BASE_CSS*/</style>','<style>\n'+css+'\n</style>\n'+cabeza,1)
        s=s.replace('<script>/*BASE_JS*/</script>',imgs(s)+'\n<script>\n'+js+'\n</script>',1)
    assert '/*BASE' not in s and '/*EDICION' not in s and '/*PAISAJE' not in s, f
    open('dist/%s.html'%f,'w').write(s)
    print(f, len(s))

# Una imagen que falta no se publica en silencio: el build corta acá.
if FALTAN:
    print('\nFALTAN %d imagen(es) en %s:' % (len(FALTAN), I))
    for k in FALTAN: print('  ·', k)
    sys.exit(1)
