class Pila:
    """Pila de datos sobre un arreglo de capacidas fija"""

    def __init__(self, capacidad: int)-> None:
        """
        Crear una pila vacia

        Args:
            capacidad: numero de elementos 
        """
        self.datos: list = [0] * capacidad
        self.tope: int = 0
        self.tamanio: int = 0

    def esta_vacia(self)-> bool:
        """
        Indica si no hay elementos en la pila

        Returns:
            True si la pila esta vacia
        """
        return self.tope == 0

    def obtener_tamanio(self) -> int:
        """
        Indica la cantidad de elementos apilados

        Returns:
            Un entero que representa la cantidad de elementos
        """
        return self.tamanio

    def push(self,dato:int) -> None:
        """
        Apila un valor

        Args
            dato: valor a apilar

        Raises: 
            OverflowError: Si la pila ya esta en su capacidad maxima
        """
        if self.tope == len(self.datos):
            raise OverflowError("Pila error")
        
        self.datos[self.tope] = dato
        self.tope += 1
        self.tamanio +=1

    def pop(self) -> int:
        """
        Desapila el valor ubicado en el top

        Return:
            El ultimo valor apilado
        """
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")


        dato_extraido: int = self.datos[self.tope - 1] 
        self.tope -= 1
        self.tamanio -=1


        return dato_extraido

    def peak(self) -> int:
        """
        Permite ver el ultimo valor apilado (el tope)

        Returns:
            el ultimo dato apilado
        """

        return self.datos[self.tope -1]



if __name__ == "__main__":
     

    pila_enteros = Pila(5)

    pila_enteros.push(1)
    pila_enteros.push(2)
    print(pila_enteros.pop())
    pila_enteros.push(3)
    print(pila_enteros.pop())
    print(pila_enteros.pop())
    print(pila_enteros.tope)


   
