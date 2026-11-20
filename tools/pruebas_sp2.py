"""Pruebas y capturas automáticas de Mi Recetario (SP2) con Playwright.
Uso: python tools/pruebas_sp2.py <url_base> [carpeta_capturas]
Ej.:  python tools/pruebas_sp2.py https://jazyelae.github.io/Mi_Recetario/ evidencias/SP2
Imprime el resultado de cada criterio de aceptación (CA) y guarda las capturas."""
import os
import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

URL = sys.argv[1]
SALIDA = sys.argv[2] if len(sys.argv) > 2 else None
resultados = []


def ca(nombre, ok, detalle=""):
    resultados.append(ok)
    print(("✅" if ok else "❌"), nombre, "-", detalle)


def captura(pagina, archivo, **kw):
    if SALIDA:
        os.makedirs(SALIDA, exist_ok=True)
        pagina.screenshot(path=os.path.join(SALIDA, archivo), **kw)


def ir_a(pagina, selector):
    pagina.locator(selector).scroll_into_view_if_needed()
    pagina.evaluate(f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})")
    pagina.wait_for_timeout(500)


with sync_playwright() as p:
    nav = p.chromium.launch(channel="chrome")  # Chrome real: muestra la página de "sin conexión"

    # ---------------- Escritorio 1366x768 ----------------
    ctx = nav.new_context(viewport={"width": 1366, "height": 768}, locale="es-MX")
    pg = ctx.new_page()
    errores, peticiones = [], []
    pg.on("console", lambda m: errores.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errores.append(str(e)))
    pg.on("response", lambda r: peticiones.append((r.url, r.status)))

    pg.goto(URL, wait_until="load")
    pg.wait_for_selector("#grid .card")
    pg.wait_for_selector("#gridMundo .card", timeout=20000)
    pg.wait_for_timeout(1500)
    captura(pg, "01_inicio.png")

    json_ok = [s for u, s in peticiones if u.endswith("data/recetas.json")]
    ca("CA-2 recetas desde data/recetas.json", json_ok == [200], f"respuestas: {json_ok}")
    n = pg.locator("#grid .card").count()

    # Filtro Sopas
    pg.click(".chip[data-c='Sopas']")
    cats = pg.locator("#grid .card .cat").all_inner_texts()
    ir_a(pg, "#recetas")
    captura(pg, "02_filtro_sopas.png")
    ok_filtro = len(cats) > 0 and all(c.lower() == "sopas" for c in cats)
    # Búsqueda aguacate
    pg.click(".chip[data-c='Todas']")
    pg.fill("#q", "aguacate")
    nombres = pg.locator("#grid .card h3").all_inner_texts()
    ir_a(pg, "#recetas")
    captura(pg, "03_busqueda_aguacate.png")
    pg.fill("#q", "jitomate"); a = pg.locator("#grid .card").count()
    pg.fill("#q", "JITÓMATE"); b = pg.locator("#grid .card").count()
    pg.fill("#q", "")
    ca("CA-3 filtro, búsqueda y acentos", ok_filtro and "Guacamole clásico" in nombres and a == b and a > 0,
       f"{n} recetas; Sopas={cats}; aguacate={nombres}; jitomate={a} / JITÓMATE={b}")

    # Detalle
    pg.locator("#grid .card").first.click()
    pg.wait_for_selector("#detalle[open]")
    pg.wait_for_timeout(400)
    ing = pg.locator("#dContenido ul li").count()
    pasos = pg.locator("#dContenido ol li").count()
    hash_ = pg.evaluate("location.hash")
    captura(pg, "04_detalle.png")
    pg.keyboard.press("Escape")
    pg.wait_for_timeout(300)
    cerrado = not pg.locator("#detalle").evaluate("d => d.open")
    pg.goto(URL + "#receta/guacamole")
    pg.wait_for_selector("#detalle[open]")
    directo = pg.locator("#dTitulo").inner_text()
    pg.keyboard.press("Escape")
    ca("CA-4 detalle, Esc y enlace directo", ing > 0 and pasos > 0 and cerrado and directo == "Guacamole clásico",
       f"hash={hash_}; ingredientes={ing}; pasos={pasos}; Esc cierra={cerrado}; #receta/guacamole -> {directo}")

    # TheMealDB
    pg.wait_for_selector("#gridMundo .card", timeout=20000)
    ir_a(pg, "#mundo")
    pg.wait_for_timeout(1500)
    captura(pg, "05_mealdb.png")
    estado = pg.locator("#estadoMundo").inner_text()
    pg.locator("#gridMundo .card").first.click()
    pg.wait_for_selector("#detalle[open] .d-foto")
    pg.wait_for_function("document.querySelector('.d-foto').complete")
    pg.wait_for_timeout(800)
    captura(pg, "05b_mealdb_detalle.png")
    titulo = pg.locator("#dTitulo").inner_text()
    pg.keyboard.press("Escape")
    api = [s for u, s in peticiones if "themealdb.com/api" in u]
    ca("CA-5 API TheMealDB", api and api[0] == 200 and pg.locator("#gridMundo .card").count() > 0,
       f"{estado} · detalle: {titulo} · HTTP {api[:1]}")

    # Formulario
    ir_a(pg, "#contacto")
    pg.fill("#nombre", "J"); pg.fill("#correo", "correo-malo"); pg.fill("#msg", "corto")
    pg.click("#form button[type=submit]")
    pg.wait_for_timeout(300)
    errs = [t for t in pg.locator("#form .error").all_inner_texts() if t]
    captura(pg, "06_formulario_errores.png")
    pg.fill("#nombre", "Jaziel Serrano"); pg.fill("#correo", "jaziel@ejemplo.com")
    pg.select_option("#categoria", "Sopas")
    pg.fill("#msg", "Me gustaría ver una receta de pozole rojo.")
    pg.click("#form button[type=submit]")
    pg.wait_for_timeout(300)
    ok_msg = pg.locator("#ok").inner_text()
    captura(pg, "07_formulario_ok.png")
    ca("CA-6 validación del formulario", len(errs) == 4 and "Gracias" in ok_msg, f"errores={len(errs)}; envío: {ok_msg}")

    # Sin manifest ni service worker
    manifest = pg.locator("link[rel=manifest]").count()
    sw = pg.evaluate("navigator.serviceWorker.getRegistrations().then(r => r.length)")
    ca("CA-9 sin manifest ni service worker", manifest == 0 and sw == 0, f"manifest={manifest}; SW={sw}")

    # Responsive escritorio (se mide con la página cargada)
    ancho_ok = {1366: not pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")}

    # Sin conexión
    ctx.set_offline(True)
    try:
        pg.reload(wait_until="load", timeout=10000)
        cargo = True
    except Exception as e:
        cargo = False
        detalle_off = str(e).splitlines()[0]
    pg.wait_for_timeout(800)
    captura(pg, "08_sin_conexion.png")
    ctx.set_offline(False)
    ca("CA-8 sin conexión la app NO carga", not cargo, detalle_off if not cargo else "cargó (no esperado)")

    ca("CA-1 consola sin errores", len(errores) == 0 or all("ERR_INTERNET_DISCONNECTED" in e for e in errores), f"errores: {errores[:3]}")
    ctx.close()

    # ---------------- Tablet y móvil ----------------
    for ancho, alto in [(768, 1024), (390, 844)]:
        c = nav.new_context(viewport={"width": ancho, "height": alto}, locale="es-MX",
                            is_mobile=ancho < 500, has_touch=ancho < 500, device_scale_factor=2 if ancho < 500 else 1)
        m = c.new_page()
        m.goto(URL, wait_until="load")
        m.wait_for_selector("#grid .card")
        m.wait_for_selector("#gridMundo .card", timeout=20000)
        m.wait_for_timeout(1200)
        ancho_ok[ancho] = not m.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        if ancho == 390:
            captura(m, "09_movil_inicio.png")
            m.click("#menuBtn"); m.wait_for_timeout(300)
            captura(m, "10_movil_menu.png")
            m.click("#menu a[href='#recetas']"); m.wait_for_timeout(600)
            m.locator("#grid .card").nth(2).click()
            m.wait_for_selector("#detalle[open]"); m.wait_for_timeout(400)
            captura(m, "11_movil_detalle.png")
        else:
            captura(m, "12_tablet.png")
        c.close()
    ca("CA-7 sin desbordamiento horizontal", all(ancho_ok.values()), str(ancho_ok))
    nav.close()

print(f"\nResultado: {sum(resultados)}/{len(resultados)} criterios OK")
sys.exit(0 if all(resultados) else 1)
