"""Une dos capturas reales (web y Android) lado a lado, con la misma altura y una etiqueta arriba.
Uso: python tools/comparativa_sp5.py web.png android.png salida.png"""
import sys
from PIL import Image, ImageDraw, ImageFont

web, android, salida = sys.argv[1:4]
ALTO, MARGEN, BARRA = 1400, 40, 90
GUINDA = (123, 23, 59)
try:
    fuente = ImageFont.truetype("arialbd.ttf", 40)
except OSError:
    fuente = ImageFont.load_default()

imgs = []
for ruta in (web, android):
    im = Image.open(ruta).convert("RGB")
    imgs.append(im.resize((round(im.width * ALTO / im.height), ALTO), Image.LANCZOS))

ancho = sum(i.width for i in imgs) + MARGEN * (len(imgs) + 1)
lienzo = Image.new("RGB", (ancho, ALTO + BARRA + MARGEN), "white")
d = ImageDraw.Draw(lienzo)
x = MARGEN
for im, texto in zip(imgs, ("Web · Chrome (GitHub Pages)", "Android 14 · APK (emulador)")):
    lienzo.paste(im, (x, BARRA))
    d.rectangle([x - 2, BARRA - 2, x + im.width + 1, BARRA + ALTO + 1], outline=(204, 204, 204), width=2)
    w = d.textlength(texto, font=fuente)
    d.text((x + (im.width - w) / 2, 22), texto, fill=GUINDA, font=fuente)
    x += im.width + MARGEN
lienzo.save(salida)
print("PNG:", salida)
