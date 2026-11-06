import sys,os,json
from playwright.sync_api import sync_playwright
F='/home/claude/fonts/node_modules/@fontsource/'
css=''
for w,st in [(500,'normal'),(600,'normal'),(500,'italic'),(600,'italic')]:
    css+="@font-face{font-family:'Cormorant Garamond';font-weight:%d;font-style:%s;src:url('file://%scormorant-garamond/files/cormorant-garamond-latin-%d-%s.woff2')}"%(w,st,F,w,st)
for w in (500,600,700,800):
    css+="@font-face{font-family:'Manrope';font-weight:%d;src:url('file://%smanrope/files/manrope-latin-%d-normal.woff2')}"%(w,F,w)
def route(r):
    u=r.request.url
    return r.continue_() if u.startswith(('file:','data:')) else r.abort()
JS="""(()=>{const r=[];document.querySelectorAll('body *').forEach(e=>{if(e.closest('.tel,.mini-app,.pant,[aria-hidden=true] svg'))return;const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());if(!t)return;const cs=getComputedStyle(e);if(cs.display=='none'||cs.visibility=='hidden')return;const s=parseFloat(cs.fontSize);if(s<16)r.push(e.tagName+'.'+(typeof e.className=='string'?e.className:'svg')+' '+s+'px «'+e.textContent.trim().slice(0,40)+'»')});
document.querySelectorAll('svg text').forEach(t=>{const k=t.getBoundingClientRect();const fs=parseFloat(getComputedStyle(t).fontSize);const svg=t.ownerSVGElement;const vb=svg.viewBox.baseVal;const sc=vb&&vb.width?svg.getBoundingClientRect().width/vb.width:1;if(fs*sc<16)r.push('svg text '+(fs*sc).toFixed(1)+'px «'+t.textContent.trim().slice(0,30)+'»')});return [...new Set(r)].slice(0,40)})()"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for f in sys.argv[2:]:
        pg=b.new_page(viewport={'width':int(sys.argv[1]),'height':900}); errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)[:120]))
        pg.route('**/*',route); pg.goto('file://'+os.path.abspath(f)); pg.add_style_tag(content=css)
        pg.evaluate("document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))"); pg.wait_for_timeout(800)
        print('==',os.path.basename(f),'errores:',errs); print('\n'.join(pg.evaluate(JS)))
        pg.close()
    b.close()
