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
                for vecino, _ in self.listaAdy[vertice]:
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
                for vecino, _ in self.listaAdy[vertice]:
                    if vecino not in visitados:
                        pila.append(vecino)
        return visitados

campus = GrafoLista()
campus.agregarVertice("Entrada principal")
campus.agregarVertice("Bloque 1 - coliseo")
campus.agregarVertice("Bloque 2 - artes")
campus.agregarVertice("Bloque 3 - laboratorios")
campus.agregarVertice("Bloque 4 - ingenierias")
campus.agregarVertice("Bloque 5 - ciencias basicas")
campus.agregarVertice("Centro idiomas")
campus.agregarVertice("Bloque 7 - ciencias economicas")
campus.agregarVertice("Cancha principal")
campus.agregarVertice("Bloque 9 - audiovisuales")
campus.agregarVertice("Bloque 10 - comunicacion")
campus.agregarVertice("Bloque 11 - posgrados") 
campus.agregarVertice("Bloque 12 - computacion")
campus.agregarVertice("Biblioteca")
campus.agregarVertice("Bloque 13 - derecho")

# 2. CORRECCIÓN: Cambiamos 'peso=' por 'atributos=' en todas las conexiones
campus.agregarConexion("Entrada principal", "Bloque 1 - coliseo",
    atributos={"distancia": 150, "tiempo": 2, "congestion": 3, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Entrada principal", "Biblioteca",
    atributos={"distancia": 120, "tiempo": 2, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Entrada principal", "Bloque 13 - derecho",
    atributos={"distancia": 90, "tiempo": 1, "congestion": 1, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 1 - coliseo", "Cancha principal",
    atributos={"distancia": 80, "tiempo": 1, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 1 - coliseo", "Bloque 2 - artes",
    atributos={"distancia": 200, "tiempo": 3, "congestion": 4, "accesible": False, "estado": "disponible"})

campus.agregarConexion("Bloque 2 - artes", "Bloque 3 - laboratorios",
    atributos={"distancia": 110, "tiempo": 2, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 2 - artes", "Centro idiomas",
    atributos={"distancia": 170, "tiempo": 3, "congestion": 3, "accesible": True, "estado": "mantenimiento"})

campus.agregarConexion("Bloque 3 - laboratorios", "Bloque 4 - ingenierias",
    atributos={"distancia": 95, "tiempo": 1, "congestion": 3, "accesible": False, "estado": "disponible"})

campus.agregarConexion("Bloque 3 - laboratorios", "Bloque 5 - ciencias basicas",
    atributos={"distancia": 130, "tiempo": 2, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 4 - ingenierias", "Bloque 12 - computacion",
    atributos={"distancia": 60, "tiempo": 1, "congestion": 4, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 4 - ingenierias", "Bloque 5 - ciencias basicas",
    atributos={"distancia": 100, "tiempo": 2, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 5 - ciencias basicas", "Bloque 7 - ciencias economicas",
    atributos={"distancia": 180, "tiempo": 3, "congestion": 3, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 7 - ciencias economicas", "Bloque 11 - posgrados",
    atributos={"distancia": 140, "tiempo": 2, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 7 - ciencias economicas", "Centro idiomas",
    atributos={"distancia": 160, "tiempo": 2, "congestion": 1, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 9 - audiovisuales", "Bloque 10 - comunicacion",
    atributos={"distancia": 70, "tiempo": 1, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 10 - comunicacion", "Bloque 11 - posgrados",
    atributos={"distancia": 120, "tiempo": 2, "congestion": 1, "accesible": True, "estado": "bloqueado"})

campus.agregarConexion("Bloque 11 - posgrados", "Bloque 12 - computacion",
    atributos={"distancia": 90, "tiempo": 1, "congestion": 2, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 12 - computacion", "Biblioteca",
    atributos={"distancia": 110, "tiempo": 2, "congestion": 3, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Biblioteca", "Bloque 13 - derecho",
    atributos={"distancia": 85, "tiempo": 1, "congestion": 1, "accesible": True, "estado": "disponible"})

campus.agregarConexion("Bloque 9 - audiovisuales", "Bloque 13 - derecho",
    atributos={"distancia": 200, "tiempo": 3, "congestion": 2, "accesible": True, "estado": "disponible"})


print("¡El grafo del campus se cargó correctamente!")
print(f"Cantidad de lugares registrados: {campus.tamano}\n")


print("--- Recorrido en Anchura (BFS) desde la Entrada ---")
ruta_bfs = campus.recorrerEnAnchura("Entrada principal")
print(ruta_bfs)
print("\n")

print("--- Recorrido en Profundidad (DFS) desde la Entrada ---")
ruta_dfs = campus.recorrerEnProfundidad("Entrada principal")
print(ruta_dfs)
