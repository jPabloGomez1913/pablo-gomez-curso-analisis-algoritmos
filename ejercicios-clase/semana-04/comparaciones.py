import random
import matplotlib.pyplot as plt



def insertion_sort(arreglo: list) -> tuple[list,int,int]:
    """
    Ordena una lista de menor a mayor usando el metodo de insercion

    Args:
        arreglo: lista de elementos

    Returns:
        Tupla(arreglo, comparaciones, desplazamientos)
    """
    comparaciones = 0
    desplazamientos = 0
    n = len(arreglo)
    for i in range(1,len(arreglo)):
        # if i in puntos_de_control:
        #     assert arreglo[:i] == sorted(arreglo[:i]), (f"Invariante del ciclo esta porta para {arreglo[:1]}")
        
        clave = arreglo[i] #Elemento que se va a insertar
        j = i - 1

        while j >= 0:
            comparaciones += 1
            if arreglo[j] <= clave:
                break
            arreglo[j + 1] = arreglo[j]
            desplazamientos += 1
            j -= 1
        arreglo[j + 1] = clave
    return arreglo,comparaciones,desplazamientos

def generar_entradas(n: int) -> dict[str,list[int]]:
    """
    Genera 3 entradas de tamanio n: ordenada, invertida y aleatoria

    Args:
        n: tamanio de cada una de las 3 listas generadas

    Returns:
        Diccionario con las claves ordenada , invertidad y aleatroia
    """
    ordenada = list(range(n))
    invertida = list(range(n, 0, -1))
    aleatoria = ordenada.copy()
    random.shuffle(aleatoria)
    return {"ordenada": ordenada, "invertida": invertida, "aleatoria": aleatoria}

def medir_compararaciones(tamanios: list[int]) ->  dict[str,list[int]]:
    """
    Mide comparaciones de insertion sort para cada tipo de entrada

    Args: 
    tamanios : lista de tamanios de entrada a medir

    Returns :
    Diccionarios con una clave por tipo de entrada y como valor, la lista de comparaciones medidad para cada tamnio n
        
    """
    resultados = {"ordenada":[], "invertida":[], "aleatoria":[]}
    for n in tamanios:
        entradas = generar_entradas(n)
        for tipo, arreglo in entradas.items():
            _, comparaciones, _ = insertion_sort(arreglo)
            resultados[tipo].append(comparaciones)

    return resultados

def graficar_operaciones(tamanios: list[int] , resultados: dict[str, list[int]]) -> None:
    """
    Grafica operaciones vs n para cada tipo de entrada
    """
    plt.figure()
    for tipo,valores in resultados.items():
        plt.plot(tamanios, valores, label=tipo)
    plt.title("Insertion sort comparaciones vs n")
    plt.xlabel("tamano de la entrada(n)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-4/comparaciones.png")


if __name__ == "__main__":
    tamanios = [10,100,1000]
    resultados = medir_compararaciones(tamanios)
    graficar_operaciones(tamanios, resultados)


