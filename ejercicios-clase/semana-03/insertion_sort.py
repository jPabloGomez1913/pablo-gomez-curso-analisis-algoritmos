def insertion_sort(arreglo: list, puntos_de_control:set[int]) -> list:
    """
    Ordena una lista de menor a mayor usando el metodo de insercion

    Args:
        arreglo: lista de elementos

    Returns:
        la misma lista ordenada de menor a mayor
    """
    for i in range(1,len(arreglo)):
        if i in puntos_de_control:
            assert arreglo[:i] == sorted(arreglo[:i]), (f"Invariante del ciclo esta porta para {arreglo[:1]}")
        
        clave = arreglo[i] #Elemento que se va a insertar
        j = i - 1

        while arreglo[j] > clave and j >= 0:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = clave
    return arreglo

if __name__ == "__main__":
    arreglo = [5,2,4,6,1,3]
    n = len(arreglo)
    puntos = {2, n // 2, n-1}
    arreglo_ordenado = insertion_sort([5,2,4,6,1,3],puntos)
    print(arreglo_ordenado)

