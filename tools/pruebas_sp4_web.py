"""Prueba y captura la demo web de Mis Pendientes (Flutter web) en vista móvil 390x844.
Uso: python tools/pruebas_sp4_web.py <url> [carpeta_capturas]"""
import os
import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
URL = sys.argv[1]
SALIDA = sys.argv[2] if len(sys.argv) > 2 else "."
os.makedirs(SALIDA, exist_ok=True)

with sync_playwright() as p:
    nav = p.chromium.launch(channel="chrome")
    ctx = nav.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True,
                          has_touch=True, locale="es-MX")
    pg = ctx.new_page()
    errores = []
    pg.on("pageerror", lambda e: errores.append(str(e)))
    pg.on("console", lambda m: errores.append(m.text) if m.type == "error" else None)
    pg.goto(URL, wait_until="load")
    pg.wait_for_selector("flt-semantics-placeholder, flutter-view", state="attached", timeout=30000)
    pg.wait_for_timeout(2500)
    # Flutter web dibuja en un canvas; se activa su árbol de accesibilidad para encontrar los botones por texto.
    pg.evaluate("document.querySelector('flt-semantics-placeholder')?.click()")
    pg.wait_for_timeout(800)
    pg.get_by_text("Agregar tareas de ejemplo").click()
    pg.wait_for_timeout(1500)
    pg.screenshot(path=os.path.join(SALIDA, "11_web_movil.png"))
    hay = "Entregar reporte de AWP" in pg.content()
    pg.reload(wait_until="load")
    pg.wait_for_timeout(3000)
    pg.evaluate("document.querySelector('flt-semantics-placeholder')?.click()")
    pg.wait_for_timeout(800)
    persiste = "Entregar reporte de AWP" in pg.content()
    desborde = pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    print(("✅" if hay else "❌"), "La demo web carga y agrega tareas en vista móvil 390x844")
    print(("✅" if persiste else "❌"), "Las tareas persisten al recargar (localStorage)")
    print(("✅" if not desborde else "❌"), "Sin desbordamiento horizontal")
    print(("✅" if not errores else "❌"), "Consola sin errores", errores[:3])
    nav.close()
