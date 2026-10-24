# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Juan Pablo Gómez Ramírez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `3624397`

Muy buen trabajo con el código y con la teoría.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 15 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **82 / 100** |
| **Nota (0–5)** | **4.10** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- Comparó con el máximo de un arreglo y justificó con el costo de combinar (`T(n) = 2T(n/2) + Θ(1)` da `Θ(n)`, igual que el recorrido simple).
- Recomendó divide y vencerás y declaró que las cifras para 1.000.000 de registros son estimaciones, escaladas con `n²` y `n log n` y no con una regla de tres lineal.

**Lo que puede mejorar:**
- Las estimaciones parten de tiempos (1,48 s y 0,014 s con n = 8000) que no coinciden con su gráfica publicada, donde fuerza bruta marca cerca de 2,4 s y divide y vencerás cerca de 0,025 s. Por eso las cifras finales quedan mal ancladas.
- Dice que divide y vencerás gana "alrededor de n = 100", pero en su gráfica esa zona no se distingue. Una tabla con los tiempos medidos habría respaldado esa afirmación.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término y verificó la condición del caso 2 del método maestro.
- Justificó bien por qué la fuerza bruta es `Θ(n²)` (n(n+1)/2 tramos, cada uno en tiempo constante).

**Lo que puede mejorar:**
- Aclarar un poco más por qué el caso cruzado recorre exactamente las dos mitades una sola vez.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta, y ninguna función modifica la lista recibida.
- Tiene *type hints*, *docstrings* y el código cumple PEP 8.

**Lo que puede mejorar:**
- Las pruebas aleatorias no usan semilla fija, así que no son exactamente repetibles.

## 4. Calidad del análisis de las gráficas (15 / 25)
**Lo que hizo bien:**
- La gráfica existe, tiene ambas curvas en los mismos ejes, título, ejes rotulados, leyenda y siete tamaños (de 10 a 8000).
- Calculó el factor de crecimiento al duplicar n y lo comparó con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Los valores de su tabla no se leen en la gráfica publicada. Allí fuerza bruta pasa de cerca de 0,95 s (n = 4000) a cerca de 2,4 s (n = 8000), un factor de unos 2,5; y divide y vencerás pasa de cerca de 0,007 s a cerca de 0,025 s. Su informe dice 4,0 y 2,3, y concluye que coinciden con la teoría, cuando su propia gráfica no lo muestra.
- Medir cada tamaño una sola vez deja mucho ruido; repetir y promediar da factores más confiables.
- Las afirmaciones del informe deben salir de lo que realmente muestra la gráfica entregada.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- Informe en el orden pedido, con nombre, instrucciones, enlaces al código en cada parte y la gráfica visible.
- Más de tres commits con mensajes descriptivos.

**Lo que puede mejorar:**
- No siguió la estructura acordada: hay una carpeta `graficas/` suelta en la raíz del repositorio con otra copia (distinta) de `tiempo_vs_n.png`, además de la que está dentro de `lab2-divide-y-vencer/`. Debe quedar solo la del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, las dos soluciones dan siempre la misma suma y la medición corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Copie en el informe los valores que realmente lee de la gráfica que entrega, o agregue una tabla con los tiempos medidos.
- Repita cada medición varias veces y use el promedio o la mediana.
- Si cambia el código o vuelve a medir, regenere la gráfica y revise que el informe siga coincidiendo.
- Mantenga una sola carpeta de gráficas, dentro de la carpeta del laboratorio.
- Use una semilla fija también en las pruebas aleatorias.
