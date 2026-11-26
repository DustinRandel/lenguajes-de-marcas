#!/usr/bin/env python3
"""Diagramas de la UT3 (CSS). Se ejecuta desde docs/imagenes/."""
import html
import subprocess
from pathlib import Path

F = 'font-family="Carlito"'


def box(x, y, w, h, fill, stroke, lines, col="#1f2937", bold0=True, size=20, anchor="middle", mono=False):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'
    n = len(lines)
    lh = size * 1.35
    y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.33
    for i, l in enumerate(lines):
        fam = 'font-family="Roboto Mono"' if mono else F
        wt = "bold" if (bold0 and i == 0 and not mono) else "normal"
        tx = x + w / 2 if anchor == "middle" else x + 18
        s += (
            f'<text x="{tx}" y="{y0 + i * lh}" {fam} font-size="{size}" font-weight="{wt}" '
            f'fill="{col}" text-anchor="{anchor}">{html.escape(l)}</text>'
        )
    return s


def text(x, y, t, size=20, col="#1f2937", w="normal", a="start", i=False):
    st = ' font-style="italic"' if i else ""
    return (
        f'<text x="{x}" y="{y}" {F} font-size="{size}" font-weight="{w}" fill="{col}" '
        f'text-anchor="{a}"{st}>{html.escape(t)}</text>'
    )


def arrow(x1, y1, x2, y2, col="#6b7280"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="3" marker-end="url(#a)"/>'


DEF = (
    '<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#6b7280"/></marker></defs>'
)
G = ("#e6f4f1", "#0f766e", "#0f766e")
P = ("#ecebff", "#4f46e5", "#3730a3")
O = ("#fff3e0", "#c2750f", "#8a4b00")


def save(name, w, h, body):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">'
        f'{DEF}<rect width="100%" height="100%" fill="white"/>{body}</svg>'
    )
    Path(name + ".svg").write_text(svg)
    subprocess.run(["magick", "-density", "192", name + ".svg", name + ".png"], check=True)


# 1. Tres formas de incluir CSS
b = text(30, 40, "Tres sitios donde escribir CSS", 28, w="bold")
b += box(30, 70, 300, 230, *O[:2], ["En el elemento", "atributo style", "Casi nunca:", "hay que repetirlo"], col=O[2], size=20)
b += box(350, 70, 300, 230, *P[:2], ["En el documento", "etiqueta <style>", "Pruebas rápidas", "o una sola página"], col=P[2], size=20)
b += box(670, 70, 300, 230, *G[:2], ["Archivo externo", "<link> + .css", "Siempre en un", "proyecto real"], col=G[2], size=20)
b += text(30, 340, "El archivo externo es el único que reutilizas en todas las páginas.", 19, "#6b7280", i=True)
save("UT3-tres-formas", 1000, 370, b)

# 2. Anatomía de una regla
b = text(30, 40, "Anatomía de una regla CSS", 28, w="bold")
b += box(80, 90, 220, 90, *P[:2], ["selector"], col=P[2], size=24, mono=True, bold0=False)
b += text(330, 145, "{", 40, "#1f2937", w="bold")
b += box(370, 70, 280, 70, *G[:2], ["propiedad: valor;"], col=G[2], size=20, mono=True, bold0=False)
b += box(370, 155, 280, 70, *G[:2], ["propiedad: valor;"], col=G[2], size=20, mono=True, bold0=False)
b += text(670, 145, "}", 40, "#1f2937", w="bold")
b += text(190, 250, "A quién se aplica", 18, P[2])
b += text(430, 250, "Qué cambia y cómo", 18, G[2])
b += text(30, 330, "Cada declaración acaba en punto y coma. El selector decide el alcance.", 19, "#6b7280", i=True)
save("UT3-anatomia-regla", 1000, 360, b)

# 3. Especificidad
b = text(30, 40, "Quién gana cuando dos reglas chocan", 28, w="bold")
b += box(30, 80, 180, 120, "#f8fafc", "#9ca3af", ["etiqueta", "p", "(0, 0, 1)"], col="#374151", size=20)
b += box(230, 80, 200, 120, *P[:2], ["clase", ".aviso", "(0, 1, 0)"], col=P[2], size=20)
b += box(450, 80, 200, 120, *O[:2], ["identificador", "#menu", "(1, 0, 0)"], col=O[2], size=20)
b += box(670, 80, 280, 120, *G[:2], ["atributo style", "en el elemento", "por encima"], col=G[2], size=20)
b += text(30, 240, "Se compara de izquierda a derecha: un id gana a cualquier cantidad de clases.", 19, "#6b7280", i=True)
b += text(30, 275, "Si empatan, gana la regla escrita más abajo. !important gana a todo: evítalo.", 19, "#6b7280", i=True)
save("UT3-especificidad", 1000, 310, b)

# 4. Modelo de caja
b = text(30, 40, "El modelo de caja", 28, w="bold")
# outer margin
b += f'<rect x="80" y="70" width="840" height="280" rx="12" fill="#fff3e0" stroke="#c2750f" stroke-width="2.5"/>'
b += text(100, 100, "margin", 18, O[2], w="bold")
# border
b += f'<rect x="160" y="115" width="680" height="210" rx="12" fill="#ecebff" stroke="#4f46e5" stroke-width="2.5"/>'
b += text(180, 145, "border", 18, P[2], w="bold")
# padding
b += f'<rect x="240" y="160" width="520" height="140" rx="12" fill="#e6f4f1" stroke="#0f766e" stroke-width="2.5"/>'
b += text(260, 190, "padding", 18, G[2], w="bold")
# content
b += box(340, 205, 320, 70, "#f8fafc", "#9ca3af", ["contenido"], col="#374151", size=22, bold0=False)
b += text(30, 375, "De fuera a dentro: margen, borde, relleno y contenido. El fondo no pinta el margen.", 19, "#6b7280", i=True)
save("UT3-modelo-caja", 1000, 400, b)

# 5. content-box vs border-box
b = text(30, 40, "content-box frente a border-box", 28, w="bold")
b += text(30, 80, "Misma receta: width 300, padding 20, border 5", 19, "#6b7280", i=True)
b += box(30, 110, 450, 200, *O[:2], ["content-box", "width = solo contenido", "Total: 350 px", "300 + 20 + 20 + 5 + 5"], col=O[2], size=20)
b += box(520, 110, 450, 200, *G[:2], ["border-box", "width incluye padding y borde", "Total: 300 px", "el contenido encoge"], col=G[2], size=20)
b += text(30, 350, "En un proyecto real se pone * { box-sizing: border-box; } y width es lo que ocupa.", 19, "#6b7280", i=True)
save("UT3-box-sizing", 1000, 380, b)

# 6. display
b = text(30, 40, "Tres valores de display", 28, w="bold")
b += box(30, 80, 300, 200, *G[:2], ["block", "Todo el ancho", "Línea nueva", "Respeta width"], col=G[2], size=20)
b += box(350, 80, 300, 200, *O[:2], ["inline", "En la línea", "Ignora width", "y height"], col=O[2], size=20)
b += box(670, 80, 300, 200, *P[:2], ["inline-block", "En la línea", "Respeta width", "y height"], col=P[2], size=20)
b += text(30, 320, "display: none oculta el elemento y su hueco. visibility: hidden deja el hueco.", 19, "#6b7280", i=True)
save("UT3-display", 1000, 360, b)
