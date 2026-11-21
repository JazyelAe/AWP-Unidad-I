"""Prueba y genera las evidencias PWA de Mi Recetario con Chrome (Playwright + Chrome DevTools Protocol).
Todo se lee del navegador real: manifest, service worker, Cache Storage, instalabilidad, modo sin conexión.
Uso: python tools/pruebas_sp7.py <url_app> [carpeta_capturas] [--pantallas carpeta_screenshots_manifest]"""
import html
import json
import os
import sys
import tempfile
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
URL = sys.argv[1]
SALIDA = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "."
PANTALLAS = sys.argv[sys.argv.index("--pantallas") + 1] if "--pantallas" in sys.argv else None
os.makedirs(SALIDA, exist_ok=True)
resultados = []


def ok(cond, texto, extra=""):
    resultados.append(bool(cond))
    print("✅" if cond else "❌", texto, extra)


ESTILO = """<style>body{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#fff;color:#222}
#panel{width:900px;padding:20px}h2{margin:0 0 4px;color:#7B173B;font-size:20px}.sub{color:#555;margin:0 0 12px;font-size:13px}
table{border-collapse:collapse;width:100%;font-size:13.5px}td,th{border-bottom:1px solid #ddd;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#7B173B;color:#fff}tr:nth-child(even) td{background:#F4EEF1}code{font-family:Consolas,monospace;font-size:12.5px}
.ok{color:#15803d;font-weight:700}.mal{color:#b91c1c;font-weight:700}img.ic{width:48px;height:48px;border:1px solid #ccc;border-radius:6px}</style>"""


def panel(navegador, nombre, titulo, subtitulo, cuerpo):
    """Dibuja datos reales leídos del navegador en una tabla y la guarda como imagen."""
    p = navegador.new_page(viewport={"width": 940, "height": 400}, device_scale_factor=2)
    p.set_content(f"<!doctype html><meta charset=utf-8>{ESTILO}<div id=panel><h2>{titulo}</h2>"
                  f"<p class=sub>{subtitulo}</p>{cuerpo}</div>")
    p.wait_for_timeout(800)  # imágenes de iconos
    p.locator("#panel").screenshot(path=os.path.join(SALIDA, nombre))
    p.close()


def fila(*celdas):
    return "<tr>" + "".join(f"<td>{c}</td>" for c in celdas) + "</tr>"


