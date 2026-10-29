Matriz =list[list[float]]

import random

def multiplicar_metodo_clasico(a: Matriz, b:Matriz):
    """
    Multiplica dos matrices  cuadradas con la formaula Cij

    Args: 
        a: nxn
        b: nxn
    """
    n = len(a)
    c = [[0,0] * n for _ in range(n)]
    multiplicaciones = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
                multiplicaciones += 1

    return c, multiplicaciones

def sumar(a: Matriz, b: Matriz):
    n = len(a)
    c = [[0,0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]

    return c

def restar(a: Matriz, b: Matriz):
    n = len(a)
    c = [[0,0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]

    return c

def generar_matriz(n: int):
    """
    Genera una matriz nxn de valores aleatorios

    Args:
        n: tamannio de la matriz a generar
    """

    matriz_generada = [[random.randint(-5,5) for _ in range(n)] for _ in range(n)]
    return matriz_generada

def deducir_complejidad(tamanios: list[int]):
    """
    Corre la funcion multiplicar_metodo_clasico sobre tamanios crecientes y muestra
    la cantidad de operaciones realizadas

    Args:
    tamanios: tamanios de matriz a probar
    """
    for i in tamanios:
        _,multiplicaciones = multiplicar_metodo_clasico(generar_matriz(i), generar_matriz(i))
        print(i, multiplicaciones)


if __name__ == "__main__":
    a = [[1,2],[3,4]]    
    b= [[1,3],[3,4]]   
    # multiplicar_metodo_clasico(a,b)
    deducir_complejidad([2, 4, 8, 16, 32, 64])
    sumar(a,b)