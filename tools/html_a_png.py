"""Convierte un HTML (diagrama) a PNG con Playwright.
Uso: python tools/html_a_png.py entrada.html salida.png [ancho]"""
import sys, pathlib
from playwright.sync_api import sync_playwright

entrada, salida = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2]
ancho = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": ancho, "height": 600}, device_scale_factor=2)
    pg.goto(entrada.as_uri())
    pg.locator("#diagrama").screenshot(path=salida)
    b.close()
print("PNG:", salida)
