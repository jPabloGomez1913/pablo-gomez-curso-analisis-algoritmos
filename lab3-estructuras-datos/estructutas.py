"""Lista enlazada y tabla hash para consultar guias de envio."""
 
 
class Nodo:
    """Nodo de una lista enlazada que guarda una guia y su estado."""
 
    def __init__(self, guia: int, estado: str) -> None:
        """Crea un nodo sin siguiente.
 
        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        self.guia = guia
        self.estado = estado
        self.siguiente: Nodo | None = None
 
 
class ListaEnlazada:
    """Lista simplemente enlazada de guias, con insercion al inicio."""
 
    def __init__(self) -> None:
        """Crea una lista vacia."""
        self.cabeza: Nodo | None = None
        self.tamano = 0
 
    def insertar(self, guia: int, estado: str) -> None:
        """Agrega una guia al inicio de la lista.
 
        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        # TODO: cree el nodo, enlacelo con la cabeza actual y actualice
        # la cabeza y el tamano. Debe costar Θ(1).

        nuevo = Nodo(guia, estado)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1

 
    def buscar(self, guia: int) -> str | None:
        """Busca una guia recorriendo la lista.
 
        Args:
            guia: numero de guia a buscar.
 
        Returns:
            El estado del envio, o None si la guia no existe.
        """
        # TODO: recorra desde la cabeza con un ciclo while (iterativo).
        actual = self.cabeza
        while actual is not None and actual.guia != guia:
            actual = actual.siguiente
        if actual is None:
            return None
        return actual.estado
 
 
class TablaHash:
    """Tabla hash con encadenamiento y funcion hash por division."""
 
    def __init__(self, m: int) -> None:
        """Crea una tabla con m casillas vacias.
 
        Args:
            m: numero de casillas de la tabla.
        """
        self.m = m
        self.casillas: list[ListaEnlazada] = [ListaEnlazada() for _ in range(m)]
        self.tamano = 0
 
    def hash(self, guia: int) -> int:
        """Calcula la casilla de una guia con el metodo de la division.
 
        Args:
            guia: numero de guia.
 
        Returns:
            Un indice entre 0 y m - 1.
        """
        # TODO: h(k) = k mod m.
        indice = guia % self.m
        return indice
 
    def insertar(self, guia: int, estado: str) -> None:
        """Inserta una guia en la lista de su casilla.
 
        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        # TODO: calcule la casilla y delegue en la lista de esa casilla.
        indice = self.hash(guia)
        self.casillas[indice].insertar(guia,estado)
        self.tamano += 1
        
 
    def buscar(self, guia: int) -> str | None:
        """Busca una guia recorriendo solo la lista de su casilla.
 
        Args:
            guia: numero de guia a buscar.
 
        Returns:
            El estado del envio, o None si la guia no existe.
        """
        # TODO: calcule la casilla y busque solo en su lista.

        indice = self.hash(guia)
        return self.casillas[indice].buscar(guia)

    
 
    def factor_carga(self) -> float:
        """Calcula el factor de carga de la tabla.
 
        Returns:
            El cociente entre guias almacenadas y casillas (n / m).
        """
        # TODO: devuelva n / m.
        return self.tamano / self.m