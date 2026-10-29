"""Medición repetida de las soluciones de subarreglo máximo."""

import random
from pathlib import Path
from statistics import mean
from time import perf_counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANIOS = [10, 50, 100, 500, 1000, 4000, 8000]
REPETICIONES = 7
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def generar_entradas(n: int) -> list[int]:
    """Genera una lista aleatoria de n enteros entre -100 y 100."""
    entrada = [random.randint(-100, 100) for _ in range(n)]
    random.shuffle(entrada)
    return entrada


def graficar_tiempo_vs_tamanio(
    tamanios: list[int],
    muestras_fuerza_bruta: list[list[float]],
    muestras_subarreglo: list[list[float]],
) -> None:
    """Grafica los promedios y rangos observados para cada tamaño."""
    promedios_fuerza_bruta = [mean(muestras) for muestras in muestras_fuerza_bruta]
    promedios_subarreglo = [mean(muestras) for muestras in muestras_subarreglo]

    def rangos_error(muestras: list[list[float]], promedios: list[float]):
        inferiores = [promedio - min(serie) for promedio, serie in zip(promedios, muestras)]
        superiores = [max(serie) - promedio for promedio, serie in zip(promedios, muestras)]
        return [inferiores, superiores]

    plt.figure(figsize=(8, 5))
    plt.errorbar(
        tamanios,
        promedios_fuerza_bruta,
        yerr=rangos_error(muestras_fuerza_bruta, promedios_fuerza_bruta),
        marker="o",
        capsize=4,
        label="Fuerza bruta (promedio)",
    )
    plt.errorbar(
        tamanios,
        promedios_subarreglo,
        yerr=rangos_error(muestras_subarreglo, promedios_subarreglo),
        marker="o",
        capsize=4,
        label="Divide y vencerás (promedio)",
    )
    plt.title(f"Tiempo vs tamaño de entrada ({REPETICIONES} repeticiones)")
    plt.xlabel("Tamaño de entrada (elementos)")
    plt.ylabel("Tiempo de ejecución (segundos, escala logarítmica)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", alpha=0.35)
    plt.tight_layout()
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_n.png", dpi=160)
    plt.close()


def imprimir_resultados(
    tamanios: list[int],
    muestras_fuerza_bruta: list[list[float]],
    muestras_subarreglo: list[list[float]],
) -> None:
    """Imprime las medias que se usan como puntos de la gráfica."""
    print(f"Promedios aritméticos de {REPETICIONES} repeticiones (segundos)")
    print(f"{'n':>7} {'Fuerza bruta':>18} {'Divide y vencerás':>20}")
    for n, fuerza, divide in zip(
        tamanios, muestras_fuerza_bruta, muestras_subarreglo
    ):
        print(f"{n:7d} {mean(fuerza):18.9f} {mean(divide):20.9f}")

    indice_4000 = tamanios.index(4000)
    indice_8000 = tamanios.index(8000)
    promedio_fb_4000 = mean(muestras_fuerza_bruta[indice_4000])
    promedio_fb_8000 = mean(muestras_fuerza_bruta[indice_8000])
    promedio_dv_4000 = mean(muestras_subarreglo[indice_4000])
    promedio_dv_8000 = mean(muestras_subarreglo[indice_8000])
    print(
        "Factores al duplicar n de 4000 a 8000: "
        f"fuerza bruta {promedio_fb_8000 / promedio_fb_4000:.3f}; "
        f"divide y vencerás {promedio_dv_8000 / promedio_dv_4000:.3f}"
    )


if __name__ == "__main__":
    random.seed(42)
    muestras_fuerza_bruta = [[] for _ in TAMANIOS]
    muestras_subarreglo = [[] for _ in TAMANIOS]

    for repeticion in range(REPETICIONES):
        # Intercala tamaños para que una tendencia en la carga del equipo no
        # afecte siempre las mediciones de los tamaños grandes.
        for indice in random.sample(range(len(TAMANIOS)), len(TAMANIOS)):
            tamanio = TAMANIOS[indice]
            serie = generar_entradas(tamanio)

            # Alterna el orden para reducir el efecto de ejecutar siempre un
            # algoritmo antes que el otro.
            if repeticion % 2 == 0:
                inicio = perf_counter()
                resultado_fuerza_bruta = subarreglo_fuerza_bruta(serie)
                muestras_fuerza_bruta[indice].append(perf_counter() - inicio)

                inicio = perf_counter()
                resultado_subarreglo = subarreglo_maximo(
                    serie, 0, len(serie) - 1
                )
                muestras_subarreglo[indice].append(perf_counter() - inicio)
            else:
                inicio = perf_counter()
                resultado_subarreglo = subarreglo_maximo(
                    serie, 0, len(serie) - 1
                )
                muestras_subarreglo[indice].append(perf_counter() - inicio)

                inicio = perf_counter()
                resultado_fuerza_bruta = subarreglo_fuerza_bruta(serie)
                muestras_fuerza_bruta[indice].append(perf_counter() - inicio)

            assert resultado_fuerza_bruta[2] == resultado_subarreglo[2]

    imprimir_resultados(TAMANIOS, muestras_fuerza_bruta, muestras_subarreglo)
    graficar_tiempo_vs_tamanio(
        TAMANIOS, muestras_fuerza_bruta, muestras_subarreglo
    )
