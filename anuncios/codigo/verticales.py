# Verticales de P1 y P2: el texto de abajo sube fuera de la zona que tapan
# historias y reels (cuenta, botón y texto del anuncio: ~18-20 % de abajo).
import os
import cv2
import numpy as np
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__))


def load(n):
    return np.asarray(Image.open(os.path.join(D, n + '.png')).convert('RGB')).astype(np.float64)


def lift_layer(img, y0, y1, x0, x1, thr=18, open_k=31, keep=None, extra=None):
    """Separa lo claro (texto, íconos, líneas) del fondo en la caja dada.
    Devuelve (fondo sin texto de toda la imagen, alfa, color) de la caja."""
    reg = img[y0:y1, x0:x1]
    L = reg.mean(axis=2)
    # fondo sin trazos: apertura (mínimo y máximo) con un núcleo más ancho que la letra
    k = np.ones((open_k, open_k), np.uint8)
    base = cv2.dilate(cv2.erode(L.astype(np.uint8), k), k).astype(np.float64)
    base = cv2.GaussianBlur(base, (0, 0), 6)
    mask = ((L - base) > thr).astype(np.uint8) * 255
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=1)
    if keep is not None:                 # zonas que no son texto (p. ej. la camisa)
        mask = np.where(keep[y0:y1, x0:x1], 0, mask).astype(np.uint8)
    full_mask = np.zeros(img.shape[:2], np.uint8)
    full_mask[y0:y1, x0:x1] = mask
    if extra is not None:                # se borra sin levantar (restos de línea sobre la camisa)
        full_mask = np.maximum(full_mask, extra)
    clean = cv2.inpaint(img.clip(0, 255).astype(np.uint8), full_mask, 7, cv2.INPAINT_TELEA).astype(np.float64)
    B = clean[y0:y1, x0:x1]
    I = reg
    a = np.max((I - B) / np.maximum(255.0 - B, 1.0), axis=2)
    a = np.where(mask > 0, a, 0.0).clip(0, 1)
    F = np.where(a[..., None] > 0.02, (I - (1 - a[..., None]) * B) / np.maximum(a[..., None], 0.02), 255.0)
    return clean, a, F.clip(0, 255)


def comp(base, a, F, x, y):
    h, w = a.shape
    seg = base[y:y + h, x:x + w]
    base[y:y + h, x:x + w] = a[..., None] * F + (1 - a[..., None]) * seg
    return base


def save(arr, name):
    Image.fromarray(arr.round().clip(0, 255).astype(np.uint8)).save(os.path.join(D, name))


# ---------------- P1: «Yo, todo lo demás.» y la bajada suben 170 px
img = load('post-1-vertical')
y0, y1, x0, x1 = 1415, 1725, 60, 1020
clean, a, F = lift_layer(img, y0, y1, x0, x1)
navy = img[1850:1900, :, :].reshape(-1, 3).mean(0)
H, W = img.shape[:2]
ramp = np.zeros(H)
for yy in range(H):
    t = np.clip((yy - 1040) / (1500 - 1040), 0, 1)
    ramp[yy] = t * t * (3 - 2 * t)          # suave, llega a azul pleno en 1500
out = clean * (1 - ramp[:, None, None]) + navy[None, None, :] * ramp[:, None, None]
dy = -170
out = comp(out, a, F, x0, y0 + dy)
save(out, 'post-1-vertical-seguro.png')
print('P1 texto ahora entre', y0 + dy, 'y', y1 + dy)

# ---------------- P2: la lista se achica para terminar antes del 82 %
img = load('post-2-vertical')
y0, y1, x0, x1 = 1100, 1692, 88, 566
keep = np.zeros(img.shape[:2], bool)
keep[1562:, 495:] = True                 # el hombro de Javo
extra = np.zeros(img.shape[:2], np.uint8)
extra[1674:1688, 490:570] = 255          # la punta de la última línea sobre el hombro
clean, a, F = lift_layer(img, y0, y1, x0, x1, thr=14, open_k=23, keep=keep, extra=extra)
k = 0.82
h, w = a.shape
nh, nw = round(h * k), round(w * k)
a2 = cv2.resize(a, (nw, nh), interpolation=cv2.INTER_AREA)
F2 = cv2.resize(F, (nw, nh), interpolation=cv2.INTER_AREA)
out = clean.copy()
ytop = 1088
out = comp(out, a2, F2, x0 + round((96 - x0) * (1 - k)), ytop)
save(out, 'post-2-vertical-seguro.png')
print('P2 lista ahora entre', ytop, 'y', ytop + nh)
