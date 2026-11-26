---
title: "JavaScript en el navegador"
subtitulo: "UT5. Dosier de apuntes"
modulo: "0373. Lenguajes de marcas y sistemas de gestión de información"
curso: "2026-2027"
profesor: "Dustin Randel de Lara García"
centro: "Sant Josep Obrer"
ut: "UT5"
---

# Cómo usar este dosier {.nobreak}

HTML describe. CSS pinta. JavaScript **reacciona**: un clic, un texto que cambia, un formulario que se comprueba antes de enviar. Es el primer lenguaje de programación del módulo, y se ejecuta en el navegador.

Copia los ejemplos a un `script.js` enlazado al final del `body`. F12, pestaña Consola, es donde salen los errores.

<!-- Notas del profesor: cronograma UF4 desde 18/02. Diapositivas antiguas «Introducción a interacción web con Javascript» y «JavaScript para Formularios». -->

## Qué vas a aprender

Al terminar esta unidad deberías ser capaz de:

- **Enlazar** un archivo `.js` al HTML y verlo ejecutar.
- **Declarar** datos con `let` y `const`.
- **Seleccionar** un elemento del DOM y cambiar su texto o su estilo.
- **Reaccionar** a un clic con `addEventListener`.
- **Explicar** por qué el script va al final del `body`.

## Índice

