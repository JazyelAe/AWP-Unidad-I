"""Comprueba las reglas de Firestore publicadas, contra la base real de Mi Recetario.
1) Borrar una receta antigua → rechazado (403).  2) Crear una receta inválida → rechazado (403).
3) Crear una receta válida DESDE LA APP y borrarla en menos de 10 minutos → permitido.
Uso: python tools/reglas_sp7.py <url_app> <carpeta_capturas>"""
import json, os, sys, time, urllib.error, urllib.request
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
URL, SALIDA = sys.argv[1], sys.argv[2]
KEY = "AIzaSyDiuklmKy5hiSmI_7Q6xbTAqdkLehitfCs"   # clave web pública (la protección son las reglas)
BASE = "https://firestore.googleapis.com/v1/projects/mi-recetario-61665/databases/(default)/documents"
res = []


def ok(c, t, e=""):
    res.append(bool(c)); print("✅" if c else "❌", t, e)


def http(metodo, ruta, cuerpo=None):
    req = urllib.request.Request(f"{BASE}/{ruta}?key={KEY}", method=metodo,
                                 data=json.dumps(cuerpo).encode() if cuerpo else None,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


docs = json.loads(http("GET", "recetas")[1]).get("documents", [])
antigua = min(docs, key=lambda d: d["fields"]["creada"]["timestampValue"])
nombre = antigua["fields"]["nombre"]["stringValue"]
estado, _ = http("DELETE", "recetas/" + antigua["name"].split("/")[-1])
ok(estado == 403, f"Borrar la receta antigua «{nombre}» → rechazado", f"({estado})")
ok(len(json.loads(http("GET", "recetas")[1]).get("documents", [])) == len(docs), "La receta antigua sigue en la base")
estado, _ = http("POST", "recetas", {"fields": {"nombre": {"stringValue": "Intrusa"}, "ingredientes": {"stringValue": "x"},
                                                 "campo_raro": {"stringValue": "no permitido"}}})
ok(estado == 403, "Crear una receta con campos no permitidos y sin fecha del servidor → rechazado", f"({estado})")

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1280, "height": 900}, locale="es-MX")
    pg.on("dialog", lambda d: d.accept())
    pg.goto(URL, wait_until="load")
    pg.locator("#grid .card").first.wait_for(timeout=30000)
    prueba = f"Prueba de reglas {time.strftime('%H:%M:%S')}"
    pg.locator("details.nueva summary").click()
    pg.locator("#rNombre").fill(prueba); pg.locator("#rCat").fill("Pruebas"); pg.locator("#rMin").fill("5")
    pg.locator("#rIng").fill("agua, sal")
    pg.get_by_role("button", name="Guardar receta").click()
    tarjeta = pg.locator("#grid .card", has_text=prueba)
    tarjeta.wait_for(timeout=15000)
    pg.get_by_text("Receta guardada.").wait_for(timeout=15000)
    ok(True, "Crear una receta válida desde la app → permitido", f"({prueba})")
    pg.wait_for_timeout(3000)   # la tarjeta se redibuja cuando Firestore confirma la escritura
    pg.evaluate("document.querySelector('#recetas').scrollIntoView()")
    pg.wait_for_timeout(500)
    pg.screenshot(path=os.path.join(SALIDA, "14_regla_alta.png"))
    tarjeta.locator(".del").click()
    tarjeta.wait_for(state="detached", timeout=15000)
    pg.wait_for_timeout(2500)
    errores = pg.locator("#aviso.err").count()
    ok(errores == 0 and "Receta borrada" in pg.locator("#aviso").inner_text(), "Borrarla en menos de 10 minutos → permitido")
    b.close()
ok(not any(prueba == d["fields"]["nombre"]["stringValue"] for d in json.loads(http("GET", "recetas")[1]).get("documents", [])),
   "La receta de prueba ya no está en la base")
print(f"\n{sum(res)}/{len(res)} comprobaciones correctas")
