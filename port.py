import re,sys
SRC='/home/claude/zipsrc/paginas-libros/'
CAP='https://libros.tuclinica.digital/capitulo/'
def port(path, pagos):
    s=open(SRC+path).read()
    s=s.replace('<link rel="icon" href="../a/img/icono.svg" type="image/svg+xml">','')
    s=s.replace('<link rel="stylesheet" href="../a/base.css">','<style>/*BASE_CSS*/</style>')
    # imágenes
    s=re.sub(r'\s+srcset="[^"]*"\s+sizes="[^"]*"','',s)
    s=re.sub(r'src="\.\./a/([^"]+)"',r'data-img="\1"',s)
    # links internos
    s=re.sub(r'href="\.\./capitulo/([a-z]+)/index\.html"',lambda m:'href="%s%s/index.html"'%(CAP,m.group(1)),s)
    s=s.replace('href="../capitulo/index.html"','data-link="capitulo" href="%sindex.html"'%CAP)
    s=re.sub(r'href="\.\./libros/index\.html#([a-z]+)"',r'data-link="libros" data-hash="#\1" href="#"',s)
    s=s.replace('href="../libros/index.html"','data-link="libros" href="#"')
    s=s.replace('href="../el-numero/index.html"','data-link="numero" href="#"')
    s=re.sub(r'href="\.\./descargas-7q4k/([^"]+)"',r'data-desc="\1" href="#"',s)
    # scripts
    s=s.replace('<script src="../a/config.js"></script>','')
    s=s.replace('<script src="../a/base.js"></script>','<script>/*BASE_JS*/</script>')
    s=s.replace('<body data-pagina=','<body data-pagos="%s" data-pagina='%pagos)
    return s
open('pages/libros.html','w').write(port('libros/index.html','obra numero lago sanadores'))
open('pages/el-numero.html','w').write(port('el-numero/index.html','numero obra'))
open('pages/gracias.html','w').write(port('gracias-7q4k/index.html',''))
for f in ['libros','el-numero','gracias']:
    s=open('pages/%s.html'%f).read()
    print(f, re.findall(r'(?:href|src)="\.\./[^"]*"',s)[:5])
