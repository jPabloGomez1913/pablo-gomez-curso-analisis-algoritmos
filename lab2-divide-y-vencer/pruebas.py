"""Pruebas de las soluciones para el problema del subarreglo máximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def generar_entradas(n: int) -> list[int]:
    """Genera una lista aleatoria de n enteros entre -100 y 100.

    Args:
        n: Cantidad de elementos que tendrá la lista.

    Returns:
        Lista de enteros generada aleatoriamente.
    """
    entrada = [random.randint(-100, 100) for _ in range(n)]
    random.shuffle(entrada)
    return entrada


if __name__ == "__main__":
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17, (
        "La validación de subarreglo_fuerza_bruta falló "
        f"con la serie: {serie}"
    )
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17, (
        "La validación de subarreglo_maximo falló "
        f"con la serie: {serie}"
    )

    serie = [-3]
    assert subarreglo_fuerza_bruta(serie)[2] == -3, (
        "La validación de subarreglo_fuerza_bruta falló "
        f"con la serie: {serie}"
    )
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -3, (
        "La validación de subarreglo_maximo falló "
        f"con la serie: {serie}"
    )

    serie = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == -1, (
        "La validación de subarreglo_fuerza_bruta falló "
        f"con la serie: {serie}"
    )
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -1, (
        "La validación de subarreglo_maximo falló "
        f"con la serie: {serie}"
    )

    serie = [2, 1, 3, 4, 1, 2, 1, 5, 4]
    assert subarreglo_fuerza_bruta(serie)[2] == 23, (
        "La validación de subarreglo_fuerza_bruta falló "
        f"con la serie: {serie}"
    )
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 23, (
        "La validación de subarreglo_maximo falló "
        f"con la serie: {serie}"
    )

    serie = [-2, 4, 3, -1, 5, -2]
    assert subarreglo_fuerza_bruta(serie)[2] == 11, (
        "La validación de subarreglo_fuerza_bruta falló "
        f"con la serie: {serie}"
    )
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 11, (
        "La validación de subarreglo_maximo falló "
        f"con la serie: {serie}"
    )

    for _ in range(20):
        serie = generar_entradas(random.randint(1, 100))
        assert subarreglo_fuerza_bruta(serie)[2] == subarreglo_maximo(
            serie, 0, len(serie) - 1
        )[2], (
            "La comparación entre subarreglo_maximo y "
            f"subarreglo_fuerza_bruta falló con la serie: {serie}"
        )
