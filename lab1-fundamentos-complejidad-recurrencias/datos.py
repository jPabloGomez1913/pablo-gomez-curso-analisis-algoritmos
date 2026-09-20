"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random

FRACCION_NUEVOS = 0.02  # escenario B: 2% de resultados nuevos al final


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    return rng.sample(range(n), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    rng = random.Random(semilla)

    # Punto de partida: permutacion aleatoria de 0..n-1 (enteros distintos).
    lote = rng.sample(range(n), n)

    # El 2% final es nuevo; el 98% restante corresponde a la lista de ayer.
    n_nuevos = round(FRACCION_NUEVOS * n)
    n_ordenados = n - n_nuevos

    nuevos = lote[n_ordenados:]

    # Como los indices son distintos y van de 0 a n-1, se construye la
    # lista de ayer de mayor a menor excluyendo los nuevos, sin ordenar.
    es_nuevo = [False] * n
    for valor in nuevos:
        es_nuevo[valor] = True
    ordenados = [v for v in range(n - 1, -1, -1) if not es_nuevo[v]]

    return ordenados + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    # El algoritmo produce el orden de mayor a menor riesgo, asi que el
    # orden inverso es de menor a mayor. Es determinista: no usa semilla.
    return list(range(n))
