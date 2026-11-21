"""Prueba y captura la versión web de ConvierteYA (React Native + Expo para web) con Chrome.
Comprueba CA-1 (unidades y divisas sin errores), CA-3 (sin conexión), CA-4 (historial al recargar)
y CA-5 (intercambiar y copiar: lee el portapapeles real del navegador).
Uso: python tools/pruebas_sp5_web.py <url> [carpeta_capturas]"""
import json
import os
import sys
import urllib.request
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
URL = sys.argv[1]
SALIDA = sys.argv[2] if len(sys.argv) > 2 else "."
os.makedirs(SALIDA, exist_ok=True)
resultados = []


def ok(cond, texto, extra=""):
    resultados.append(bool(cond))
    print("✅" if cond else "❌", texto, extra)


def resultado(pg):
    # Solo hay un resultado visible (las otras pestañas están ocultas con display:none)
    return pg.locator("[data-testid=resultado]:visible").inner_text().strip()


def escribir(pg, texto):
    caja = pg.locator("input[aria-label=Cantidad]:visible")
    caja.fill(texto)
    pg.wait_for_timeout(300)


with sync_playwright() as p:
    nav = p.chromium.launch(channel="chrome")
    ctx = nav.new_context(viewport={"width": 1280, "height": 860}, locale="es-MX", device_scale_factor=1)
    ctx.grant_permissions(["clipboard-read", "clipboard-write"])
    pg = ctx.new_page()
    errores = []
    pg.on("pageerror", lambda e: errores.append(str(e)))
    pg.on("console", lambda m: errores.append(m.text) if m.type == "error" else None)
    boton = lambda nombre: pg.get_by_role("button", name=nombre, exact=True).locator("visible=true")

    pg.goto(URL, wait_until="networkidle")
    pg.get_by_text("ConvierteYA", exact=True).wait_for()
    ok(pg.get_by_test_id("plataforma").inner_text() == "Web", "Etiqueta de plataforma: Web")

    # --- Unidades (CA-1) ---
    ok(resultado(pg) == "6.21371 mi", "10 km = 6.21371 mi", resultado(pg))
    escribir(pg, "25")
    ok(resultado(pg) == "15.5343 mi", "Conversión en tiempo real al escribir: 25 km = 15.5343 mi", resultado(pg))
    boton("Temperatura").click()
    escribir(pg, "37")
    ok(resultado(pg) == "98.6 °F", "37 °C = 98.6 °F", resultado(pg))
    boton("Guardar en historial").click()
    pg.screenshot(path=os.path.join(SALIDA, "01_web_unidades.png"))

    # --- Intercambiar y copiar (CA-5) ---
    boton("Intercambiar").click()
    pg.wait_for_timeout(300)
    ok(resultado(pg) == "2.77778 °C", "Intercambiar: 37 °F = 2.77778 °C", resultado(pg))
    boton("Copiar").click()
    pg.wait_for_timeout(500)
    copiado = pg.evaluate("navigator.clipboard.readText()")
    ok(copiado == "37 °F = 2.77778 °C", "El portapapeles tiene el resultado", repr(copiado))
    ok(pg.get_by_role("alert").inner_text().startswith("Copiado:"), "Aviso web «Copiado» (en lugar del Toast nativo)")

    # --- Divisas con la API Frankfurter (CA-1, CA-3) ---
    pg.get_by_role("tab", name="Divisas").click()
    pg.get_by_text("En línea · tipos del BCE", exact=False).wait_for(timeout=15000)
    with urllib.request.urlopen("https://api.frankfurter.dev/v1/latest?symbols=MXN,USD,GBP,JPY,CAD") as r:
        api = json.load(r)
    esperado = f"{100 / api['rates']['USD'] * api['rates']['MXN']:,.2f} MXN"
    ok(resultado(pg) == esperado, "100 USD → MXN coincide con la API", f"{resultado(pg)} (API: {esperado})")
    boton("Guardar en historial").click()
    pg.wait_for_timeout(2800)  # que se quite el aviso antes de la captura
    pg.screenshot(path=os.path.join(SALIDA, "02_web_divisas.png"))

    # --- Historial y persistencia (CA-4) ---
    pg.get_by_role("tab", name="Historial").click()
    pg.wait_for_timeout(400)
    ok(pg.get_by_text("2 de 30 conversiones guardadas").is_visible(), "Historial con 2 conversiones")
    pg.screenshot(path=os.path.join(SALIDA, "03_web_historial.png"))
    pg.reload(wait_until="networkidle")
    pg.get_by_role("tab", name="Historial").click()
    pg.wait_for_timeout(400)
    ok(pg.get_by_text("2 de 30 conversiones guardadas").is_visible(), "El historial persiste al recargar (AsyncStorage → localStorage)")

    # --- Sin conexión (CA-3) ---
    pg.get_by_role("tab", name="Divisas").click()
    pg.get_by_text("En línea · tipos del BCE", exact=False).wait_for(timeout=15000)
    ctx.set_offline(True)
    boton("Actualizar tipos de cambio").click()
    pg.get_by_text("Sin conexión · tipos del", exact=False).wait_for(timeout=15000)
    ok(resultado(pg) == esperado, "Sin conexión usa los tipos guardados", resultado(pg))
    pg.screenshot(path=os.path.join(SALIDA, "05_web_sin_conexion.png"))
    ctx.set_offline(False)
    errores = [e for e in errores if "ERR_INTERNET_DISCONNECTED" not in e]  # error esperado al estar sin red

    # --- Borrar una entrada ---
    pg.get_by_role("tab", name="Historial").click()
    pg.get_by_role("button", name="Borrar 37 °C = 98.6 °F").click()
    ok(pg.get_by_text("1 de 30 conversiones guardadas").is_visible(), "Borrar una entrada del historial")

    ok(not errores, "Consola sin errores", errores[:3])

    # --- Vista de teléfono 390x844 ---
    movil = nav.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True,
                            has_touch=True, locale="es-MX")
    pm = movil.new_page()
    pm.goto(URL, wait_until="networkidle")
    pm.get_by_text("ConvierteYA", exact=True).wait_for()
    pm.wait_for_timeout(500)
    pm.screenshot(path=os.path.join(SALIDA, "04_web_movil.png"))
    ok(not pm.evaluate("document.documentElement.scrollWidth > window.innerWidth"), "Sin desbordamiento horizontal en 390 px")
    # Misma conversión que en el emulador Android (100 USD → MXN) para la imagen comparativa
    pm.get_by_role("tab", name="Divisas").click()
    pm.get_by_text("En línea · tipos del BCE", exact=False).wait_for(timeout=15000)
    pm.wait_for_timeout(500)
    pm.screenshot(path=os.path.join(SALIDA, "04b_web_movil_divisas.png"))
    nav.close()

print(f"\n{sum(resultados)}/{len(resultados)} comprobaciones correctas")
sys.exit(0 if all(resultados) else 1)
