"""Experimentos de medicion: lista enlazada frente a tabla hash."""

import os
import random
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from pathlib import Path

from estructuras import ListaEnlazada, TablaHash  # noqa: E402

SEMILLA_GUIAS = 2026
BUSQUEDAS = 200
REPETICIONES = 5
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo, por division de prueba.

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor (el menor si hay empate).

    Args:
        objetivo: valor alrededor del cual se busca.

    Returns:
        El primo mas cercano a `objetivo`.
    """
    distancia = 0
    while True:
        if es_primo(objetivo - distancia):
            return objetivo - distancia
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        distancia += 1


def generar_guias(n: int, semilla: int = SEMILLA_GUIAS) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador.

    Returns:
        Lista de n enteros distintos de diez digitos.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def construir(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una lista y una tabla con las mismas guias.

    Args:
        guias: guias a insertar en ambas estructuras.
        m: numero de casillas de la tabla.

    Returns:
        La lista y la tabla ya pobladas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = f"estado {guia}"
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar_igualdad(
    lista: ListaEnlazada, tabla: TablaHash, guias: list[int]
) -> None:
    """Comprueba que lista y tabla devuelven el mismo estado.

    Args:
        lista: lista enlazada poblada.
        tabla: tabla hash poblada con las mismas guias.
        guias: guias existentes de las que se toma una muestra.

    Raises:
        AssertionError: si las estructuras difieren en alguna guia.
    """
    azar = random.Random(SEMILLA_GUIAS)
    muestra = azar.sample(guias, min(100, len(guias)))
    for guia in muestra:
        esperado = f"estado {guia}"
        assert lista.buscar(guia) == esperado
        assert tabla.buscar(guia) == esperado


def medir_busquedas(estructura: ListaEnlazada | TablaHash,
                    guias: list[int]) -> float:
    """Mide el tiempo medio por busqueda, cronometrando solo la busqueda.

    Se repite la tanda de busquedas y se devuelve la mediana de los
    tiempos medios, para reducir el ruido del sistema.

    Args:
        estructura: lista o tabla donde se busca.
        guias: guias a buscar en cada tanda.

    Returns:
        Tiempo medio por busqueda, en microsegundos.
    """
    medias: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in guias:
            estructura.buscar(guia)
        fin = time.perf_counter()
        medias.append((fin - inicio) / len(guias))
    medias.sort()
    return medias[len(medias) // 2] * 1e6


def experimento_a(valores_n: list[int]) -> list[tuple[int, int, float, float]]:
    """Compara lista y tabla (alfa cercano a 2) para varios n.

    Args:
        valores_n: valores del numero de guias a medir.

    Returns:
        Filas (n, m, microsegundos de la lista, microsegundos de la tabla).
    """
    filas: list[tuple[int, int, float, float]] = []
    for n in valores_n:
        guias = generar_guias(n)
        m = primo_cercano(n // 2)
        lista, tabla = construir(guias, m)
        verificar_igualdad(lista, tabla, guias)
        ausentes = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        t_lista = medir_busquedas(lista, ausentes)
        t_tabla = medir_busquedas(tabla, ausentes)
        filas.append((n, m, t_lista, t_tabla))
        print(f"A  n={n:>6}  m={m:>6}  alfa={n / m:5.2f}  "
              f"lista={t_lista:10.3f} us  tabla={t_tabla:8.3f} us")
    return filas


def experimento_b(
    n: int, alfas: list[float]
) -> list[tuple[float, int, float]]:
    """Mide la busqueda en tablas de distinto factor de carga, con n fijo.

    Args:
        n: numero fijo de guias.
        alfas: factores de carga objetivo.

    Returns:
        Filas (alfa real, m, microsegundos por busqueda en la tabla).
    """
    guias = generar_guias(n)
    ausentes = generar_guias_inexistentes(set(guias), BUSQUEDAS)
    filas: list[tuple[float, int, float]] = []
    for alfa in alfas:
        m = primo_cercano(round(n / alfa))
        lista, tabla = construir(guias, m)
        verificar_igualdad(lista, tabla, guias)
        t_tabla = medir_busquedas(tabla, ausentes)
        filas.append((tabla.factor_carga(), m, t_tabla))
        print(f"B  n={n}  m={m:>6}  alfa={tabla.factor_carga():6.3f}  "
              f"tabla={t_tabla:8.3f} us")
    return filas


def graficar_a(filas: list[tuple[int, int, float, float]]) -> None:
    """Grafica el experimento A (ambas curvas en los mismos ejes).

    Args:
        filas: resultados de `experimento_a`.
    """
    ns = [fila[0] for fila in filas]
    plt.figure(figsize=(7, 4.5))
    plt.plot(ns, [f[2] for f in filas], "o-", label="Lista enlazada")
    plt.plot(ns, [f[3] for f in filas], "s-", label="Tabla hash (alfa ~ 2)")
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Busqueda de guias inexistentes: lista vs tabla hash")
    plt.xlabel("Numero de guias n (adimensional, escala log)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos, escala log)")
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "lista_vs_tabla.png"), dpi=150)
    plt.close()


def graficar_b(filas: list[tuple[float, int, float]], n: int) -> None:
    """Grafica el experimento B (tiempo frente al factor de carga).

    Args:
        filas: resultados de `experimento_b`.
        n: numero fijo de guias, para el titulo.
    """
    plt.figure(figsize=(7, 4.5))
    plt.plot([f[0] for f in filas], [f[2] for f in filas], "o-",
             label=f"Tabla hash, n = {n}")
    plt.title("Efecto del factor de carga en la busqueda (n fijo)")
    plt.xlabel("Factor de carga alfa = n / m (adimensional)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "tiempo_vs_alfa.png"), dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y genera las graficas."""
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
    filas_a = experimento_a([100, 500, 1000, 5000, 20000, 50000])
    graficar_a(filas_a)
    n_fijo = 20000
    filas_b = experimento_b(n_fijo, [0.25, 0.5, 1, 2, 4, 10])
    graficar_b(filas_b, n_fijo)


if __name__ == "__main__":
    main()