# Práctica Grafos: Optimización de Recorridos UdeM
Sistema que ayuda a estudiantes, docentes y visitantes a encontrar rutas eficientes dentro del campus de la Universidad de Medellín, modelando el campus como un grafo ponderado con múltiples criterios de optimización.

## Autores:
Alejandra Escobar - Camila Villero

Universidad de Medellin - Estructura de datos


## Descripción del proyecto

El campus se representa como un grafo no dirigido donde cada *vértice* es un lugar importante (bloques académicos, biblioteca, coliseo, canchas, etc.) y cada *arista* es un camino entre dos lugares. Cada arista guarda cinco atributos:

- *Distancia* en metros
- *Tiempo* estimado de recorrido en minutos
- *Nivel de congestión* (escala numérica)
- *Accesibilidad* para personas con movilidad reducida (booleano)
- *Estado* del camino: disponible, bloqueado o mantenimiento

El sistema implementa:

1. *Dijkstra personalizado*: encuentra la mejor ruta entre dos lugares según el criterio elegido (distancia, tiempo o congestión), con opción de filtrar solo caminos accesibles. Ignora automáticamente caminos en estado bloqueado o mantenimiento.
2. *Prim (Árbol de Expansión Mínima)*: genera un recorrido turístico que conecta todos los lugares del campus minimizando la distancia total, sin repetir lugares.
3. *Explicación de la ruta*: cada ruta calculada incluye una explicación textual del por qué fue seleccionada.
4. *BFS y DFS*: recorridos en anchura y profundidad desde un nodo inicial (heredados de la clase base).


|---claseBase.py (clase grafo lista y construccion del grafo del campus)

|---campusUdem.py (clase campusUdeM con dijkstra, prim y explicar ruta)

|---Readme.md 

## Cómo ejecutar el proyecto

### Requisitos

- Python 3.8 o superior
- No requiere librerías externas (solo módulos de la librería estándar: typing, collections)

### Ejecución

Desde la carpeta del proyecto, en la terminal:

bash
python campusUdem.py

Esto imprime:

1. Cantidad de lugares registrados en el campus
2. Recorrido en anchura (BFS) desde la entrada principal
3. Recorrido en profundidad (DFS) desde la entrada principal
4. Ruta más corta por distancia (Entrada principal → Bloque 4 - ingenierías)
5. Ruta más rápida y accesible (Entrada principal → Bloque 3 - laboratorios)
6. Tour completo del campus generado con Prim (MST)
7. Ruta con menor congestión (Entrada principal → Bloque 7 - ciencias económicas)

Cada ruta calculada muestra el camino, el costo total y la explicación de por qué fue seleccionada.

## Supuestos asumidos

- *Grafo no dirigido*: todos los caminos del campus se pueden recorrer en ambos sentidos. Por eso agregarConexion registra la arista en ambas listas de adyacencia por defecto.
- *Accesibilidad como filtro, no como peso*: dado que la accesibilidad es un atributo booleano (un camino es accesible o no lo es), se implementó como un filtro de aristas en Dijkstra mediante el parámetro solo_accesible=True, no como un criterio numérico de costo. Esto significa que cuando el usuario necesita una ruta accesible, el algoritmo descarta cualquier arista no accesible y luego optimiza según el criterio elegido (distancia, tiempo o congestión).
- *Caminos bloqueados o en mantenimiento*: se ignoran por completo tanto en Dijkstra como en Prim. Si todos los caminos hacia un destino están bloqueados, el sistema devuelve una ruta vacía y costo infinito.
- *Prim sin restricciones de movilidad*: el tour para visitantes asume que estos no tienen restricciones de accesibilidad, por lo que el MST no filtra por el atributo accesible. Solo descarta caminos bloqueados o en mantenimiento.
- *Atributos por defecto*: si una conexión se crea sin especificar atributos, se le asignan valores razonables por defecto (distancia 10m, tiempo 2min, congestión 1, accesible, disponible).
- *Reconstrucción de ruta dentro del algoritmo*: en lugar de usar un diccionario de "padres" para reconstruir el camino al final, se arrastra la lista del camino dentro de cada elemento de la cola de prioridad. Esto simplifica el código a costa de un poco más de memoria.
- *Cola de prioridad implementada manualmente*: la cola de Dijkstra se gestiona como una lista a la que se le busca el mínimo en cada iteración (búsqueda lineal), en lugar de usar heapq. Funciona correctamente para el tamaño del grafo del campus.

## Algoritmos implementados

| Algoritmo | Propósito | Complejidad aproximada |
|---|---|---|
| BFS | Recorrido en anchura desde un nodo | O(V + E) |
| DFS | Recorrido en profundidad desde un nodo | O(V + E) |
| Dijkstra personalizado | Ruta óptima entre dos nodos según criterio | O(V²) con la implementación actual |
| Prim (MST) | Árbol de expansión mínima del grafo completo | O(V²) |
