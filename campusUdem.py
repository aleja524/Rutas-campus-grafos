import heapq
from typing import Any, List, Dict, Tuple
from claseBase import GrafoLista
from claseBase import GrafoLista, campus

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

                if atributos.get("estado") in ["bloqueado", "mantenimiento"]:
                    continue

                if solo_accesible and not atributos.get("accesible", True):
                    continue
                  
                peso_arista = atributos.get(criterio, float('inf'))
                costo_nuevo = costo_actual + peso_arista
                nueva_ruta = camino + [vecino]
                cola_caminos.append([costo_nuevo, vecino, nueva_ruta])

        return [], float('inf')
    
    def prim_mst(self) -> Tuple[List[Tuple[Any, Any, float]], float]:
        if not self.listaAdy:
            return [], 0

        nodo_inicial = list(self.listaAdy.keys())[0]
        visitados = [nodo_inicial]
        
        caminos_elegidos = []
        distancia_total = 0

        while len(visitados) < self.tamano:
            
            menor_distancia = float('inf') 
            mejor_origen = None
            mejor_destino = None

            for nodo_v in visitados:
                for vecino, atributos in self.listaAdy[nodo_v]:
                    if atributos.get("estado") in ["bloqueado", "mantenimiento"]:
                        continue
                    
                    if vecino in visitados:
                        continue
                    
                    distancia_actual = atributos.get("distancia", 10)

                    if distancia_actual < menor_distancia:
                        menor_distancia = distancia_actual
                        mejor_origen = nodo_v
                        mejor_destino = vecino

            if mejor_destino is None:
                break

            visitados.append(mejor_destino)
            caminos_elegidos.append((mejor_origen, mejor_destino, menor_distancia))
            distancia_total += menor_distancia

        return caminos_elegidos, distancia_total


mi_campus_optimizado = CampusUdeM()
mi_campus_optimizado.listaAdy = campus.listaAdy
mi_campus_optimizado.tamano = campus.tamano

print("\n=========================================================")
print("          PRUEBAS DE OPTIMIZACIÓN DE RECORRIDOS          ")
print("=========================================================\n")

print("--- 1. Buscando la ruta más corta (Criterio: distancia) ---")
camino_corto, costo_distancia = mi_campus_optimizado.dijkstra_personalizado(
    inicio="Entrada principal", 
    fin="Bloque 4 - ingenierias", 
    criterio="distancia"
)
print(f"Ruta óptima: {camino_corto}")
print(f"Distancia total: {costo_distancia} metros.\n")


print("--- 2. Buscando la ruta más rápida y accesible (Movilidad Reducida) ---")
camino_rapido, costo_tiempo = mi_campus_optimizado.dijkstra_personalizado(
    inicio="Entrada principal", 
    fin="Bloque 3 - laboratorios", 
    criterio="tiempo", 
    solo_accesible=True
)

print(f"Ruta óptima accesible: {camino_rapido}")
print(f"Tiempo estimado: {costo_tiempo} minutos.\n")
print("--- 3. Generando Tour del Campus para Visitantes (Prim MST) ---")
caminos_tour, distancia_tour = mi_campus_optimizado.prim_mst()
print(f"Distancia mínima total para conectar todo el campus: {distancia_tour} metros.")
print("Caminos sugeridos para el recorrido sin repetir lugares:")
for origen, destino, metros in caminos_tour:
    print(f"  • De [{origen}] hacia [{destino}] recorriendo {metros}m")
print("=========================================================")
