# Laboratorio 2: Divide y vencerás

## Datos e instrucciones para reproducir el experimento

**Nombre completo:** Juan pablo gomez ramirez

Ejecuta estos comandos desde la raíz del repositorio:

```powershell
# Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Ejecutar las pruebas
python lab2-divide-y-vencer/pruebas.py

# Ejecutar la medición y generar la gráfica
python lab2-divide-y-vencer/medicion.py
```

## Parte 1 — Verificación de las soluciones

**Código:** [subarreglo.py](subarreglo.py) · [pruebas.py](pruebas.py)

### Verificación y casos cubiertos

Para comprobar que ambas soluciones eran correctan se uso la palabra reservada "assert" la cual nos permite verificar supociones y/o condiciones lógicas durante la ejecución del programa.

```python
assert subarreglo_fuerza_bruta(serie)[2] == 17
```

`[2]` -> accede al resultado de la suma  
`[2] == 17` -> valida que el resultado de la suma sea igual a `17`

Para comprbar la validez de ambos algoritmo se validaron varios casos:

#### El primer caso en ser probado fue el base

Serie: `-3   +5   -2   +8   -6   +3   +9   -4`

En este ya se nos daba la solución del sub arreglo máximo la cual era `17` y se uso como primera comprobación

```python
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17
```

#### Segunda comprobación se uso un solo valor

Serie: `[-3]`

```python
serie = [-3]
assert subarreglo_fuerza_bruta(serie)[2] == -3
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -3
```

#### Tercera comprobación todos los elementos negativos

Serie: `[-2, -1, -3, -4, -1, -2, -1, -5, -4]`

```python
serie = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
assert subarreglo_fuerza_bruta(serie)[2] == -1
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -1
```

#### Cuarta comprobación todos los elementos positivos

Serie: `[2, 1, 3, 4, 1, 2, 1, 5, 4]`

```python
serie = [2, 1, 3, 4, 1, 2, 1, 5, 4]
assert subarreglo_fuerza_bruta(serie)[2] == 23
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 23
```

#### Quinta comprobación el mejor tramo cruza el punto medio

Para serie = `[-2, 4, 3, -1, 5, -2]`

El punto medio está en el índice `2`. El mejor tramo va del índice `1` al `4`, así que cruza el punto medio. La suma máxima es `4 + 3 - 1 + 5 = 11`.

```python
serie = [-2, 4, 3, -1, 5, -2]
assert subarreglo_fuerza_bruta(serie)[2] == 11
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 11
```

#### Sexta comprobación 20 listas aleatorias

Se uso un generador de listas que recibe un `n` como tamaño de la lista  y genera número de manera aleatoria entre `(-100,100)`.

`serie[aleatoria]`

```python
def generar_entradas(n: int) -> list[int]:
    entrada = [random.randint(-100, 100) for _ in range(n)]
    random.shuffle(entrada)
    return entrada


for i in range(20):
    serie = generar_entradas(random.randint(1, 100))
    assert subarreglo_fuerza_bruta(serie)[2] == subarreglo_maximo(
        serie, 0, len(serie) - 1
    )[2]
```

## Parte 2 — Medición de tiempos

**Código:** [medicion.py](medicion.py)

![Gráfica de tiempo de ejecución según el tamaño de entrada](graficas/tiempo_vs_n.png)

### Procedimiento de medición

Para la medición del tiempo de ejecución de ambas funciones se uso la función:

```python
    perf_counter()
```
Los datos de prueba fueron generados aleatoriamente  y el tamaño de esta lista esta dado por : 
```python
    random.seed(42)
    tamanios = [10, 50, 100, 500, 1000, 4000, 8000]
    def generar_entradas(n: int) -> list[int]:
        entrada = [random.randint(-100,100) for _ in range(n)]
        random.shuffle(entrada)
        return entrada

```

para asegurar que solo se mide el tiempo de ejecución de la función y no de algo mas se uso la siguiente estructura

```python
   for tamanio in tamanios:
        serie = generar_entradas(tamanio)

        inicio_fuerza_bruta = perf_counter()
        subarreglo_fuerza_bruta(serie)
        fin_fuerza_bruta = perf_counter()
        tiempo_fuerza_bruta.append(fin_fuerza_bruta - inicio_fuerza_bruta)

```





## Parte 3 — Análisis

### 1. Recurrencia y complejidad

