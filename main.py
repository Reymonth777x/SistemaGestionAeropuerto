"""
Archivo principal del Sistema de Gestión Aeroportuaria.

main.py se encarga del menú y de llamar las funciones del módulo
 gestor_vuelos.py. La lista_vuelos se mantiene aquí durante la ejecución.
"""

from gestor_vuelos import (
    agregar_vuelo,
    buscar_vuelo,
    eliminar_vuelo,
    mostrar_todos_los_vuelos,
    mostrar_panel_vuelos,
    mostrar_estadisticas,
    guardar_vuelos_en_archivo,
    leer_vuelos_desde_archivo,
    mostrar_informacion_sistema,
)


def mostrar_menu():
    print("\n" + "=" * 60)
    print("SISTEMA DE GESTIÓN AEROPORTUARIA".center(60))
    print("=" * 60)
    print("1. Registrar vuelo")
    print("2. Buscar vuelo")
    print("3. Eliminar vuelo")
    print("4. Mostrar todos los vuelos")
    print("5. Ver panel de vuelos")
    print("6. Ver estadísticas")
    print("7. Guardar vuelos en archivo")
    print("8. Consultar archivo de vuelos")
    print("9. Ver información del sistema")
    print("10. Salir")
    print("=" * 60)


def solicitar_opcion_menu():
    try:
        return int(input("Seleccione una opción (1-10): "))
    except ValueError:
        print("Opción inválida. Debe ingresar un número.")
        return None


def main():
    """Controla el ciclo principal del programa."""
    lista_vuelos = []

    print("\nBienvenido al Sistema de Gestión Aeroportuaria.")
    print("Sistema iniciado correctamente.")

    while True:
        mostrar_menu()
        opcion = solicitar_opcion_menu()

        if opcion is None:
            continue

        if opcion == 1:
            agregar_vuelo(lista_vuelos)
        elif opcion == 2:
            buscar_vuelo(lista_vuelos)
        elif opcion == 3:
            eliminar_vuelo(lista_vuelos)
        elif opcion == 4:
            mostrar_todos_los_vuelos(lista_vuelos)
        elif opcion == 5:
            mostrar_panel_vuelos(lista_vuelos)
        elif opcion == 6:
            mostrar_estadisticas(lista_vuelos)
        elif opcion == 7:
            guardar_vuelos_en_archivo(lista_vuelos)
        elif opcion == 8:
            leer_vuelos_desde_archivo()
        elif opcion == 9:
            mostrar_informacion_sistema()
        elif opcion == 10:
            print("\nSistema cerrado correctamente. Hasta pronto.")
            break
        else:
            print("Opción fuera de rango. Seleccione una opción del 1 al 10.")


if __name__ == "__main__":
    main()
