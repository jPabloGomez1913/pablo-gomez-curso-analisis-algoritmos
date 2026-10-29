import math
import matplotlib.pyplot as plt

def trabajo_aproximado_del_algoritmo_a(n: int) -> float:
    """
    Estima el trabajo del algoritmo A para un tamano n de datos

    Args:
        n: tamano de la entrada

    Returns:
        Trabajo aproximado del algoritmo(el numero de opetaciones que realiza el algoritmo)
    """
    return n ** 2


def trabajo_aproximado_del_algoritmo_b(n: int) -> float:
    """
    Estima el trabajo del algoritmo B para un tamano n de datos

    Args:
        n: tamano de la entrada

    Returns:
        Trabajo aproximado del algoritmo(el numero de opetaciones que realiza el algoritmo)
    """
    return n * math.log2(n)

def graficar_y_comparar_algoritmos(tamanios: list[int], ruta_salida: str) -> None:
    """
    Grafica el trabajo aproximado de A y B  para una lista de tamanios

    Args:
        tamanios: tamanios de entradas a evalauar en orden creciente
        ruta_salida: lugar donde se guarda la figura generada
    """
    trabajo_a = [trabajo_aproximado_del_algoritmo_a(n) for n in tamanios]
    trabajo_b = [trabajo_aproximado_del_algoritmo_b(n) for n in tamanios]
    trabajo_a_hardware_rapido = [valor / 2 for valor in trabajo_a]
    trabajo_a_hardware_rapido_3x = [valor / 3 for valor in trabajo_a]

    plt.figure(figsize=(8,5))
    plt.plot(tamanios,trabajo_a, label="Algoritmo A (n**2)")
    plt.plot(tamanios,trabajo_b, label="Algoritmo B (n log n)")
    plt.plot(tamanios,trabajo_a_hardware_rapido, label="Algoritmo A en hardware 2x mas rapido")
    plt.plot(tamanios,trabajo_a_hardware_rapido_3x, label="Algoritmo A en hardware 3x mas rapido")
    plt.xlabel("Tamano de la entrada (n)")
    plt.title("Trabajo aproximado")
    plt.ylabel("Algoritmo A vs Algoritmo B")
    plt.legend()
    plt.grid(True)
    plt.savefig(ruta_salida)


    

if __name__ == "__main__":
    tamanios = [10 ,100, 500, 1000, 5000, 10000]
    graficar_y_comparar_algoritmos(tamanios,"graficas/clase-1/grafica_algotimo_a_vs_b.png")