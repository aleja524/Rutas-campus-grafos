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
