import heapq
from typing import Any, List, Tuple
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
    
    def explicar_ruta(self, camino: List[Any], costo: float, criterio: str, solo_accesible: bool = False) -> str:
        if not camino:
            return ("No se encontró una ruta válida. Puede que el destino no exista, "
                    "que todos los caminos estén bloqueados o en mantenimiento, "
                    "o que no haya rutas accesibles disponibles.")
        
        unidades = {
            "distancia": "metros",
            "tiempo": "minutos",
            "congestion": "puntos de congestión"
        }
        unidad = unidades.get(criterio, "unidades")
        
        explicacion = (
            f"Se eligió esta ruta porque minimiza el criterio '{criterio}' "
            f"con un costo total de {costo} {unidad}. "
            f"El recorrido pasa por {len(camino)} lugares e ignora caminos "
            f"en estado 'bloqueado' o 'mantenimiento'."
        )
        
        if solo_accesible:
            explicacion += " Además, solo considera caminos accesibles para personas con movilidad reducida."
        
        return explicacion
    
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
print(f"Distancia total: {costo_distancia} metros.")
print(mi_campus_optimizado.explicar_ruta(camino_corto, costo_distancia, "distancia"))
print()

print("--- 2. Buscando la ruta más rápida y accesible (Movilidad Reducida) ---")
camino_rapido, costo_tiempo = mi_campus_optimizado.dijkstra_personalizado(
    inicio="Entrada principal",
    fin="Bloque 3 - laboratorios",
    criterio="tiempo",
    solo_accesible=True
)
print(f"Ruta óptima accesible: {camino_rapido}")
print(f"Tiempo estimado: {costo_tiempo} minutos.")
print(mi_campus_optimizado.explicar_ruta(camino_rapido, costo_tiempo, "tiempo", solo_accesible=True))
print()

print("--- 3. Generando Tour del Campus para Visitantes (Prim MST) ---")
caminos_tour, distancia_tour = mi_campus_optimizado.prim_mst()
print(f"Distancia mínima total para conectar todo el campus: {distancia_tour} metros.")
print("Caminos sugeridos para el recorrido sin repetir lugares:")
for origen, destino, metros in caminos_tour:
    print(f"  • De [{origen}] hacia [{destino}] recorriendo {metros}m")
print()

print("--- 4. Buscando la ruta con menor congestión ---")
camino_calmo, costo_congestion = mi_campus_optimizado.dijkstra_personalizado(
    inicio="Entrada principal",
    fin="Bloque 7 - ciencias economicas",
    criterio="congestion"
)
print(f"Ruta menos congestionada: {camino_calmo}")
print(f"Congestión total: {costo_congestion}")
print(mi_campus_optimizado.explicar_ruta(camino_calmo, costo_congestion, "congestion"))
print("=========================================================")
