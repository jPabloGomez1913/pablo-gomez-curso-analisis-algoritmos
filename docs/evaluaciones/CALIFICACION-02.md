# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Juan Pablo Gómez Ramírez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `caa1640`

Muy buen trabajo: el laboratorio está completo, bien ordenado y apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 21 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **92 / 100** |
| **Nota (0–5)** | **4.60** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identificó que divide y vencerás empieza a ganar entre n = 50 y n = 100 según sus datos, y explicó por qué en tamaños pequeños las llamadas recursivas cuestan más de lo que ahorran.
- Comparó correctamente con el máximo de un arreglo: dividir da `T(n) = 2T(n/2) + Θ(1)`, que sigue siendo `Θ(n)`, igual que el recorrido simple, así que dividir no ayuda.
- Recomendó divide y vencerás, declaró que las cifras para 1.000.000 de registros son una estimación y las calculó escalando por la complejidad, no con regla de tres lineal.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación parte de un solo tamaño (n = 8000), cuya medición tiene mucha variación (las barras de la gráfica son amplias).
  → *Cómo corregirlo:* compare su estimación partiendo de otro tamaño grande, por ejemplo n = 4000, y diga si el resultado es parecido; eso le dice qué tanta confianza tiene en la cifra.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término: dos mitades, barrido lineal del caso cruzado y combinación constante.
- Resolvió con el método maestro, verificó que `f(n)` es del mismo orden que `n^(log_2 2)` y concluyó `Θ(n log n)`.
- Justificó que la fuerza bruta es `Θ(n²)` contando los n(n+1)/2 tramos.

**Lo que puede mejorar (y cómo corregirlo):**
- Para el caso base, solo indica que cuesta constante, pero no dice qué pasa con el tamaño de los subproblemas cuando n no es par.
  → *Cómo corregirlo:* agregue una frase sobre qué tamaño tienen las dos mitades cuando n es impar y por qué eso no cambia el orden del resultado.

## 3. Corrección de la implementación (21 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en la serie de ocho días, un elemento, todos negativos, todos positivos, un caso que cruza el punto medio y en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos con recursión propia, sin llamar a la fuerza bruta, y ninguna función cambia la lista recibida.
- `pruebas.py` cubre todos los casos pedidos y las veinte listas aleatorias; corre sin errores.
- Los tres archivos tienen *type hints* y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py`, `generar_entradas`, `graficar_tiempo_vs_tamanio` e `imprimir_resultados` tienen un docstring de una sola línea, sin las secciones `Args` y `Returns`.
  → *Cómo corregirlo:* complete cada docstring con las secciones `Args:` y `Returns:` como lo hizo en `subarreglo.py`.
- La función interna `rangos_error` no tiene docstring ni tipo de retorno.
  → *Cómo corregirlo:* agréguele docstring estilo Google con `Args` y `Returns`, y un *type hint* de lo que devuelve (`list[list[float]]`).

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica `tiempo_vs_n.png` tiene ambas curvas en los mismos ejes, título, ejes rotulados, leyenda y siete tamaños (incluidos dos menores de 100 y uno de 8000).
- Los valores del informe coinciden con la gráfica: en n = 8000 se ve fuerza bruta cerca de 5 s y divide y vencerás cerca de 0,04 s.
- Calculó los factores al duplicar n (3,57 para fuerza bruta y 1,80 para divide y vencerás), los contrastó con 4 y con 2,17, y fue prudente al decir que la variación impide afirmar una coincidencia exacta.
- Usó semilla fija, siete repeticiones, la misma lista para ambos algoritmos y verificó que las sumas coincidieran.

**Lo que puede mejorar (y cómo corregirlo):**
- El factor de divide y vencerás (1,80) queda por debajo de lo esperado y el informe no explica a qué podría deberse.
  → *Cómo corregirlo:* revise en la gráfica cuánto se amplía la barra de variación en esos dos tamaños y use eso para explicar la diferencia con lo que predice la teoría.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` está en la ubicación acordada, con `README.md`, `subarreglo.py`, `pruebas.py`, `medicion.py` y `graficas/tiempo_vs_n.png`.
- El informe sigue el orden pedido, trae su nombre, instrucciones de reproducción, enlaces al código en cada parte y la gráfica se incrusta con ruta relativa que funciona.
- Hay varios commits con mensajes descriptivos que tocan el laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones dan siempre la misma suma y no cambian la lista de entrada. `medicion.py` corre completo y genera la gráfica.
