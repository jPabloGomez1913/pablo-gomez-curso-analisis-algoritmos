# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Juan Pablo Gomez Ramirez · **Laboratorio:** Fundamentos, complejidad y recurrencias (Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `95e0a0f`

Muy buen trabajo: el informe es claro, está bien razonado y se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 24 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 19 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que se produzca dentro de las cuatro horas, y nombra la restricción incumplida.
- Explica por qué un servidor del doble de velocidad solo reduce el tiempo a la mitad y el problema vuelve a aparecer al crecer los datos.
- Su segundo ejemplo (el listado de inventario sin paginación) es propio e indica qué se procesa, cuántos datos hay y qué límite de tiempo se incumple.
- En la parte ética señala dos perjuicios concretos y dice quién asume el costo en cada uno; la discusión sobre desempates y vigilancia del tiempo es muy buena.

**Lo que puede mejorar:**
- La parte ambiental usa horas "ilustrativas" (6 u 8 horas). Un cálculo sencillo de energía con valores medidos o estimados (por ejemplo, kWh por noche por 365 noches) la haría más sólida.
- En el segundo perjuicio ético podría ser más claro nombrar a un paciente concreto afectado, no solo "el paciente".

## 2. Calidad de la explicación teórica (24 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué conjunto de entradas y con qué tamaño fijo se toma cada uno, y justifica que usaría el peor caso.
- Dejó escrita la predicción antes del experimento y la contrastó después.
- La recurrencia de merge sort está explicada término por término y resuelta con árbol de recursión, con costo por nivel, número de niveles y costo total.
- El cálculo línea a línea de insertion sort es completo y la tabla de complejidades está presente.

**Lo que puede mejorar:**
- Al usar la notación Θ en el mejor caso de insertion sort, aclare que se refiere a la lista ya en el orden que el algoritmo produce.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (probadas con listas aleatorias, vacías y con repetidos), no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `list.sort()`.
- `merge_sort` tiene su propia mezcla recursiva.
- Los tres generadores dan listas del tamaño pedido, con valores distintos y semilla reproducible; el escenario B deja el 98 % ordenado y el 2 % al final.
- Tiene type hints y docstrings en todas las funciones.

## 4. Calidad del análisis de las gráficas (19 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con nombre y unidades y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con datos que C es el peor caso, B el mejor y A se acerca al promedio, y explica por qué B no fue lineal.
- En la Parte 4 compara el crecimiento de ambas curvas, lo contrasta con las complejidades calculadas y explica lo ocurrido con tamaños pequeños.
- El concepto técnico recomienda merge sort, responde sobre el servidor con datos medidos, extrapola a 1.200.000 registros declarándolo como estimación y discute memoria y desempates.

**Lo que puede mejorar:**
- La extrapolación se basa en una sola medición (n = 6.400); mencionar que a tamaños mayores el comportamiento de la máquina puede cambiar (memoria, caché) la haría más honesta.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos están donde y como se pidió, el informe sigue el orden de las partes, las gráficas se ven incrustadas con rutas correctas y cada parte práctica enlaza su código.
- Las instrucciones para reproducir son claras.

**Lo que puede mejorar:**
- Solo hay dos commits que tocan este laboratorio, y se pedían al menos cinco que muestren el avance.
- Los mensajes "Laboratorio 1" y "Formateo" no dicen qué se hizo; use mensajes como "Implementa insertion_sort con conteo de comparaciones".
- Su nombre aparece en minúsculas ("Juan pablo gomez ramirez"); escríbalo con mayúsculas iniciales.

## ¿El código funciona?
Sí. Los scripts corren sin errores, ordenan correctamente y generan las gráficas en la carpeta `graficas/`. Los tiempos al ejecutarlos son distintos a los suyos, pero las conclusiones son las mismas.

## Para el próximo laboratorio
- Haga commits pequeños y frecuentes, con mensajes que describan el cambio.
- Respalde los cálculos de energía con números, aunque sean estimados.
- Aclare los supuestos de las extrapolaciones y los límites de lo medido.
