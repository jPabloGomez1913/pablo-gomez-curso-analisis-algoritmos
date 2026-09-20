"""Parte 4: comparacion temporal de insertion sort y merge sort.

Uso desde la carpeta del laboratorio:
    python parte4_complejidad.py

Requiere matplotlib. Genera graficas/parte4_tiempo.png con el escenario A.
"""

import time
from collections import Counter
from collections.abc import Callable
from pathlib import Path
from statistics import median
from typing import TypedDict

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio
from parte3_casos import REPETICIONES, SEMILLA, TAMANOS

plt.switch_backend("Agg")

CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"
ALGORITMOS: dict[str, Callable[[list[int]], tuple[list[int], int]]] = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}


class SerieResultados(TypedDict):
    """Comparaciones y medianas de tiempo de un algoritmo para cada n."""

    comparaciones: list[int]
    tiempo: list[float]


Resultados = dict[str, SerieResultados]


def verificar(
    datos: list[int], copia: list[int], resultado: list[int]
) -> None:
    """Comprueba la salida y la entrada fuera del intervalo cronometrado.

    Args:
        datos: entrada despues de la llamada al algoritmo.
        copia: contenido original de la entrada.
        resultado: lista devuelta por el algoritmo.

    Raises:
        AssertionError: si se altera la entrada o el resultado es incorrecto.
    """
    assert datos == copia, "el algoritmo modifico la lista recibida"
    assert resultado is not datos, "el algoritmo no devolvio una lista nueva"
    assert Counter(resultado) == Counter(copia), "faltan o sobran elementos"
    assert all(
        resultado[i] >= resultado[i + 1]
        for i in range(len(resultado) - 1)
    ), "el resultado no esta ordenado de mayor a menor"


def ejecutar_experimento() -> Resultados:
    """Compara ambos algoritmos sobre los mismos lotes aleatorios.

    Se alterna el orden de ejecucion entre repeticiones. La generacion,
    la verificacion y el calculo de la mediana quedan fuera del cronometro.

    Returns:
        Comparaciones y medianas de tiempo en segundos para cada algoritmo,
        en el mismo orden que TAMANOS.
    """
    resultados: Resultados = {
        nombre: {"comparaciones": [], "tiempo": []}
        for nombre in ALGORITMOS
    }
    nombres = list(ALGORITMOS)
    for n in TAMANOS:
        datos = generar_aleatorio(n, SEMILLA)
        copia = list(datos)
        tiempos: dict[str, list[float]] = {
            nombre: [] for nombre in nombres
        }
        conteos: dict[str, list[int]] = {nombre: [] for nombre in nombres}

        for repeticion in range(REPETICIONES):
            orden = nombres if repeticion % 2 == 0 else nombres[::-1]
            for nombre in orden:
                algoritmo = ALGORITMOS[nombre]
                inicio = time.perf_counter()
                resultado, comparaciones = algoritmo(datos)
                tiempo = time.perf_counter() - inicio

                verificar(datos, copia, resultado)
                tiempos[nombre].append(tiempo)
                conteos[nombre].append(comparaciones)

        for nombre in nombres:
            assert all(
                valor == conteos[nombre][0] for valor in conteos[nombre]
            ), "cambio el conteo entre repeticiones del mismo lote"
            resultados[nombre]["comparaciones"].append(conteos[nombre][0])
            resultados[nombre]["tiempo"].append(median(tiempos[nombre]))
        print(f"  n = {n:>5} listo")
    return resultados


def imprimir_tablas(resultados: Resultados) -> None:
    """Presenta comparaciones, tiempos y razones entre los algoritmos.

    Args:
        resultados: series producidas por ejecutar_experimento.
    """
    nombres = list(ALGORITMOS)
    print("\nComparaciones")
    print(f"{'n':>6} " + " ".join(f"{nombre:>20}" for nombre in nombres))
    for i, n in enumerate(TAMANOS):
        fila = " ".join(
            f"{resultados[nombre]['comparaciones'][i]:>20,}"
            for nombre in nombres
        )
        print(f"{n:>6} {fila}")

    print(f"\nTiempo (segundos, mediana de {REPETICIONES} ejecuciones)")
    print(f"{'n':>6} " + " ".join(f"{nombre:>20}" for nombre in nombres))
    for i, n in enumerate(TAMANOS):
        fila = " ".join(
            f"{resultados[nombre]['tiempo'][i]:>20.8f}"
            for nombre in nombres
        )
        print(f"{n:>6} {fila}")

    tiempo_insertion, tiempo_merge = (
        resultados[nombre]["tiempo"][-1] for nombre in nombres
    )
    print(
        f"\nRazon de tiempos con n = {TAMANOS[-1]}: "
        f"insertion / merge = {tiempo_insertion / tiempo_merge:.2f}"
    )
    print("Factor de tiempo al duplicar n en el ultimo paso:")
    for nombre in nombres:
        tiempos = resultados[nombre]["tiempo"]
        print(f"  {nombre:<20} x{tiempos[-1] / tiempos[-2]:.2f}")


def graficar(resultados: Resultados) -> None:
    """Guarda la comparacion temporal en graficas/parte4_tiempo.png.

    Args:
        resultados: series producidas por ejecutar_experimento.
    """
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5.5))
    for (nombre, serie), marcador in zip(resultados.items(), ["o", "s"]):
        ax.plot(
            TAMANOS,
            serie["tiempo"],
            marker=marcador,
            linewidth=2,
            label=nombre,
        )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Tamaño de entrada n (registros, escala log)")
    ax.set_ylabel("Tiempo de ejecución (s, mediana, escala log)")
    ax.set_title("Escenario A: insertion sort frente a merge sort")
    ax.set_xticks(TAMANOS)
    ax.set_xticklabels([str(n) for n in TAMANOS])
    ax.minorticks_off()
    ax.grid(True, which="major", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    ruta = CARPETA_GRAFICAS / "parte4_tiempo.png"
    fig.savefig(ruta, dpi=150)
    plt.close(fig)
    print(f"  guardada: {ruta}")


def main() -> None:
    """Ejecuta la comparacion, imprime los resultados y genera la figura."""
    print(
        f"Escenario A | tamanos: {TAMANOS} | semilla: {SEMILLA} | "
        f"repeticiones: {REPETICIONES}"
    )
    resultados = ejecutar_experimento()
    imprimir_tablas(resultados)
    graficar(resultados)


if __name__ == "__main__":
    main()
