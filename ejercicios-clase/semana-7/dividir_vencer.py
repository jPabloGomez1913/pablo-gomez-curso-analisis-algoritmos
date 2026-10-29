
import matplotlib.pyplot as plt
import random

def subarreglo_maximo_por_dividir_vencer(arreglo: list, inicio: int, fin: int) -> tuple[int,int,float]:
    """
    Encuentra el subarreglo de mayor suma en un arreglo original con el paradigma de 
    dividir y vencer

    Args:
        arreglo: arreglo a procesar para extrarer el maximo subarreglo
        inicio: indice inicial del rango a considerar (SE INCLUYE)
        fin: indica final del rango a considerar (SE INCLUYE)

    Return:
        Una tupla(mejor_inicio, mejor_fin, suma_maxima, operaciones)
    """
    if inicio == fin:
        return inicio, fin, arreglo[inicio]
    
    medio = (inicio + fin) // 2

    inicio_izq, fin_izq, suma_izq = subarreglo_maximo_por_dividir_vencer(arreglo, inicio, medio)
    inicio_derecha, fin_derecha, suma_derecha = subarreglo_maximo_por_dividir_vencer(arreglo, medio + 1, fin)
    inicio_cruzada, fin_cruzado, suma_cruzado = suma_cruzada(arreglo, inicio, medio, fin)

    if suma_izq >= suma_derecha and suma_izq >= suma_cruzado:
        return inicio_izq,fin_izq,suma_izq
    if suma_derecha >= suma_izq and suma_derecha >= suma_cruzado:
        return inicio_derecha, fin_derecha,suma_derecha
        
    return inicio_cruzada, fin_cruzado, suma_cruzado

def suma_cruzada(arreglo: int, inicio: int, medio: int, fin: int) -> tuple[int,int,float]:
    """
    Encuentra el subarreglo maximo que cruza el punto medio

    Args:
        arreglo: arreglo a procesar
        inicio: indice inicial del rango considerado
        medio: inidice del pumto medio de la division
        fin: indice final del rango considerado

    Returns:
    Una tupla (indicde_inicial,indice_final,suma_maxima)
    """

    suma = 0
    suma_maxima_izquierda = float("-inf")
    mejor_izquierda = medio
    for i in range(medio, inicio - 1, -1):
        suma += arreglo[i]
        if suma > suma_maxima_izquierda:
            suma_maxima_izquierda = suma
            mejor_izquierda = i

    suma = 0
    suma_maxima_derecha = float("-inf")
    mejor_derecha = medio
    for j in range(medio + 1, fin + 1 , 1):
        suma += arreglo[j]
        if suma >= suma_maxima_derecha:
            suma_maxima_derecha = suma
            mejor_derecha = j

    return mejor_izquierda,mejor_derecha,suma_maxima_izquierda + suma_maxima_derecha



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
     arreglo = [2, 1, 3, 4, 1, 2, 1, 5, 4]
     mejor_inicio, mejor_fin, suma_maxima = subarreglo_maximo_por_dividir_vencer(arreglo,0,len(arreglo)-1)
     print(mejor_inicio, mejor_fin, suma_maxima )

    # tamanios = [10,50,100,200,400,800]
    # cantidad_operaciones = []
    # for tamanio in tamanios:
    #     _, _, _, operaciones = subaregglo_maximo_por_fuerza_bruta(generar_entradas(tamanio))
    #     cantidad_operaciones.append(operaciones)
    #     print(tamanio,operaciones)

    #graficar_operaciones(tamanios,cantidad_operaciones)