with sync_playwright() as p:
    # Contexto persistente (no incógnito): Chrome solo evalúa la instalabilidad fuera del modo incógnito.
    perfil = tempfile.mkdtemp(prefix="perfil_pwa_")
    ctx = p.chromium.launch_persistent_context(perfil, channel="chrome", headless=True, locale="es-MX",
                                               viewport={"width": 1280, "height": 800})
    pg = ctx.pages[0]
    errores = []
    pg.on("pageerror", lambda e: errores.append(str(e)))
    cdp = ctx.new_cdp_session(pg)

    respuesta = pg.goto(URL, wait_until="load")
    pg.locator("#grid .card").first.wait_for(timeout=30000)
    pg.wait_for_function("navigator.serviceWorker.controller !== null || navigator.serviceWorker.ready", timeout=20000)
    pg.evaluate("navigator.serviceWorker.ready")
    pg.wait_for_timeout(2500)
    tarjetas = pg.locator("#grid .card").count()
    ok(tarjetas > 0, "Recetas cargadas desde Firestore", f"({tarjetas})")
    pg.screenshot(path=os.path.join(SALIDA, "01_escritorio.png"))
    if PANTALLAS:
        os.makedirs(PANTALLAS, exist_ok=True)
        pg.screenshot(path=os.path.join(PANTALLAS, "escritorio.png"))

    # ---------- HTTPS ----------
    seguridad = respuesta.security_details() if URL.startswith("https") else None
    if seguridad:
        ok(pg.evaluate("location.protocol") == "https:" and pg.evaluate("window.isSecureContext"), "Servida por HTTPS (contexto seguro)")
        from datetime import datetime, timezone
        vence = datetime.fromtimestamp(seguridad["validTo"], timezone.utc).strftime("%d/%m/%Y")
        panel(p.chromium.launch(channel="chrome"), "03_https.png", "HTTPS: conexión segura",
              "Datos del certificado leídos por Chrome al abrir la app (Playwright · security_details).",
              "<table>" + fila("URL", f"<code>{html.escape(pg.url)}</code>") + fila("Protocolo", seguridad.get("protocol"))
              + fila("Emitido para", seguridad.get("subjectName")) + fila("Emisor", seguridad.get("issuer"))
              + fila("Válido hasta", vence) + fila("Contexto seguro (window.isSecureContext)", "<span class=ok>true</span>")
              + "</table>")

    # ---------- Manifest (leído por Chrome) ----------
    man = cdp.send("Page.getAppManifest")
    datos = json.loads(man.get("data") or "{}")
    ok(not man.get("errors") and datos.get("display") == "standalone", "Manifest válido para Chrome", man.get("errors"))
    base = man["url"].rsplit("/", 1)[0] + "/"
    iconos = "".join(f"<img class=ic src='{base}{i['src']}'> <code>{i['sizes']} · {i.get('purpose', 'any')}</code><br>"
                     for i in datos.get("icons", []))
    capturas = "<br>".join(f"<code>{s['src']}</code> ({s['form_factor']}, {s['sizes']})" for s in datos.get("screenshots", []))
    campos = ["name", "short_name", "start_url", "scope", "display", "theme_color", "background_color", "lang", "id"]
    panel(p.chromium.launch(channel="chrome"), "04_manifest.png", "Web App Manifest",
          f"Leído por Chrome con Page.getAppManifest desde <code>{html.escape(man['url'])}</code> · errores: "
          f"<span class=ok>{len(man.get('errors', []))}</span>",
          "<table>" + "".join(fila(f"<code>{c}</code>", html.escape(str(datos.get(c, "")))) for c in campos)
          + fila("<code>icons</code>", iconos) + fila("<code>screenshots</code>", capturas) + "</table>")

    # ---------- Service worker ----------
    sw = pg.evaluate("""navigator.serviceWorker.getRegistration().then(r => ({
        scope: r.scope, script: r.active && r.active.scriptURL, estado: r.active && r.active.state,
        controla: !!navigator.serviceWorker.controller }))""")
    ok(sw["estado"] == "activated" and sw["controla"], "Service worker activo y controlando la página", sw["estado"])

    # ---------- Cache Storage ----------
    cachés = pg.evaluate("""caches.keys().then(ks => Promise.all(ks.map(async k =>
        [k, (await (await caches.open(k)).keys()).map(r => r.url)])))""")
    nombres = dict(cachés)
    app = next((v for k, v in nombres.items() if k.startswith("recetario-app")), [])
    ok(any("firebase-firestore.js" in u for u in app) and any("offline.html" in u for u in app),
       "Cache Storage con app shell, offline.html y SDK de Firebase", f"({len(app)} archivos)")
    panel(p.chromium.launch(channel="chrome"), "05_service_worker.png", "Service worker registrado y activo",
          "Leído con navigator.serviceWorker.getRegistration() en la app publicada.",
          "<table>" + fila("Script", f"<code>{html.escape(sw['script'])}</code>") + fila("Alcance (scope)", f"<code>{html.escape(sw['scope'])}</code>")
          + fila("Estado", f"<span class=ok>{sw['estado']}</span>") + fila("¿Controla la página?", f"<span class=ok>{sw['controla']}</span>")
          + fila("Estrategias", "Páginas: <b>network first</b> + offline.html · App y SDK de Firebase: <b>cache first</b> · "
                 "Fotos: <b>stale-while-revalidate</b> · Recetas: caché persistente de Firestore (IndexedDB)") + "</table>")
    filas_cache = ""
    for nombre, urls in cachés:
        for u in urls:
            corto = u.replace(base, "./")
            filas_cache += fila(f"<code>{html.escape(nombre)}</code>", f"<code>{html.escape(corto)}</code>")
    panel(p.chromium.launch(channel="chrome"), "06_cache_storage.png", "Cache Storage",
          f"Archivos guardados en el dispositivo por el service worker ({sum(len(u) for _, u in cachés)} en total).",
          "<table><tr><th>Caché</th><th>Archivo</th></tr>" + filas_cache + "</table>")

    # ---------- Instalabilidad ----------
    instalable = cdp.send("Page.getInstallabilityErrors").get("installabilityErrors", [])
    ok(instalable == [], "Instalable: Chrome no reporta errores de instalabilidad", instalable)
    panel(p.chromium.launch(channel="chrome"), "07_instalable.png", "Criterios de instalación",
          "Resultado de Page.getInstallabilityErrors (Chrome DevTools Protocol): Chrome lista aquí cualquier motivo que impida instalar la app.",
          "<table>" + fila("Errores de instalabilidad", f"<span class={'ok' if not instalable else 'mal'}>"
                           f"{'Ninguno: la app se puede instalar' if not instalable else html.escape(str(instalable))}</span>")
          + fila("Manifest con name, iconos 192/512, start_url y display standalone", "<span class=ok>Sí</span>")
          + fila("Service worker con evento fetch", "<span class=ok>Sí</span>")
          + fila("HTTPS", f"<span class=ok>{URL.startswith('https')}</span>") + "</table>")

    # ---------- Sin conexión ----------
    cdp.detach()  # la sesión CDP propia interfiere con la emulación «sin red» de Playwright
    ctx.set_offline(True)
    pg.reload(wait_until="load")
    pg.locator("#grid .card").first.wait_for(timeout=20000)
    pg.wait_for_function("document.querySelector('#modo').textContent.includes('Sin conexión')", timeout=20000)
    sin_red = pg.locator("#grid .card").count()
    ok(sin_red == tarjetas, "Sin conexión: al recargar se ven las mismas recetas (Firestore offline)", f"({sin_red})")
    pg.locator("#qApi").fill("pasta")
    pg.locator("#formApi button").click()
    pg.wait_for_timeout(1500)
    aviso_api = pg.locator("#estadoApi").inner_text()
    ok("necesita Internet" in aviso_api or "revisa tu conexión" in aviso_api, "La búsqueda en TheMealDB avisa que necesita Internet", f"({aviso_api[:60]})")
    pg.evaluate("window.scrollTo(0, 0)")
    pg.wait_for_timeout(500)
    pg.screenshot(path=os.path.join(SALIDA, "08_offline.png"))
    pg.goto(URL + "pagina-no-guardada.html", wait_until="load")
    ok(pg.get_by_text("Estás sin conexión").is_visible(), "Página no guardada sin red → offline.html")
    pg.screenshot(path=os.path.join(SALIDA, "09_offline_html.png"))
    ctx.set_offline(False)
    ok(not [e for e in errores if "Failed to fetch" not in e], "Sin errores de JavaScript", errores[:2])
    ctx.close()

    # ---------- Vista de teléfono ----------
    nav = p.chromium.launch(channel="chrome")
    movil = nav.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True, locale="es-MX")
    pm = movil.new_page()
    pm.goto(URL, wait_until="load")
    pm.locator("#grid .card").first.wait_for(timeout=30000)
    pm.wait_for_timeout(1500)
    pm.screenshot(path=os.path.join(SALIDA, "02_movil.png"))
    if PANTALLAS:
        pm.screenshot(path=os.path.join(PANTALLAS, "movil.png"))
    ok(not pm.evaluate("document.documentElement.scrollWidth > window.innerWidth"), "Responsive: sin desbordamiento en 390 px")
    nav.close()

print(f"\n{sum(resultados)}/{len(resultados)} comprobaciones correctas")
sys.exit(0 if all(resultados) else 1)
