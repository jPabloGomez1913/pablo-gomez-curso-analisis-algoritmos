"Antes"
def CalcularPromedio(Lista):
    s=0
    for x in Lista:
     s=s+x
    return s/len(Lista)
 
l=[1,2,3,4,5]
print(CalcularPromedio(l))

"Despues"
def calcular_promedio(lista: list) -> float:
    """Calcula el promedio de una lista de numeros.
 
    Args:
        lista: lista de números para calcular su promedio.
 
    Returns:
        Promedio de la lista.
    """
    suma = 0
    for valor in lista:
        suma = suma + valor
    return suma / len(lista)
 

def main() -> None:
    lista = [1,2,3,4,5]
    print(calcular_promedio(lista))
 
 
if __name__ == "__main__":
    main()