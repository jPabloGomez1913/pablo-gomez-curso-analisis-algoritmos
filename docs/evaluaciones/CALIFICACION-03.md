# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Juan Pablo Gómez Ramírez · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `ad40f79`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 8 / 25 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **76 / 100** |
| **Nota (0–5)** | **3.80** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Explica bien la colisión con el ejemplo de `10`, `24` y `17` con `m = 7`, y compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica que la tabla hash no sirve para rangos y que el árbol sí, y estima la altura y las comparaciones del árbol degenerado frente al equilibrado.
- La recomendación (tabla hash más árbol equilibrado) está clara y la estimación a 5.000.000 de envíos está declarada como estimación, con su razonamiento.

**Lo que puede mejorar (y cómo corregirlo):**
- Para estimar la lista a 5.000.000 usa una gráfica con ejes logarítmicos que no está publicada, así que el lector no puede comprobar la pendiente que menciona.
  → *Cómo corregirlo:* publique la gráfica en la que se apoya, o cite la tabla de valores medidos que sí está en el informe.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Explica por qué buscar una guía inexistente recorre los `n` nodos, y de dónde sale `Θ(1 + α)` en la tabla.
- Nombra el supuesto de hash uniforme y explica que, si todas las guías caen en una casilla, la tabla se vuelve tan lenta como la lista.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` devuelven el estado correcto, también para guías que no existen. La tabla reutiliza la lista, sin `dict`, `set` ni `hash()`.
- Las pruebas cubren la colisión forzada con `m = 7`, el factor de carga `3 / 7` y 30 colecciones aleatorias.
- Las funciones tienen *type hints* y *docstrings* con `Args` y `Returns`.

## 4. Calidad del análisis de las gráficas (8 / 25)
**Lo que hizo bien:**
- El código de `medicion.py` produce las dos gráficas con título, ejes rotulados y leyenda, con seis valores de `n` y seis de `α`.
- En la pregunta 2 calcula factores de crecimiento y los compara con `Θ(n)`, `Θ(1)` y `Θ(1 + α)`, y comenta con honestidad el ruido de la medición.

**Lo que puede mejorar (y cómo corregirlo):**
- Las imágenes `lista_vs_tabla.png` y `tiempo_vs_alfa.png` no se subieron al repositorio: no existe la carpeta `graficas/` dentro del laboratorio. No se pudo revisar ninguna gráfica, y los valores del análisis no se pueden contrastar con ellas.
  → *Cómo corregirlo:* ejecute `medicion.py`, compruebe que aparecen los dos PNG en `graficas/` y súbalos al repositorio junto con el resto del trabajo.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, trae su nombre, enlaza `estructuras.py`, `pruebas.py` y `medicion.py`, y explica cómo midió, con tablas de `m` y `α`.
- Hay cinco commits sobre el laboratorio, con mensajes comprensibles.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió la estructura de entrega: faltan los archivos `graficas/lista_vs_tabla.png` y `graficas/tiempo_vs_alfa.png`, así que las dos imágenes del informe aparecen rotas en GitHub.
  → *Cómo corregirlo:* suba la carpeta `graficas/` con los dos PNG y verifique en la vista web de GitHub que se ven.
- Las instrucciones de reproducción apuntan a una carpeta que no existe (`lab3-tablas-hash/`); la carpeta real es `lab3-estructuras-datos/`.
  → *Cómo corregirlo:* cambie las dos rutas de los comandos por `lab3-estructuras-datos/pruebas.py` y `lab3-estructuras-datos/medicion.py`.
- Un par de commits tienen mensajes muy parecidos ("Agrega la medición", "agrega la medicion").
  → *Cómo corregirlo:* describa en cada mensaje qué cambió concretamente.

## ¿El código funciona?
Sí. Las pruebas pasan todas y `medicion.py` corre completo, mostrando que la lista crece con `n` y la tabla se mantiene casi plana. Genera las gráficas al ejecutarlo, pero los PNG no quedaron publicados.
