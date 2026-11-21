"""Convierte el registro real de gunicorn (prueba en GitHub Actions) en una imagen para el reporte.
Muestra método, ruta y código de estado de cada petición que recibió la API.
Uso: python tools/registro_sp6.py evidencias/SP6/gunicorn_actions.log salida.png"""
import html, re, subprocess, sys, tempfile, os

entrada, salida = sys.argv[1], sys.argv[2]
filas = []
for linea in open(entrada, encoding="utf-8"):
    m = re.search(r'\[(.+?) \+0000\] "(\w+) (\S+) HTTP/1\.1" (\d{3})', linea)
    if m and "Python-urllib" not in linea and "curl" not in linea:  # solo las del navegador (cliente web)
        hora, metodo, ruta, codigo = m.group(1).split(":", 1)[1], m.group(2), m.group(3), m.group(4)
        color = {"2": "#15803d", "4": "#b91c1c"}.get(codigo[0], "#555")
        filas.append(f"<tr><td>{hora}</td><td><b>{metodo}</b></td><td>{html.escape(ruta)}</td>"
                     f"<td style='color:{color}'><b>{codigo}</b></td></tr>")
pagina = f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;font-family:Consolas,monospace;background:#fff}}#diagrama{{width:900px;padding:18px}}
h2{{font-family:Helvetica,Arial;color:#7B173B;font-size:20px;margin:0 0 10px}}
table{{border-collapse:collapse;width:100%;font-size:14px}}td{{padding:4px 10px;border-bottom:1px solid #ddd}}
tr:nth-child(even){{background:#F4EEF1}}</style><div id="diagrama">
<h2>Peticiones HTTP que recibió la API (gunicorn, GitHub Actions)</h2><table>{''.join(filas)}</table></div>"""
tmp = os.path.join(tempfile.gettempdir(), "registro_sp6.html")
open(tmp, "w", encoding="utf-8").write(pagina)
subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "html_a_png.py"), tmp, salida, "940"], check=True)
print(len(filas), "peticiones")
