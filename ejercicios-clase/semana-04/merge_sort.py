def merge_sort(arreglo: list[int]) -> list[int]:
    """
    Ordena una lista de menor a mayor mediante merge sort (divir y vencer)

    Args:
        Arreglo: lis de elementos a ordenar

    Returns: 
        Lista de elemnetos ordenados
    """
    #Caso base
    if len(arreglo) <= 1:
        return arreglo

    #Caso recursivo
    mitad = len(arreglo) // 2
    izquierda = merge_sort(arreglo[:mitad])
    derecha = merge_sort(arreglo[mitad:])

    return merge(izquierda, derecha)

def merge(izquierda: list[int], derecha: list[int]) ->list[int]:
    """
    Combina dos listas ya ordenadas en una lista ordenada

    Args:
        izquierda : lista ordenada de menor a mayor del subarreglo a las izquierda
        derecha : lista ordenada de menor a mayor del subarreglo a las derecha

    Returns:
    Una lista ordenada con todos los elementos
    """
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

if __name__ == "__main__":
    arreglo = [5,2,4,10,6,1,3]
    arreglo_ordenado = merge_sort(arreglo)
    print(arreglo_ordenado)