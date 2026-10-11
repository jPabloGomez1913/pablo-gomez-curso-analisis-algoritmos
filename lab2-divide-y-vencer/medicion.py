from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo
import random
import matplotlib.pyplot as plt
from time import perf_counter

def generar_entradas(n: int) -> list[int]:
    """
    Genera entradas de tamanio n

    Args:
        n: tamanio de cada una de las  listas generadas

    Returns:
        Litsa
    """
    entrada = [random.randint(-100,100) for _ in range(n)]
    random.shuffle(entrada)
    return entrada
 
def graficar_tiempo_vs_tamanio(tamanios: list[int] , tiempo_fuerza_bruta: list[int], tiempo_subarreglo) -> None:
    """
    Tiempo vs n para cada tipo de entrada
    """
    plt.figure()

    plt.plot(tamanios,tiempo_fuerza_bruta, label="Tiempo fuerza bruta")
    plt.plot(tamanios,tiempo_subarreglo, label="Tiempo subarreglo")
    plt.title("Tiempo vs tamaño entrada")
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

        inicio_sub_arreglo = perf_counter()
        subarreglo_maximo(serie, 0, len(serie) - 1)
        fin_sub_arreglo = perf_counter()
        tiempo_subarreglo_maximo.append(fin_sub_arreglo - inicio_sub_arreglo)

        assert subarreglo_fuerza_bruta(serie)[2] == subarreglo_maximo(serie, 0, len(serie) - 1)[2]

    graficar_tiempo_vs_tamanio(tamanios, tiempo_fuerza_bruta, tiempo_subarreglo_maximo)

