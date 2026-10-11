"""Medición de tiempos para las soluciones de subarreglo máximo."""

import random
from time import perf_counter

import matplotlib
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

matplotlib.use("Agg")


def generar_entradas(n: int) -> list[int]:
    """Genera una lista aleatoria de n enteros entre -100 y 100.

    Args:
        n: Cantidad de elementos que tendrá la lista.

    Returns:
        Lista de enteros generada aleatoriamente.
    """
    entrada = [random.randint(-100, 100) for _ in range(n)]
    random.shuffle(entrada)
    return entrada


def graficar_tiempo_vs_tamanio(
    tamanios: list[int],
    tiempo_fuerza_bruta: list[float],
    tiempo_subarreglo: list[float],
) -> None:
    """Genera la gráfica de tiempo de ejecución contra tamaño de entrada.

    Args:
        tamanios: Tamaños de las entradas medidas.
        tiempo_fuerza_bruta: Tiempos de ejecución de fuerza bruta.
        tiempo_subarreglo: Tiempos de ejecución de divide y vencerás.
    """
    plt.figure()
    plt.plot(tamanios, tiempo_fuerza_bruta, label="Tiempo fuerza bruta")
    plt.plot(tamanios, tiempo_subarreglo, label="Tiempo subarreglo")
    plt.title("Tiempo vs tamaño de entrada")
    plt.xlabel("Tamaño de entrada (elementos)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("lab2-divide-y-vencer/graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    random.seed(42)
    tamanios = [10, 50, 100, 500, 1000, 4000, 8000]
    tiempo_subarreglo_maximo = []
    tiempo_fuerza_bruta = []

    for tamanio in tamanios:
        serie = generar_entradas(tamanio)

        inicio_fuerza_bruta = perf_counter()
        subarreglo_fuerza_bruta(serie)
        fin_fuerza_bruta = perf_counter()
        tiempo_fuerza_bruta.append(fin_fuerza_bruta - inicio_fuerza_bruta)

        inicio_subarreglo = perf_counter()
        subarreglo_maximo(serie, 0, len(serie) - 1)
        fin_subarreglo = perf_counter()
        tiempo_subarreglo_maximo.append(fin_subarreglo - inicio_subarreglo)

        assert subarreglo_fuerza_bruta(serie)[2] == subarreglo_maximo(
            serie, 0, len(serie) - 1
        )[2]

    graficar_tiempo_vs_tamanio(
        tamanios,
        tiempo_fuerza_bruta,
        tiempo_subarreglo_maximo,
    )