Para `n > 1`, `subarreglo_maximo` hace dos llamadas recursivas: una para la mitad izquierda y otra para la mitad derecha, cada una con aproximadamente `n/2` elementos. También busca el mejor tramo que cruza el punto medio. Ese barrido recorre las dos mitades una vez, por lo que cuesta `Θ(n)`; comparar los tres resultados cuesta `Θ(1)`. El caso base, con un solo elemento, cuesta `Θ(1)`. Por tanto:

```text
T(1) = Θ(1)
T(n) = 2T(n/2) + Θ(n)
```

En el método maestro, `a = 2`, `b = 2` y `f(n) = Θ(n)`. Como `n^(log_b(a)) = n^(log_2(2)) = n`, se cumple que `f(n) = Θ(n^(log_b(a)))`. Aplica el caso 2 del método maestro, con `k = 0`, y resulta `T(n) = Θ(n log n)`.

La fuerza bruta considera cada par de índices `(i, j)`, es decir, cada tramo contiguo. Hay `n(n+1)/2` tramos, que es `Θ(n²)`. Como extiende cada tramo sumando un elemento en tiempo constante, el trabajo total también es `Θ(n²)`.

### 2. Lo medido contra lo esperado

Al crecer `n`, ambas curvas aumentan, pero la de fuerza bruta crece mucho más rápido. Leyendo aproximadamente la gráfica para el par consecutivo `4000` y `8000`:

| Algoritmo | Tiempo con `n = 4000` | Tiempo con `n = 8000` | Multiplicador aproximado |
| --- | ---: | ---: | ---: |
| Fuerza bruta | `0,37 s` | `1,48 s` | `1,48 / 0,37 ≈ 4,0` |
| Divide y vencerás | `0,006 s` | `0,014 s` | `0,014 / 0,006 ≈ 2,3` |

Al duplicar `n`, `Θ(n²)` predice un factor de `4`. Para `Θ(n log n)`, el factor esperado entre `4000` y `8000` es `2 log₂(8000) / log₂(4000) ≈ 2,17`. Los factores observados son cercanos a esas predicciones. No coinciden exactamente porque cada tamaño se midió una sola vez y los tiempos dependen del ruido de ejecución; además, los valores de la tabla se leen de la gráfica.

### 3. Tamaños pequeños

En el rango medido, divide y vencerás empieza a ganar aproximadamente alrededor de `n = 100`: en los tamaños más pequeños, la fuerza bruta tarda igual o menos, y desde los tamaños mayores su ventaja de tiempo es clara. Para entradas pequeñas, las llamadas recursivas y el trabajo de dividir y combinar tienen un costo fijo que puede superar el ahorro de operaciones. El punto de cruce es aproximado porque las mediciones pequeñas duran muy poco y se hicieron una sola vez.

### 4. ¿Cuándo conviene dividir?

Para hallar el máximo de un arreglo, se puede dividir el arreglo en dos mitades, hallar el máximo de cada mitad y combinar los dos resultados comparándolos en tiempo constante. La recurrencia sería `T(n) = 2T(n/2) + Θ(1)`, que por el método maestro también da `Θ(n)`. Un recorrido lineal mantiene el máximo actual y cuesta `Θ(n)`. Dividir no mejora el orden de crecimiento y agrega llamadas recursivas, así que para este problema conviene el recorrido lineal.

### 5. Concepto para la gerente

Recomiendo divide y vencerás para procesar una serie de un millón de registros: su crecimiento `n log n` es mucho menor que el crecimiento cuadrático de la fuerza bruta. A partir de la gráfica, tomo como referencia aproximada `n = 8000`, con `1,48 s` para fuerza bruta y `0,014 s` para divide y vencerás. Las siguientes cifras son **estimaciones**, no mediciones directas:

- Fuerza bruta: `1,48 × (1.000.000 / 8.000)² = 1,48 × 125² ≈ 23.125 s`, es decir, alrededor de `6,4 horas`.
- Divide y vencerás: `0,014 × (1.000.000 log₂(1.000.000) / (8.000 log₂(8.000))) ≈ 0,014 × 192,2 ≈ 2,7 s`.

Estas proyecciones escalan cada tiempo según su complejidad (`n²` o `n log n`), no mediante una regla de tres lineal. El tiempo real dependerá del equipo, la implementación y las condiciones de ejecución.
