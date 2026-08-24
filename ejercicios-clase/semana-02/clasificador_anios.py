"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 4 == 0:
        if anio % 100 == 0 and anio % 400 == 0:
            return True
        elif anio % 100 == 0:
            return False
        return True
    else:
        return False


 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    while True:
        try:
            lista_anios = []
            lista_anios_input = input("Ingrese una lista de años separados por ',' : ")
            lista_anios = lista_anios_input.split(",")
            for indice, numero in enumerate(lista_anios):
                anio = int(numero)
                if anio < 0:
                     raise ValueError(f"el año {anio} es negativo")
                lista_anios[indice] = int(numero)

            return lista_anios
        except:
            print(f"El dato {numero} es incorrecto")
        
 
 
def main() -> None:
    """Punto de entrada del script."""
    anios_ingresados = leer_anios()
    anios_bisiestos = [anio for anio in anios_ingresados if es_bisiesto(anio)]

    print(f"Años ingresados: {anios_ingresados}")
    print(f"Años bisiestos: {anios_bisiestos}")
    print(f"Cantidad de años bisiestos: {len(anios_bisiestos)} de {len(anios_ingresados)}")
 
if __name__ == "__main__":
    main()