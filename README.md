# Plantilla de dosier FP (MkDocs)

Plantilla común para los dosieres de todos los módulos (CONT, BBDD, LLMA, DAW).
Autor: Dustin Randel de Lara García. Centro: Sant Josep Obrer.

## Reglas acordadas

- **Un sitio MkDocs por módulo**, todos con esta misma plantilla. Solo cambia el bloque «DATOS DEL MÓDULO» de `mkdocs.yml`.
- **En el repo público solo va teoría.** Nunca soluciones, claves de corrección ni exámenes: eso vive en Drive.
- **El `.md` es la fuente.** De él salen la web (GitHub Pages) y el PDF del dosier, que se sube a Drive y se enlaza en Classroom.
- **Notas para el profesor** en comentarios HTML (`<!-- ... -->`). El hook `hooks/notas_profesor.py` las quita de la web y `pdf/generar_pdf.py` las quita del PDF, **pero en un repo público siguen visibles en el `.md`**. Úsalas solo para organización (sesiones, fuentes, diapositivas que acompañan), nunca para soluciones.
- Unidades: `UT1`, `UT2`... Un archivo por UT: `docs/UT1-dosier.md`. Nunca el carácter punto medio en títulos ni nombres de archivo.
- Escribir para que se entienda: una idea por apartado, un buen ejemplo mejor que tres, frases cortas.

## Estructura

```text
mkdocs.yml                 configuración (cambia solo el bloque de datos del módulo)
requirements.txt           lo que necesita la web
requirements-pdf.txt       lo que necesita además el PDF
docs/.pages                menú lateral: una entrada por UT
docs/index.md              portada del sitio
docs/UT1-dosier.md         ejemplo de UT con todas las cajas
docs/imagenes/             imágenes de los dosieres
docs/assets/               icono de Dustin: logo.png (cabecera, blanco), logo-claro.png (portada del PDF, azul marino) y favicons (32 y 48 px, .ico)
overrides/main.html        añade a la web los favicons de 48 px y .ico
docs/stylesheets/extra.css estilo sobrio común
hooks/notas_profesor.py    quita las notas del profesor de la web
pdf/generar_pdf.py         genera el PDF desde el mismo .md
pdf/dosier-pdf.css         estilo del PDF
.github/workflows/deploy.yml  publica en GitHub Pages en cada push a main
```

## Cajas

Se escriben como admonitions de MkDocs. Úsalas solo cuando aporten:

```markdown
!!! definicion "Definición"
    Texto de la definición.

!!! ejemplo "Ejemplo"
    Un ejemplo bien elegido.

!!! ojo "Ojo"
    El error típico o la confusión habitual.

!!! predice "Predice"
    Una pregunta para pensar antes de seguir leyendo.

!!! comprueba "Comprueba"
    Algo que el alumnado puede verificar por sí mismo.
```

Al principio de cada UT va una caja `!!! abstract "Qué vas a aprender en esta UT"`.

## Cabecera de cada dosier

```yaml
---
title: UT1. Servicios y puertos
modulo: «Código» «Nombre del módulo»
ut: UT1
subtitulo: Dosier de apuntes
curso: 2026-2027
profesor: Dustin Randel de Lara García
centro: Sant Josep Obrer
---
```

## Ver la web en local

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
mkdocs serve        # http://127.0.0.1:8000
```

## Generar el PDF

```bash
pip install -r requirements-pdf.txt
python3 -m playwright install chromium
python3 pdf/generar_pdf.py docs/UT1-dosier.md      # -> pdf/salida/UT1-Dosier.pdf
```

Si ya tienes Chrome instalado, puedes usarlo con `CHROME=/ruta/a/chrome python3 pdf/generar_pdf.py ...`.
La portada del PDF lleva el icono de `docs/assets/logo-claro.png` si existe. El PDF lleva como autor a Dustin Randel de Lara García y no deja rastro de herramientas en los metadatos.
Para que salga igual que aquí conviene tener instaladas las fuentes Caladea, Carlito y Roboto Mono (todas libres, en Google Fonts).
