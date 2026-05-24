import heapq
from typing import Any, List, Dict, Tuple
from claseBase import GrafoLista

class CampusUdeM(GrafoLista):
    def __init__(self):
        super().__init__()

    def dijkstra_personalizado(self, inicio: Any, fin: Any, criterio: str, solo_accesible: bool = False) -> Tuple[List[Any], float]:
        if inicio not in self.listaAdy or fin not in self.listaAdy:
            return [], float('inf')
          
        cola_caminos = [[0, inicio, [inicio]]]
        visitados = []

        while len(cola_caminos) > 0:
            indice_minimo = 0
            for i in range(len(cola_caminos)):
                if cola_caminos[i][0] < cola_caminos[indice_minimo][0]:
                    indice_minimo = i
        
            costo_actual, nodo_actual, camino = cola_caminos.pop(indice_minimo)

            if nodo_actual == fin:
                return camino, costo_actual
              
            if nodo_actual in visitados:
                continue
            visitados.append(nodo_actual)

            for vecino, atributos in self.listaAdy[nodo_actual]:
                if vecino in visitados:
                    continue

                if atributos.get("estado") in ["bloqueado", "en mantenimiento"]:
                    continue

                if solo_accesible and not atributos.get("accesible", True):
                    continue
                  
                peso_arista = atributos.get(criterio, float('inf'))
                costo_nuevo = costo_actual + peso_arista
                nueva_ruta = camino + [vecino]
                cola_caminos.append([costo_nuevo, vecino, nueva_ruta])

        return [], float('inf')