| | Bloque |
|---|---|
| [1](#bloque-1-que-es-javascript-y-como-se-incluye) | Qué es JavaScript y cómo se incluye |
| [2](#bloque-2-variables-y-funciones) | Variables y funciones |
| [3](#bloque-3-el-dom) | El DOM |
| [4](#bloque-4-eventos) | Eventos |
| A | Glosario |
| B | Mapa |
| C | Autoevaluación |

# Bloque 1. Qué es JavaScript y cómo se incluye

## 1.1 El tercer lenguaje del navegador

El navegador entiende HTML, CSS y JavaScript. Los dos primeros no ejecutan nada. JavaScript sí: tiene variables, condiciones, bucles y funciones.

!!! definicion "JavaScript"
    Lenguaje de programación que el navegador ejecuta. Sirve para reaccionar a lo que hace el usuario y para cambiar el documento que ya está en pantalla, sin recargar la página.

## 1.2 Un archivo externo, al final del body

```html
<body>
  <h1 id="titulo">Hola</h1>
  <button id="boton">Cambiar</button>
  <script src="script.js"></script>
</body>
```

El `script` al final asegura que el HTML ya está leído cuando el JS busca `#titulo`. Si lo pones en el `head` sin más, `getElementById` devuelve `null`.

!!! ojo "Ojo"
    `script.js` no es CSS: no va con `link rel="stylesheet"`. Va con `<script src="…">`. Y se cierra.

!!! comprueba "Comprueba"
    1. ¿JavaScript es un lenguaje de marcas?
    2. ¿Por qué el script se pone al final del body?
    3. ¿Qué pestaña de F12 enseña `console.log`?

# Bloque 2. Variables y funciones

## 2.1 let y const

```js
let contador = 0;
const PI = 3.14;
contador = contador + 1;
```

`let` se puede reasignar. `const` no. Los dos viven en el bloque donde los declaras. Olvida `var` en este módulo.

Las cadenas van con comillas. Los números, sin ellas. `===` compara valor y tipo (`"5" === 5` es falso).

## 2.2 Una función es un bloque con nombre

```js
function saludar(nombre) {
  return "Hola, " + nombre;
}

const saludar2 = (nombre) => "Hola, " + nombre;
```

Las dos formas se usan. Empieza por `function` hasta que te salga natural.

!!! comprueba "Comprueba"
    1. ¿Puedes hacer `PI = 3` si `PI` es `const`?
    2. ¿`"5" === 5`?
    3. ¿Dónde vive un `let` declarado dentro de una función?

# Bloque 3. El DOM

## 3.1 El HTML como árbol de objetos

Cuando el navegador lee el HTML, construye un árbol: el DOM. JavaScript habla con ese árbol, no con el archivo.

```js
const titulo = document.getElementById("titulo");
titulo.textContent = "Cartelera de la semana";
titulo.style.color = "teal";
```

`getElementById` devuelve **un** elemento. `querySelector(".ficha")` devuelve el primero que cumple el selector CSS. `querySelectorAll` devuelve una lista.

!!! definicion "DOM"
    Representación en árbol del documento HTML, viva en memoria. JavaScript la lee y la cambia: texto, atributos, clases, estilos.

`textContent` pone texto plano. `innerHTML` interpreta marcas: no lo uses con texto que venga del usuario.

## 3.2 Lo que cambias es el documento en pantalla

El archivo `index.html` no se reescribe. Si recargas, vuelves al HTML original. Eso es normal.

!!! predice "Predice"
    Un `h1` con id titulo. El script hace `document.getElementById("Titulo")` (mayúscula). ¿Qué sale en consola si luego haces `.textContent = "Hola"`?

!!! comprueba "Comprueba"
    1. ¿`getElementById` usa almohadilla?
    2. ¿Cuál es más seguro con texto del usuario, `textContent` o `innerHTML`?
    3. Si el script corre antes de existir el h1, ¿qué devuelve `getElementById`?

# Bloque 4. Eventos

## 4.1 El clic no es magia: te suscribes

```js
const boton = document.getElementById("boton");
const titulo = document.getElementById("titulo");

boton.addEventListener("click", () => {
  titulo.textContent = "Has pulsado";
});
```

`addEventListener` recibe el nombre del evento (`click`, `input`, `submit`) y una función. Cada clic ejecuta esa función.

!!! definicion "Evento"
    Suceso del documento o del usuario (clic, tecla, envío de formulario) al que JavaScript puede enganchar una función.

## 4.2 Un ejemplo que se prueba entero

```html
<h1 id="titulo">Hola</h1>
<button id="boton">Cambiar</button>
<script src="script.js"></script>
```

```js
document.getElementById("boton").addEventListener("click", () => {
  document.getElementById("titulo").textContent = "Hola, JavaScript";
});
```

Abre la página, pulsa, mira el título. En Consola no debería haber errores en rojo.

!!! ojo "Ojo"
    `onclick="…"` en el HTML mezcla marcado y programa. En este módulo, los eventos van en el `.js`.

!!! comprueba "Comprueba"
    1. ¿Qué dos argumentos recibe `addEventListener`?
    2. ¿Hace falta recargar para ver el cambio de `textContent` después de un clic?
    3. ¿Dónde escribirías el `addEventListener`, en el HTML o en el JS?

# Anexo A. Glosario

| Término | Significado |
|---|---|
| JavaScript | Lenguaje de programación del navegador |
| DOM | Árbol en memoria del HTML |
| `let` / `const` | Declaración de datos; `const` no se reasigna |
| `getElementById` | Busca un elemento por su id, sin almohadilla |
| `textContent` | Texto plano de un elemento |
| Evento | Clic, tecla, envío… |
| `addEventListener` | Engancha una función a un evento |

# Anexo B. Mapa

```text
HTML (estructura) + CSS (aspecto) + JS (comportamiento)
  script src al final del body
  let / const / function
  document.getElementById / querySelector
  textContent, style
  addEventListener("click", …)
```

# Anexo C. Autoevaluación

## Preguntas cortas

1. ¿Por qué JavaScript no es un lenguaje de marcas?
2. Escribe el `script` para enlazar `app.js` al final del body.
3. Diferencia `textContent` e `innerHTML`.
4. Escribe el `addEventListener` de un botón que ponga «Ok» en un párrafo.

## Tipo test

1. `getElementById("titulo")` busca:
    - a) `#titulo` en CSS
    - b) El id `titulo`, sin almohadilla
    - c) Todas las clases `titulo`
    - d) El tag `titulo`
2. `const n = 1; n = 2;`:
    - a) Vale, n pasa a 2
    - b) Error: const no se reasigna
    - c) Vale solo dentro de una función
    - d) Vale si n era un string
3. El script en el `head` sin esperar al HTML:
    - a) Encuentra igual los id
    - b) Puede devolver `null`
    - c) Convierte el HTML en DOM dos veces
    - d) Ignora el CSS

## Razona

Un compañero pone `onclick="cambiar()"` en el botón y la función en un `script` del `head`. El botón «no hace nada». ¿Por qué y cómo lo harías tú?
