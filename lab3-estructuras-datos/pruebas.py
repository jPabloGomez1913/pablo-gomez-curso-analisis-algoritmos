"""Pruebas de ListaEnlazada y TablaHash."""
import random

from estructuras import ListaEnlazada, TablaHash


def test_lista_busqueda() -> None:
    lista = ListaEnlazada()
    for guia in (5, 8, 13):
        lista.insertar(guia, f"estado {guia}")
    assert lista.buscar(8) == "estado 8"      # exitosa
    assert lista.buscar(99) is None           # infructuosa
    assert lista.tamano == 3
    assert lista.cabeza is not None and lista.cabeza.guia == 13


def test_tabla_busqueda() -> None:
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")
    assert tabla.buscar(24) == "en bodega"    # exitosa
    assert tabla.buscar(99) is None           # infructuosa


def test_colision_forzada() -> None:
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, f"estado {guia}")
    for guia in (10, 24, 17):
        assert tabla.buscar(guia) == f"estado {guia}"
    assert tabla.casillas[3].tamano == 3
    longitud = 0
    actual = tabla.casillas[3].cabeza
    while actual is not None:
        longitud += 1
        actual = actual.siguiente
    assert longitud == 3
    assert all(
        tabla.casillas[i].tamano == 0 for i in range(7) if i != 3
    )


def test_factor_carga() -> None:
    tabla = TablaHash(7)
    assert tabla.factor_carga() == 0
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")
    assert tabla.factor_carga() == 3 / 7


def test_colecciones_aleatorias() -> None:
    rng = random.Random(2026)
    for _ in range(30):
        m = rng.choice([7, 11, 61, 101])
        n = rng.randint(0, 80)
        guias = rng.sample(range(1_000_000, 9_999_999), n)
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        for guia in guias:
            estado = f"estado {guia}"
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
        for guia in guias:                    # existentes
            assert lista.buscar(guia) == tabla.buscar(guia) == f"estado {guia}"
        conjunto = set(guias)
        ausentes = [g for g in rng.sample(range(1, 999_999), 40)
                    if g not in conjunto]
        for guia in ausentes:                 # inexistentes
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None
        assert tabla.factor_carga() == n / m


if __name__ == "__main__":
    test_lista_busqueda()
    test_tabla_busqueda()
    test_colision_forzada()
    test_factor_carga()
    test_colecciones_aleatorias()
    print("Todas las pruebas pasaron")