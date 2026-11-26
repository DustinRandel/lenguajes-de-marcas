---
title: "XML y JSON"
subtitulo: "UT6. Dosier de apuntes"
modulo: "0373. Lenguajes de marcas y sistemas de gestión de información"
curso: "2026-2027"
profesor: "Dustin Randel de Lara García"
centro: "Sant Josep Obrer"
ut: "UT6"
---

# Cómo usar este dosier {.nobreak}

Hasta ahora el marcado servía para **mostrar** (HTML) o para **pintar** (CSS). XML y JSON sirven para **guardar e intercambiar datos** entre programas. Un archivo de alumnos, un catálogo, la respuesta de una API: no se ven como una página, se leen como un árbol de información.

Copia los ejemplos, ábrelos en el editor y, si puedes, en el navegador. Un XML mal cerrado se queja; un JSON con una coma de más también.

<!-- Notas del profesor: cronograma UF5 desde 13/04. Las diapositivas antiguas son imágenes; este dosier reconstruye el temario habitual (árbol XML, bien formado, JSON, cuándo usar cada uno). -->

## Qué vas a aprender

Al terminar esta unidad deberías ser capaz de:

- **Escribir** un XML bien formado, con una sola raíz y etiquetas propias.
- **Dibujar** el árbol de un documento XML.
- **Escribir** un JSON con objetos, arrays, strings y números.
- **Traducir** el mismo dato de XML a JSON y al revés.
- **Elegir** XML o JSON según quién lo va a leer.

## Índice

