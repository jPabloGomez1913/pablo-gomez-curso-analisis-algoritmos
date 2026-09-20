"""Experimento de la Parte 3: escenarios de insertion sort en Tamiza.

Uso desde la carpeta del laboratorio:
    python parte3_casos.py

Requiere matplotlib. Guarda las dos figuras en graficas/, junto al script.
"""

import time
from collections.abc import Callable
from pathlib import Path
from statistics import median
from typing import Literal, TypedDict

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

plt.switch_backend("Agg")  # Guarda las figuras sin abrir ventanas.

SEMILLA = 42
TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"

ESCENARIOS: dict[str, Callable[[int], list[int]]] = {
    "A — aleatorio": lambda n: generar_aleatorio(n, SEMILLA),
    "B — casi ordenado": lambda n: generar_casi_ordenado(n, SEMILLA),
    "C — orden inverso": generar_inverso,
}


class SerieResultados(TypedDict):
    """Comparaciones y medianas de tiempo para los tamanos del experimento."""

    comparaciones: list[int]
    tiempo: list[float]


Resultados = dict[str, SerieResultados]


def verificar(
    datos: list[int], copia: list[int], resultado: list[int]
) -> None:
    """Comprueba el resultado sin incluir la verificacion en el cronometro.

    Args:
        datos: entrada despues de ejecutar el algoritmo.
        copia: contenido original de la entrada.
        resultado: lista devuelta por el algoritmo.

    Raises:
        AssertionError: si cambia la entrada o el resultado es incorrecto.
    """
    n = len(copia)
    assert len(datos) == n and len(set(datos)) == n, (
        "el lote no tiene n indices distintos"
    )
    assert datos == copia, "insertion_sort modifico la lista recibida"
    assert resultado is not datos, "el algoritmo no devolvio una lista nueva"
    assert len(resultado) == n and set(resultado) == set(copia), (
        "faltan o sobran elementos"
    )
    assert all(resultado[i] >= resultado[i + 1] for i in range(n - 1)), (
        "el resultado no esta ordenado de mayor a menor"
    )


def ejecutar_experimento() -> Resultados:
    """Mide las comparaciones y el tiempo de los tres escenarios.

    Cada lote se genera antes de medir y se reutiliza en las repeticiones.
    El cronometro incluye solamente la llamada a insertion_sort.

    Returns:
        Series de comparaciones y medianas de tiempo en segundos,
        en el mismo orden que TAMANOS, agrupadas por escenario.
    """
    resultados: Resultados = {
        nombre: {"comparaciones": [], "tiempo": []}
        for nombre in ESCENARIOS
    }
    for n in TAMANOS:
        for nombre, generador in ESCENARIOS.items():
            datos = generador(n)
            copia = list(datos)
            tiempos: list[float] = []
            conteos: list[int] = []

            for _ in range(REPETICIONES):
                inicio = time.perf_counter()
                resultado, comparaciones = insertion_sort(datos)
                tiempo = time.perf_counter() - inicio

                verificar(datos, copia, resultado)
                tiempos.append(tiempo)
                conteos.append(comparaciones)

            assert all(conteo == conteos[0] for conteo in conteos), (
                "cambio el conteo entre repeticiones del mismo lote"
            )
            resultados[nombre]["comparaciones"].append(conteos[0])
            resultados[nombre]["tiempo"].append(median(tiempos))
        print(f"  n = {n:>5} listo")
    return resultados


def imprimir_tablas(resultados: Resultados) -> None:
    """Presenta las mediciones y las razones entre escenarios.

    Args:
        resultados: series producidas por ejecutar_experimento.
    """
    nombres = list(ESCENARIOS)
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

    a, b, c = (
        resultados[nombre]["comparaciones"][-1] for nombre in nombres
    )
    print(
        f"\nRazones con n = {TAMANOS[-1]}: "
        f"C/A = {c / a:.2f}, A/B = {a / b:.1f}, C/B = {c / b:.1f}"
    )
    print("Factor de comparaciones al duplicar n en el ultimo paso:")
    for nombre in nombres:
        valores = resultados[nombre]["comparaciones"]
        print(f"  {nombre:<20} x{valores[-1] / valores[-2]:.2f}")


def graficar(
    resultados: Resultados,
    magnitud: Literal["comparaciones", "tiempo"],
    etiqueta_y: str,
    titulo: str,
    archivo: str,
) -> None:
    """Guarda una grafica con los tres escenarios en los mismos ejes.

    Args:
        resultados: series producidas por ejecutar_experimento.
        magnitud: clave a dibujar, comparaciones o tiempo.
        etiqueta_y: nombre de la magnitud y su unidad.
        titulo: titulo de la figura.
        archivo: nombre del PNG dentro de CARPETA_GRAFICAS.
    """
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5.5))
    for (nombre, serie), marcador in zip(
        resultados.items(), ["o", "s", "^"]
    ):
        ax.plot(
            TAMANOS,
            serie[magnitud],
            marker=marcador,
            linewidth=2,
            label=nombre,
        )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Tamaño de entrada n (registros, escala log)")
    ax.set_ylabel(etiqueta_y)
    ax.set_title(titulo)
    ax.set_xticks(TAMANOS)
    ax.set_xticklabels([str(n) for n in TAMANOS])
    ax.minorticks_off()
    ax.grid(True, which="major", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    ruta = CARPETA_GRAFICAS / archivo
    fig.savefig(ruta, dpi=150)
    plt.close(fig)
    print(f"  guardada: {ruta}")


def main() -> None:
    """Ejecuta las mediciones, imprime las tablas y guarda ambas figuras."""
    print(
        f"Tamanos: {TAMANOS} | semilla: {SEMILLA} | "
        f"repeticiones: {REPETICIONES}"
    )
    resultados = ejecutar_experimento()
    imprimir_tablas(resultados)
    graficar(
        resultados,
        "comparaciones",
        "Comparaciones entre elementos (conteo, escala log)",
        "Insertion sort: comparaciones vs. tamaño de entrada",
        "parte3_comparaciones.png",
    )
    graficar(
        resultados,
        "tiempo",
        "Tiempo de ejecución (s, mediana, escala log)",
        "Insertion sort: tiempo vs. tamaño de entrada",
        "parte3_tiempo.png",
    )


if __name__ == "__main__":
    main()
