# Laboratorio 3: Listas enlazadas y tablas hash

## Datos e instrucciones para reproducir el experimento

**Nombre completo:** Juan pablo gomez ramirez

Ejecuta estos comandos desde la raíz del repositorio:

```powershell
# Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Ejecutar las pruebas
python lab3-tablas-hash/pruebas.py

# Ejecutar la medición y generar las gráficas
python lab3-tablas-hash/medicion.py
```

## Parte 1 — Verificación de las estructuras

**Código:** [estructuras.py](estructuras.py) · [pruebas.py](pruebas.py)

### Verificación y casos cubiertos

Se verificó con `assert`, que detiene el programa si una condición lógica no se cumple. Las pruebas cubren:

- **Búsqueda en la lista:** una guía existente devuelve su estado y una inexistente devuelve `None`. También se comprueba `tamano` y que la última guía insertada quede en la cabeza.
- **Búsqueda en la tabla:** una exitosa y una infructuosa, con `TablaHash(7)` y las guías `10`, `24` y `17`.
- **Colisión forzada:** con `m = 7`, las guías `10`, `24` y `17` caen en la casilla 3. Se comprueba que las tres se insertan y se encuentran después, que la lista de esa casilla tiene longitud 3 y que las otras seis casillas quedan vacías.
- **Factor de carga:** `factor_carga()` da `0` con la tabla vacía y `3 / 7` tras esas tres inserciones.
- **Colecciones aleatorias:** 30 colecciones con semilla fija, con `m` entre 7, 11, 61 y 101. En cada una, para guías existentes y para guías inexistentes, la lista y la tabla devuelven lo mismo.

```python
tabla = TablaHash(7)
for guia in (10, 24, 17):
    tabla.insertar(guia, "en bodega")

assert tabla.buscar(24) == "en bodega"
assert tabla.buscar(99) is None
assert tabla.factor_carga() == 3 / 7
```

## Parte 2 — Medición de tiempos

**Código:** [medicion.py](medicion.py)

### Experimento A — Lista frente a tabla

![Tiempo medio por búsqueda de guías inexistentes: lista frente a tabla hash](graficas/lista_vs_tabla.png)

### Experimento B — Efecto del factor de carga

![Tiempo medio por búsqueda frente al factor de carga, con n fijo](graficas/tiempo_vs_alfa.png)

### Procedimiento de medición

Las guías son enteros distintos de diez dígitos, generados con semilla fija (`2026`). Las 200 guías inexistentes salen de `generar_guias_inexistentes` con semilla `7`. Lista y tabla reciben las mismas guías en cada valor de `n`. `time.perf_counter()` cronometra solo el ciclo de búsquedas, nunca la construcción ni la generación de datos. Cada punto es la mediana de 5 tandas de 200 búsquedas, expresada como tiempo medio por búsqueda. Antes de medir, el script comprueba que lista y tabla devuelven el mismo estado para una muestra de 100 guías existentes.

En el experimento A, `m` es el primo más cercano a `n / 2`:

| `n` | 100 | 500 | 1.000 | 5.000 | 20.000 | 50.000 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `m` | 47 | 251 | 499 | 2.503 | 10.007 | 24.989 |
| `α` | 2,13 | 1,99 | 2,00 | 2,00 | 2,00 | 2,00 |

En el experimento B, `n = 20.000` y `m` es el primo más cercano a `n / α`:

| `α` objetivo | 0,25 | 0,5 | 1 | 2 | 4 | 10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `m` | 79.999 | 40.009 | 19.997 | 10.007 | 4.999 | 1.999 |

Tiempos medios por búsqueda de una guía inexistente:

| `n` | Lista (µs) | Tabla (µs) |
| ---: | ---: | ---: |
| 100 | 3,867 | 0,271 |
| 500 | 19,198 | 0,266 |
| 1.000 | 40,320 | 0,268 |
| 5.000 | 212,817 | 0,333 |
| 20.000 | 865,701 | 0,170 |
| 50.000 | 1692,625 | 0,224 |

| `α` | 0,25 | 0,5 | 1 | 2 | 4 | 10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Tabla (µs) | 0,108 | 0,119 | 0,201 | 0,295 | 0,296 | 1,300 |

## Parte 3 — Análisis

### 1. Costo teórico

Para una guía inexistente, la lista no puede detenerse antes: compara contra los `n` nodos y solo al final concluye que no está. El trabajo crece en proporción a `n`, es decir, `Θ(n)`. En la tabla, calcular `guia % m` cuesta `Θ(1)` y luego solo se recorre la cadena de esa casilla. Si la función reparte las guías de manera pareja, cada cadena mide en promedio `n / m = α`, y una búsqueda sin éxito la recorre completa: `Θ(1 + α)`, donde el 1 es el cálculo del hash y `α` el recorrido.