| | Bloque |
|---|---|
| [1](#bloque-1-xml-etiquetas-propias-y-un-arbol) | XML: etiquetas propias y un árbol |
| [2](#bloque-2-bien-formado-y-nombres) | Bien formado y nombres |
| [3](#bloque-3-json-datos-sin-etiquetas) | JSON: datos sin etiquetas |
| [4](#bloque-4-xml-o-json) | XML o JSON |
| A | Glosario |
| B | Mapa |
| C | Autoevaluación |

# Bloque 1. XML: etiquetas propias y un árbol

## 1.1 No es HTML con otro nombre

En HTML las etiquetas ya existen (`p`, `h1`, `a`). En XML **las inventas tú**, adaptadas al dato: `alumno`, `pelicula`, `pedido`. El navegador no sabe cómo pintarlas. Otro programa sí sabe leerlas.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<alumnos>
  <alumno>
    <nombre>Marta</nombre>
    <curso>1.º DAW</curso>
  </alumno>
  <alumno>
    <nombre>Pau</nombre>
    <curso>1.º DAW</curso>
  </alumno>
</alumnos>
```

La primera línea es la declaración. `alumnos` es la **raíz**: hay una y solo una. Cada `alumno` es un hijo, con sus propios hijos.

!!! definicion "XML"
    Lenguaje de marcas extensible para describir datos con etiquetas propias. Es un metalenguaje: con él se definen otros (RSS, SVG, XHTML). Su forma es un árbol con un único nodo raíz.

## 1.2 El árbol se lee de arriba abajo

```text
alumnos
  alumno
    nombre: Marta
    curso: 1.º DAW
  alumno
    nombre: Pau
    curso: 1.º DAW
```

Los atributos van en la apertura (`<alumno id="a1">`) y no tienen hijos. Si un dato tiene estructura, mejor un elemento hijo que un atributo.

!!! comprueba "Comprueba"
    1. ¿Puedes tener dos raíces en un XML?
    2. ¿El navegador pinta `<alumno>` como pinta `<p>`?
    3. Dibuja el árbol de un `pedido` con `cliente` y dos `linea` (producto y cantidad).

# Bloque 2. Bien formado y nombres

## 2.1 Reglas que no se negocian

Un XML **bien formado** cumple:

- Una sola raíz.
- Etiquetas cerradas, en orden (no se cruzan).
- Mayúsculas y minúsculas cuentan: `<Nombre>` no cierra `<nombre>`.
- Atributos con valor entre comillas.
- Caracteres especiales en el contenido: `&lt;`, `&gt;`, `&amp;`.

Si falta un cierre, el documento no vale. El navegador no «arregla» el XML como a veces hace con el HTML.

!!! ojo "Ojo"
    `<br>` suelto en XML no vale. O lo cierras (`<br></br>`) o la forma vacía (`<br/>`). En tus datos, casi nunca hace falta una etiqueta vacía.

## 2.2 Nombres de etiqueta

Empiezan por letra o `_`. No empiezan por número. Sin espacios. `1alumno` no vale; `alumno1` sí.

Los comentarios son `<!-- ... -->`, igual que en HTML. No se ven como dato.

!!! predice "Predice"
    ¿Este fragmento está bien formado? `<curso><nombre>DAW</Curso></nombre>`

!!! comprueba "Comprueba"
    1. ¿`<Alumno>` cierra `<alumno>`?
    2. ¿Hace falta `<?xml …?>` para que sea XML?
    3. ¿Cómo escribes el carácter `&` dentro de un texto?

# Bloque 3. JSON: datos sin etiquetas

## 3.1 Llaves, corchetes y comas

JSON no es un lenguaje de marcas: no hay etiquetas. Es texto con una sintaxis de objetos y listas, nació en JavaScript y lo usan casi todas las APIs.

```json
{
  "alumnos": [
    {"nombre": "Marta", "curso": "1.º DAW"},
    {"nombre": "Pau", "curso": "1.º DAW"}
  ]
}
```

| Qué | Cómo se escribe |
|---|---|
| Objeto | `{ "clave": valor, … }` |
| Array | `[ valor, valor, … ]` |
| String | `"entre comillas dobles"` |
| Número | `3`, `1.5` (punto, no coma) |
| Booleanos | `true`, `false` (minúsculas) |
| Nulo | `null` |

Las claves van siempre entre comillas dobles. Sin coma después del último elemento. Sin comentarios.

!!! definicion "JSON"
    Formato de texto para intercambiar datos: objetos y arrays, con tipos simples (string, número, boolean, null). No es un lenguaje de marcas.

## 3.2 El mismo dato, las dos formas

El XML de Marta y Pau de arriba es el JSON de este bloque. XML nombra cada pieza con una etiqueta. JSON nombra las claves del objeto. Los dos describen el mismo árbol.

!!! ojo "Ojo"
    En JSON el decimal es `1.5`, no `1,5`. Una coma de más al final de un array tumba el archivo entero.

!!! comprueba "Comprueba"
    1. ¿JSON es un lenguaje de marcas?
    2. Reescribe el JSON de alumnos como XML.
    3. ¿Vale `{nombre: Marta}` sin comillas?

# Bloque 4. XML o JSON

## 4.1 Quién lo va a leer

| | XML | JSON |
|---|---|---|
| Marcas | Sí, etiquetas propias | No |
| Árbol | Elementos e hijos | Objetos y arrays |
| Atributos | Sí | No (todo es clave de objeto) |
| Comentarios | Sí | No |
| Típico | Configuración, documentos, SVG | APIs web, JavaScript |

Si el dato lo consume JavaScript en el navegador, JSON. Si necesitas atributos, espacios de nombres o un documento largo con mezcla de texto y estructura, XML. Los dos son texto plano.

!!! ejemplo "Ejemplo"
    La lista de películas que pide la web del videoclub, JSON. Un recetario con párrafos, listas y metadatos que tiene que validar un esquema, XML.

!!! comprueba "Comprueba"
    1. ¿Dónde pondrías atributos, en XML o en JSON?
    2. Una API que devuelve tres productos al front: ¿qué formato esperas?
    3. ¿Por qué JSON no lleva comentarios?

# Anexo A. Glosario

| Término | Significado |
|---|---|
| Raíz | Único elemento que contiene a todos los demás en XML |
| Bien formado | XML que cumple las reglas de sintaxis |
| Metalenguaje | Lenguaje para definir otros lenguajes |
| JSON | Formato de datos con objetos y arrays |
| Array | Lista ordenada de valores, entre corchetes |
| Clave | Nombre de un campo en un objeto JSON |

# Anexo B. Mapa

```text
Datos (no páginas)
  XML: una raíz, etiquetas propias, árbol, bien formado
  JSON: { } y [ ], claves entre comillas, sin comentarios
  Mismo árbol, dos escrituras
  JS en el navegador suele hablar JSON
```

# Anexo C. Autoevaluación

## Preguntas cortas

1. Escribe un XML de dos películas con título y año, una sola raíz.
2. ¿Qué regla rompe `<a><b></a></b>`?
3. Escribe el JSON equivalente.
4. Cita dos diferencias entre XML y JSON.

## Tipo test

1. Un XML con dos elementos sueltos al mismo nivel, sin padre:
    - a) Está bien formado
    - b) Falta la raíz única
    - c) El navegador lo convierte a HTML
    - d) Es JSON
2. En JSON, `true`:
    - a) Va entre comillas
    - b) Va en minúsculas, sin comillas
    - c) Se escribe `True`
    - d) No existe, se usa `1`
3. Las claves de un objeto JSON:
    - a) Pueden ir sin comillas
    - b) Van entre comillas dobles
    - c) Van entre comillas simples
    - d) Solo si tienen un espacio

## Razona

Secretaría quiere un fichero de alumnos que lea un programa Java de hace quince años y, a la vez, la web nueva en JavaScript. ¿Un formato o dos? ¿Por qué?
