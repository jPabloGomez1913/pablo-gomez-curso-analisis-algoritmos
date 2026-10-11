"""Subarreglo maximo: fuerza bruta y divide y venceras."""
 
 
def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).
 
    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.
 
    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    # TODO: implemente la solucion en Θ(n²): acumule la suma dentro del
    # ciclo en vez de recalcularla desde cero para cada par.
    n = len(valores)
    mejor_inicio, mejor_fin = 0,0
    suma_maxima = float("-inf")

    for i in range(n):
        suma = 0
        for j in range(i,n):
            suma += valores[j]
            if suma > suma_maxima:
                suma_maxima = suma
                mejor_inicio, mejor_fin = i, j
    return mejor_inicio, mejor_fin, suma_maxima
 
 
def suma_cruzada(valores: list[float], inicio: int, medio: int, fin: int) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
     # TODO: barrido lineal desde el punto medio hacia cada lado.
    suma = 0
    suma_maxima_izquierda = float("-inf")
    mejor_izquierda = medio
    for i in range(medio, inicio - 1, -1):
        suma += valores[i]
        if suma > suma_maxima_izquierda:
            suma_maxima_izquierda = suma
            mejor_izquierda = i

    suma = 0
    suma_maxima_derecha = float("-inf")
    mejor_derecha = medio
    for j in range(medio + 1, fin + 1 , 1):
        suma += valores[j]
        if suma >= suma_maxima_derecha:
            suma_maxima_derecha = suma
            mejor_derecha = j

    return mejor_izquierda,mejor_derecha,suma_maxima_izquierda + suma_maxima_derecha

   
 
 
def subarreglo_maximo(valores: list[float], inicio: int, fin: int) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    # TODO: caso base, dos llamadas recursivas, caso cruzado y combinar.

    if inicio == fin:
            return inicio, fin, valores[inicio]
        
    medio = (inicio + fin) // 2
    
    inicio_izq, fin_izq, suma_izq = subarreglo_maximo(valores, inicio, medio)
    inicio_derecha, fin_derecha, suma_derecha = subarreglo_maximo(valores, medio + 1, fin)
    inicio_cruzada, fin_cruzado, suma_cruzado = suma_cruzada(valores, inicio, medio, fin)
    
    if suma_izq >= suma_derecha and suma_izq >= suma_cruzado:
        return inicio_izq,fin_izq,suma_izq
    if suma_derecha >= suma_izq and suma_derecha >= suma_cruzado:
        return inicio_derecha, fin_derecha,suma_derecha
            
    return inicio_cruzada, fin_cruzado, suma_cruzado