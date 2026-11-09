import os,re,base64,json,pathlib
I='/home/claude/eco/imgs/'
def imgs(s):
    # las imágenes van dentro de la página: data-img (las <img>) y data-tapa (los lomos del estante)
    ks=sorted(set(re.findall(r'data-(?:img|tapa)="([^"]+)"',s)))
    m={k:'data:image/webp;base64,'+base64.b64encode(open(I+k,'rb').read()).decode() for k in ks if os.path.exists(I+k)}
    return '<script>window.TCD_IMGS='+json.dumps(m)+';</script>'
css=open('src/base.css').read(); cfg=open('src/config.js').read(); js=open('src/base.js').read(); cla=open('src/clarity.js').read()
ecss=open('src/edicion.css').read(); ejs=open('src/edicion.js').read(); estante=open('src/estante.html').read()
cabeza='<script>\n'+cfg+'\n</script>\n<script>\n'+cla+'\n</script>'
os.makedirs('dist',exist_ok=True)
for f in sorted(p.stem for p in pathlib.Path('pages').glob('*.html')):
    s=open('pages/%s.html'%f).read()
    s=s.replace('<!--ESTANTE-->',estante)
    # el precio en los botones: en el celular baja a su propia línea («Quiero Tu nuevo precio» / «97 USD»), nunca se parte
    if f!='gracias': s=re.sub(r' · <span data-precio="(\w+)">(\d+)</span> USD',r'<span class="pr"><span class="sep"> · </span><span data-precio="\1">\2</span>&nbsp;USD</span>',s)
    if '/*EDICION_CSS*/' in s:   # la piel de la Edición Libres (9 nov 2026)
        s=s.replace('<style>/*EDICION_CSS*/</style>','<style>\n'+ecss+'\n</style>\n'+cabeza,1)
        s=s.replace('<script>/*EDICION_JS*/</script>',imgs(s)+'\n<script>\n'+js+'\n</script>\n<script>\n'+ejs+'\n</script>',1)
    else:
        s=s.replace('<style>/*BASE_CSS*/</style>','<style>\n'+css+'\n</style>\n'+cabeza,1)
        s=s.replace('<script>/*BASE_JS*/</script>',imgs(s)+'\n<script>\n'+js+'\n</script>',1)
    assert '/*BASE' not in s and '/*EDICION' not in s, f
    open('dist/%s.html'%f,'w').write(s)
    print(f, len(s))
