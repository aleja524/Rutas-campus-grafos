from typing import Any, List, Dict, Tuple
from collections import deque

class GrafoLista:

    def __init__(self):
        self.listaAdy = {}
        self.tamano: int = 0

    def agregarVertice(self, lugar: Any):
        if lugar in self.listaAdy:
            return None  
        self.listaAdy[lugar] = []
        self.tamano += 1
    
    def agregarConexion(self, vertice1, vertice2, dirigido = False, atributos = None):
        if atributos is None:
            atributos = {
                "distancia": 10,
                "tiempo": 2,
                "congestion": 1,
                "accesible": True,
                "estado": "disponible"
            }

        if vertice1 not in self.listaAdy: 
            self.agregarVertice(vertice1)
        if vertice2 not in self.listaAdy:
            self.agregarVertice(vertice2)

        vecinosVertice1 = [] 
        for vertice in self.listaAdy[vertice1]:
            vecinosVertice1.append(vertice[0])

        if vertice2 not in vecinosVertice1: 
            self.listaAdy[vertice1].append((vertice2, atributos))

        if not dirigido: 
            vecinosVertice2 = [] 
            for vertice in self.listaAdy[vertice2]:
                vecinosVertice2.append(vertice[0])

            if vertice1 not in vecinosVertice2: 
                self.listaAdy[vertice2].append((vertice1, atributos))
    
    def recorrerEnAnchura(self, verticeInicial: any) -> List[Any]:
        if verticeInicial not in self.listaAdy:
            return []
        visitados = []
        cola = deque([verticeInicial])
        while cola:
            vertice = cola.popleft()
            if vertice not in visitados:
                visitados.append(vertice)
                for vecino, peso in self.listaAdy[vertice]:
                    if vecino not in visitados:
                        cola.append(vecino)
        return visitados   
     
    def recorrerEnProfundidad(self, verticeInicial: any) -> List[Any]:              
        if verticeInicial not in self.listaAdy:
            return []
        visitados = []
        pila = [verticeInicial]
        while pila:
            vertice = pila.pop()
            if vertice not in visitados:
                visitados.append(vertice)
                for vecino, peso in self.listaAdy[vertice]:
                    if vecino not in visitados:
                        pila.append(vecino)
        return visitados
    
