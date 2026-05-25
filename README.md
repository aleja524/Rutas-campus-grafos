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
