"""Lee con Chrome las características PWA de sitios reales (manifest, service worker, instalabilidad)
y genera una imagen de evidencia por sitio. Uso: python tools/pwa_real_sp7.py <carpeta> url1 [url2 ...]"""
import html, json, os, sys, tempfile
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
SALIDA, SITIOS = sys.argv[1], sys.argv[2:]
ESTILO = ("<style>body{margin:0;font-family:Segoe UI,Arial,sans-serif}#p{width:900px;padding:20px}h2{color:#7B173B;margin:0 0 4px}"
          ".s{color:#555;font-size:13px;margin:0 0 10px}table{border-collapse:collapse;width:100%;font-size:13.5px}"
          "td{border-bottom:1px solid #ddd;padding:6px 8px;vertical-align:top}tr:nth-child(even) td{background:#F4EEF1}"
          "code{font-family:Consolas,monospace;font-size:12.5px}.ok{color:#15803d;font-weight:700}.no{color:#b91c1c;font-weight:700}"
          "img{width:44px;height:44px;border:1px solid #ccc;border-radius:6px;margin-right:6px}</style>")
with sync_playwright() as p:
    for url in SITIOS:
        ctx = p.chromium.launch_persistent_context(tempfile.mkdtemp(), channel="chrome", headless=True,
                                                   locale="es-MX", viewport={"width": 1280, "height": 800})
        pg = ctx.pages[0]
        pg.goto(url, wait_until="load", timeout=60000)
        pg.wait_for_timeout(8000)
        cdp = ctx.new_cdp_session(pg)
        man = cdp.send("Page.getAppManifest")
        datos = json.loads(man.get("data") or "{}")
        sw = pg.evaluate("navigator.serviceWorker.getRegistration().then(r => r ? {script: (r.active||r.waiting||r.installing).scriptURL, estado: (r.active||r.waiting||r.installing).state} : null)")
        errores = cdp.send("Page.getInstallabilityErrors").get("installabilityErrors", [])
        nombre = url.split("//")[1].split("/")[0].replace("www.", "").split(".")[0]
        print(url, "| manifest:", man.get("url"), "| sw:", sw, "| instalable:", errores)
        base = man["url"].rsplit("/", 1)[0] + "/" if man.get("url") else ""
        icono = next((i for i in datos.get("icons", []) if "192" in i.get("sizes", "")), (datos.get("icons") or [{}])[0])
        src = icono.get("src", "")
        src = src if src.startswith("http") else base + src.lstrip("./")
        filas = "".join(f"<tr><td><code>{k}</code></td><td>{html.escape(str(datos.get(k, '—')))}</td></tr>"
                        for k in ("name", "short_name", "start_url", "display", "theme_color"))
        cuerpo = (f"<table><tr><td>URL</td><td><code>{html.escape(pg.url)}</code></td></tr>"
                  f"<tr><td>Manifest</td><td><img src='{html.escape(src)}'><code>{html.escape(man.get('url') or 'no tiene')}</code></td></tr>{filas}"
                  f"<tr><td>Service worker</td><td class={'ok' if sw else 'no'}>{html.escape(sw['script'] + ' · ' + sw['estado']) if sw else 'no registrado'}</td></tr>"
                  f"<tr><td>Errores de instalabilidad</td><td class={'ok' if not errores else 'no'}>{'Ninguno: instalable' if not errores else html.escape(str(errores))}</td></tr></table>")
        hoja = p.chromium.launch(channel="chrome").new_page(device_scale_factor=2, viewport={"width": 940, "height": 300})
        hoja.set_content(f"<meta charset=utf-8>{ESTILO}<div id=p><h2>PWA real: {html.escape(datos.get('name', nombre))}</h2>"
                         f"<p class=s>Leído con Chrome (Page.getAppManifest, serviceWorker.getRegistration y Page.getInstallabilityErrors).</p>{cuerpo}</div>")
        hoja.wait_for_timeout(1500)
        hoja.locator("#p").screenshot(path=os.path.join(SALIDA, f"10_pwa_real_{nombre}.png"))
        pg.screenshot(path=os.path.join(SALIDA, f"10_sitio_{nombre}.png"))
        ctx.close()
