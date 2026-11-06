import os,re,base64
I='/home/claude/eco/imgs/'
def imgs(s):
    ks=sorted(set(re.findall(r'data-img="([^"]+)"',s)))
    m={k:'data:image/webp;base64,'+base64.b64encode(open(I+k,'rb').read()).decode() for k in ks if os.path.exists(I+k)}
    return '<script>window.TCD_IMGS='+__import__('json').dumps(m)+';</script>'
css=open('src/base.css').read(); cfg=open('src/config.js').read(); js=open('src/base.js').read()
os.makedirs('dist',exist_ok=True)
for f in sorted(p.stem for p in __import__('pathlib').Path('pages').glob('*.html')):
    s=open('pages/%s.html'%f).read()
    s=s.replace('<style>/*BASE_CSS*/</style>','<style>\n'+css+'\n</style>\n<script>\n'+cfg+'\n</script>',1)
    s=s.replace('<script>/*BASE_JS*/</script>',imgs(s)+'\n<script>\n'+js+'\n</script>',1)
    assert '/*BASE' not in s
    open('dist/%s.html'%f,'w').write(s)
    print(f, len(s))
