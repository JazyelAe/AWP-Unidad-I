"""Extrae todos los enlaces de un PDF y comprueba que abran (curl y, si un sitio bloquea a curl, Chrome).
Uso: python tools/verificar_enlaces.py reporte.pdf"""
import subprocess, sys
import pymupdf
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
urls = sorted({l["uri"] for p in pymupdf.open(sys.argv[1]) for l in p.get_links() if l.get("uri")})
codigos = {}
for u in urls:
    codigos[u] = subprocess.run(["curl", "-s", "-o", "/dev/null", "-L", "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130",
                                 "-w", "%{http_code}", u], capture_output=True, text=True).stdout
dudosos = [u for u, c in codigos.items() if c != "200"]
if dudosos:
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        for u in dudosos:
            pg = b.new_page()
            try:
                r = pg.goto(u, wait_until="load", timeout=45000)
                codigos[u] = f"{codigos[u]} (curl) → {r.status} (Chrome)"
            except Exception as e:
                codigos[u] = f"{codigos[u]} (curl) → error en Chrome: {str(e)[:60]}"
            pg.close()
        b.close()
malos = 0
for u in urls:
    final = codigos[u].split()[-2] if "Chrome" in codigos[u] else codigos[u]
    bien = final == "200"
    malos += not bien
    print("✅" if bien else "❌", codigos[u], u)
print(f"\n{len(urls) - malos}/{len(urls)} enlaces abren")
