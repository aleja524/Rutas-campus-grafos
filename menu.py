from campusUdem import mi_campus_optimizado


def mostrar_lugares():
    print("\nLugares disponibles:")
    for i, lugar in enumerate(mi_campus_optimizado.listaAdy.keys(), 1):
        print(f"  {i}. {lugar}")


def menu():
    while True:
        print("\n========== SISTEMA DE RUTAS UdeM ==========")
        print("1. Ruta más corta (distancia)")
        print("2. Ruta más rápida (tiempo)")
        print("3. Ruta con menor congestión")
        print("4. Ruta accesible (movilidad reducida)")
        print("5. Tour completo del campus (Prim MST)")
        print("6. Ver lugares disponibles")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if opcion == "6":
            mostrar_lugares()
            continue

        if opcion == "5":
            caminos_tour, distancia_tour = mi_campus_optimizado.prim_mst()
            print(f"\nDistancia mínima total: {distancia_tour} metros.")
            print("Recorrido sugerido:")
            for origen, destino, metros in caminos_tour:
                print(f"  • De [{origen}] a [{destino}] - {metros}m")
            continue

        if opcion in ["1", "2", "3", "4"]:
            mostrar_lugares()
            inicio = input("\nLugar de inicio (escriba el nombre exacto): ").strip()
            fin = input("Lugar de destino (escriba el nombre exacto): ").strip()

            if opcion == "1":
                camino, costo = mi_campus_optimizado.dijkstra_personalizado(inicio, fin, "distancia")
                criterio = "distancia"
                accesible = False
            elif opcion == "2":
                camino, costo = mi_campus_optimizado.dijkstra_personalizado(inicio, fin, "tiempo")
                criterio = "tiempo"
                accesible = False
            elif opcion == "3":
                camino, costo = mi_campus_optimizado.dijkstra_personalizado(inicio, fin, "congestion")
                criterio = "congestion"
                accesible = False
            else:
                camino, costo = mi_campus_optimizado.dijkstra_personalizado(inicio, fin, "distancia", solo_accesible=True)
                criterio = "distancia"
                accesible = True

            print(f"\nRuta encontrada: {camino}")
            print(f"Costo total: {costo}")
            print(mi_campus_optimizado.explicar_ruta(camino, costo, criterio, accesible))
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