El supuesto es el hash uniforme simple: cada guía tiene la misma probabilidad de caer en cualquier casilla, sin depender de las demás. Si todas cayeran en la misma casilla, habría una sola cadena de `n` nodos y `m − 1` casillas vacías. Buscar costaría `Θ(n)`, igual que en la lista, aunque `α` fuera 0,5.

### 2. Lo medido contra lo esperado

De `n = 1.000` a `n = 5.000` (`n` se multiplica por 5), la lista pasa de 40,3 µs a 212,8 µs: el tiempo se multiplica por 5,3. Coincide con `Θ(n)`. La tabla pasa de 0,268 µs a 0,333 µs: se multiplica por 1,24, casi plana, como `Θ(1)` con `α` fijo cerca de 2. No todo encaja perfecto: de 20.000 a 50.000 (`n` × 2,5) la lista solo se multiplica por 1,96, y la tabla sube y baja (0,33 µs en 5.000 y 0,17 µs en 20.000). Con tiempos tan pequeños el ruido pesa, así que solo afirmo la tendencia.

En la segunda gráfica, el tiempo crece con `α`: 0,108 µs con `α = 0,25`, 0,201 µs con `α = 1` y 1,300 µs con `α = 10`. De `α = 1` a `α = 10` se multiplica por 6,5, y `Θ(1 + α)` predice 11/2 = 5,5. Es coherente: hay una parte constante (hash y acceso a la casilla) y otra proporcional a `α`. Entre `α = 2` y `α = 4` el tiempo es casi igual (0,295 y 0,296 µs); lo atribuyo a ruido de medición.

### 3. Colisiones

Una colisión ocurre cuando dos guías distintas dan la misma casilla. Pasa aunque la tabla tenga más casillas que guías: las guías posibles (hasta 10¹⁰) son muchísimas más que las `m` casillas. Ejemplo con `m = 7`: `10 mod 7 = 3`, `24 mod 7 = 3` y `17 mod 7 = 3`, así que las tres quieren la casilla 3.

**Encadenamiento:** cada casilla guarda una lista. Las tres guías quedan enlazadas en la casilla 3 (longitud 3) y las otras seis casillas quedan vacías. Ventaja: es simple, nunca se llena, `α` puede superar 1 y borrar es fácil. Costo: memoria extra por los punteros y cadenas que se alargan.

**Direccionamiento abierto:** todo se guarda dentro del arreglo y, si la casilla está ocupada, se prueba otra. Con sondeo lineal: `10` va a la casilla 3, `24` a la 4 y `17` a la 5. Ventaja: no hay punteros y aprovecha mejor la caché. Costo: `α` debe ser menor que 1, los bloques ocupados alargan los sondeos y borrar exige marcas especiales.

### 4. Tabla hash o árbol de búsqueda

La tabla hash no sirve para rangos. La función dispersa a propósito: guías consecutivas caen en casillas lejanas, sin orden. Para "entre X y Y" habría que revisar todas las guías, `Θ(n + m)`. Un árbol binario de búsqueda guarda las claves en orden: se baja hasta X en `O(h)` y se recorre en orden hasta Y, con costo `O(h + k)` para `k` guías dentro del rango.

Si las 400.000 guías llegaran ordenadas, cada una sería hijo derecho de la anterior y el árbol sería una cadena de altura 399.999. Insertar la guía número `i` cuesta `i` comparaciones, así que construirlo cuesta unas `n²/2 ≈ 8×10¹⁰` comparaciones, y buscar una guía inexistente, unas 400.000. Un árbol equilibrado tiene altura `⌊log₂ 400.000⌋ = 18`: una búsqueda hace unas 19 comparaciones y construirlo cuesta unas `n log₂ n ≈ 7,4×10⁶`. Cada búsqueda es unas 20.000 veces más barata.

### 5. Concepto para la jefa de operaciones

Recomiendo una combinación: una tabla hash para consultar una guía exacta (`Θ(1 + α)`) y un árbol de búsqueda equilibrado (AVL o rojinegro) para los rangos. Cada envío se registra en ambas.

**Estimación, no medición,** para una guía inexistente con 5.000.000 de envíos:

- **Lista:** en mi primera gráfica, con ejes logarítmicos, la curva es una recta de pendiente cercana a 1, es decir, tiempo ≈ `c · n`. De mis seis valores de `n` sale `c ≈ 0,04 µs` por nodo (entre 0,034 y 0,043). Con `n = 5×10⁶` da unos 0,2 s. Probablemente es una cota inferior, porque la lista ya no cabría en la caché.
- **Tabla:** mi curva es plana (0,17 a 0,33 µs) porque el costo depende de `α` y no de `n`. Si mantengo `α ≈ 2` (`m` primo cerca de 2.500.000), estimo del orden de 0,3 µs, quizá algo más por la caché.

Sería una diferencia de entre 10⁵ y 10⁶ veces. Esto solo vale si la tabla se agranda al crecer `n` para conservar `α`; con `m` fijo, `α` crecería con `n` y la tabla se acercaría a una lista.