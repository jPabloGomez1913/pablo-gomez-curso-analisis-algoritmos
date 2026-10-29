class Cola:
    """Cola circular de enteros sobre un arreglo de capacidad fija"""

    def __init__(self, capacidad: int)-> None:
        """
        Crear una cola vacia

        Args:
            capacidad: numero maximo de elementos 
        """
        self.datos: list = [0] * capacidad
        self.inicio: int = 0
        self.tamanio: int = 0

    def esta_vacia(self)-> bool:
        """
        Indica si no hay elementos en la cola

        Returns:
            True si la cola esta vacia
        """
        return self.inicio == 0

    def obtener_tamanio(self) -> int:
        """
        Indica la cantidad de elementos encolados

        Returns:
            Un entero que representa la cantidad de elementos
        """
        return self.tamanio

    def enqueue(self,dato:int) -> None:
        """
        Encola un valor al final

        Args
            dato: valor a encolar

        Raises: 
            OverflowError: Si la cola ya esta en su capacidad maxima
        """
        if self.tamanio == len(self.datos):
            raise OverflowError("Colla llena")
        posicion = self.tamanio
        self.datos[posicion] = dato
        

    def dequeue(self) -> int:
        """
        Desencola el valor ubicado en el frente

        Return:
            El dato que llevaba mas tiempo en la cola
        """
        if self.esta_vacia():
            raise IndexError("La cola esta vacia")


        dato_extraido: int = self.datos[self.inicio] 
        self.inico = self.inico + 1
        self.tamanio -= 1
        return dato_extraido

    def front(self) -> int:
        """
        Permite ver el primer elemento en la cola (el inicio)

        Returns:
            el primer dato encolado
        """

        return self.datos[self.inicio]



if __name__ == "__main__":

    cola_enteros = Cola(5)
    cola_enteros.enqueue(9)
    cola_enteros.enqueue(5)
    cola_enteros.enqueue(7)
    cola_enteros.enqueue(11)
    cola_enteros.enqueue(6)

    cola_enteros.dequeue() #procesar el primer elemento
    cola_enteros.enqueue(76)
