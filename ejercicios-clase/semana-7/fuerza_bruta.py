
import matplotlib.pyplot as plt
import random

def subaregglo_maximo_por_fuerza_bruta(arreglo: list) -> tuple[int,int,float,float]:
    """
    Encuentra el subarreglo de mayor suma en un arreglo original calculando
    todas las posibles ecuaciones

    Args:
        arreglo: arreglo a procesar para extrarer el maximo subarreglo

    Return:
        Una tupla(mejor_inicio, mejor_fin, suma_maxima, operaciones)
    """
    n = len(arreglo)
    mejor_inicio, mejor_fin = 0,0
    suma_maxima = float("-inf")
    operaciones = 0

    for i in range(n):
        operaciones += 1
        for j in range(i,n):
            suma = 0
            operaciones += 1
            for k in range(i, j+1):
                operaciones += 1
                suma += arreglo[k]
            if suma > suma_maxima:
                suma_maxima = suma
                mejor_fin = j
                mejor_inicio = i
    return mejor_inicio, mejor_fin, suma_maxima, operaciones


def generar_entradas(n: int) -> list[int]:
    """
    Genera 3 entradas de tamanio n: ordenada, invertida y aleatoria

    Args:
        n: tamanio de cada una de las 3 listas generadas

    Returns:
        Diccionario con las claves ordenada , invertidad y aleatroia
    """
    entrada = [random.randint(-100,100) for _ in range(n)]
    random.shuffle(entrada)
    return entrada

def graficar_operaciones(tamanios: list[int] , resultados: list[int]) -> None:
    """
    Grafica operaciones vs n para cada tipo de entrada
    """
    plt.figure()
   
    plt.plot(tamanios, resultados)
    plt.title("Insertion sort comparaciones vs n")
    plt.xlabel("tamano de la entrada(n)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-4/fuerza_bruta_maximo_sub_arreglo.png")


if __name__ == "__main__":
    # arreglo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # mejor_inicio, mejor_fin, suma_maxima, operaciones = subaregglo_maximo_por_fuerza_bruta(arreglo)
    # print(mejor_inicio, mejor_fin, suma_maxima, operaciones )

    tamanios = [10,50,100,200,400,800]
    cantidad_operaciones = []
    for tamanio in tamanios:
        _, _, _, operaciones = subaregglo_maximo_por_fuerza_bruta(generar_entradas(tamanio))
        cantidad_operaciones.append(operaciones)
        print(tamanio,operaciones)

    graficar_operaciones(tamanios,cantidad_operaciones)
