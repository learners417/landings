import sys
from PIL import Image
import numpy as np
def runs(path, x0=0, x1=1080, thr=40, bg=None, minrun=1):
    im=np.asarray(Image.open(path).convert('RGB')).astype(int)
    reg=im[:, x0:x1]
    if bg is None:
        bg=reg[5, 5]
    d=np.abs(reg-np.array(bg)).sum(axis=2)
    rows=(d>thr).sum(axis=1)
    out=[];start=None
    for y,v in enumerate(rows):
        if v>0 and start is None: start=y
        if v==0 and start is not None:
            out.append((start,y-1)); start=None
    if start is not None: out.append((start,len(rows)-1))
    return bg, out
if __name__=='__main__':
    p=sys.argv[1]; x0=int(sys.argv[2]) if len(sys.argv)>2 else 0; x1=int(sys.argv[3]) if len(sys.argv)>3 else 1080
    bg,o=runs(p,x0,x1)
    print('bg',bg)
    for a,b in o: print(a,b,b-a+1)
