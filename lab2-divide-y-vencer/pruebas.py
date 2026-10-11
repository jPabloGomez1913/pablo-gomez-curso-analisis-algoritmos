from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo
import random

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
 


if __name__ == "__main__":
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

    serie = [-3,]
    assert subarreglo_fuerza_bruta(serie)[2] == -3
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -3

    serie = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == -1
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -1

    serie = [2, 1, 3, 4, 1, 2, 1, 5, 4]
    assert subarreglo_fuerza_bruta(serie)[2] == 23
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 23

    for i in range(20):
        serie = generar_entradas(random.randint(1,100))
        assert subarreglo_fuerza_bruta(serie)[2] == subarreglo_maximo(serie, 0, len(serie) - 1)[2]

