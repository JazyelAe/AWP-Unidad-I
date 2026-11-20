"""Funciones compartidas por los scripts de reportes (SP2 en adelante)."""
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "tools"))
from utp_doc import *  # noqa: E402,F401,F403
from utp_doc import estilos, figura, enlace, GRIS_CLARO  # noqa: E402
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
from reportlab.platypus import Paragraph, Table, TableStyle, KeepTogether  # noqa: E402

s = estilos()
REF = ParagraphStyle("ref", parent=s["bullet"], leftIndent=22, firstLineIndent=-22)


class Reporte:
    """Lleva la numeración de figuras y la carpeta de evidencias de un subproducto."""

    def __init__(self, sp):
        self.evid = os.path.join(RAIZ, "evidencias", sp)
        self.n = 0

    def fig(self, nombre, pie, ancho=420, alto_max=330):
        ruta = os.path.join(self.evid, nombre)
        if not os.path.exists(ruta):
            sys.exit(f"Falta la captura {ruta}")
        self.n += 1
        return figura(ruta, f"Figura {self.n}. {pie}", ancho, alto_max)

    def fila(self, capturas, alto_max=330):
        """Varias capturas lado a lado (2 o 3) en una tabla sin bordes."""
        ancho_col = 504 / len(capturas)
        celdas = [self.fig(n, p, ancho=ancho_col - 12, alto_max=alto_max)._content for n, p in capturas]
        t = Table([celdas], colWidths=[ancho_col] * len(capturas))
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
        return t


def P(texto, estilo="body"):
    return Paragraph(texto, s[estilo])


def li(texto):
    return Paragraph("•&nbsp;&nbsp;" + texto, s["bullet"])


def R(texto):
    """Referencia APA 7 con sangría francesa."""
    return Paragraph(texto, REF)


def url(u, etiqueta="URL"):
    return Paragraph(f"<b>{etiqueta}:</b> " + enlace(u), s["bullet"])
