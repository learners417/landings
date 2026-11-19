"""Portadas de La Videoteca (curso de Sanadores Libres, comunidad abierta). 19 nov 2026.
Misma piel que las tarjetas de og/tarjeta.py.
Armar:  python3 og/videoteca.py    → imgs/videoteca/<clave>.jpg (1200 x 630)
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import tarjeta as T

T.T.clear()
t = T.t
t('videoteca', 'La Videoteca.', 'Todo lo que grabé, en el orden del camino: del lago al bosque.', 'lago2', T.numeral('60', 'videos, para mirar uno y hacer algo'))
t('empieza', 'Empieza aquí.', 'Dos videos para ordenar todo lo demás.', 'papel2', T.lomos_grandes())
t('lago', 'El lago.', 'Mírate antes de moverte.', 'papel2', T.tapas('lago'))
t('montana', 'La montaña.', 'Tu programa y tu precio.', 'papel2', T.tapas('montana'))
t('viento', 'El viento.', 'Tu voz y tu llamada.', 'papel2', T.tapas('viento'))
t('rio', 'El río.', 'Que todo corra solo.', 'papel2', T.tapas('rio'))
t('bosque', 'El bosque.', 'Tu marca y tu ecosistema.', 'papel2', T.tapas('bosque'))
t('cruzaron', 'Los que ya cruzaron.', 'Sus historias, en primera persona.', 'sanadores', T.numeral('10', 'historias de colegas'))
t('metodo-360', 'Método 360 en 7 días.', 'Un video por día, durante una semana.', 'viento', T.numeral('7', 'días, un paso por día'))
t('marca-digital', 'Marca Digital Rentable.', 'Seis clases, de la intención al embudo.', 'montana', T.numeral('6', 'clases'))

if __name__ == '__main__':
    sys.argv = [sys.argv[0], str(T.REPO / 'imgs/videoteca')] + sys.argv[1:]
    T.main()
