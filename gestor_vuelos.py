"""
Módulo: gestor_vuelos.py

Aquí se concentra la lógica del sistema. La información principal se
mantiene en una lista de diccionarios, tal como solicita el proyecto.
La clase Vuelo se utiliza para aplicar POO y realizar cálculos/mensajes.
"""

import math
import platform
import random

from vuelo import Vuelo

NOMBRE_ARCHIVO = "vuelos.txt"
ESTADOS_VALIDOS = ["programado", "abordando", "retrasado", "cancelado", "finalizado"]


def mostrar_titulo(titulo):
    print("\n" + "=" * 60)
    print(titulo.center(60))
    print("=" * 60)


def solicitar_texto_no_vacio(mensaje):
    """Repite la solicitud hasta recibir un texto válido."""
    while True:
        valor = input(mensaje).strip()

        if valor == "":
            print("El campo no puede quedar vacío.")
        else:
            return valor


def solicitar_numero_entero(mensaje, minimo=0):
    """Solicita un entero y controla errores de conversión."""
    while True:
        try:
            valor = int(input(mensaje))

            if valor < minimo:
                print(f"El valor debe ser mayor o igual que {minimo}.")
            else:
                return valor

        except ValueError:
            print("Dato inválido. Debe ingresar un número entero.")


def solicitar_hora():
    """Valida una hora básica en formato HH:MM sin usar módulos nuevos."""
    while True:
        hora = input("Hora de salida (HH:MM): ").strip()
        partes = hora.split(":")

        if len(partes) != 2:
            print("Formato inválido. Ejemplo correcto: 14:30")
            continue

        try:
            horas = int(partes[0])
            minutos = int(partes[1])

            if horas < 0 or horas > 23:
                print("La hora debe estar entre 00 y 23.")
                continue

            if minutos < 0 or minutos > 59:
                print("Los minutos deben estar entre 00 y 59.")
                continue

            return f"{horas:02d}:{minutos:02d}"

        except ValueError:
            print("La hora y los minutos deben ser números.")


def codigo_existe(lista_vuelos, codigo):
    """Comprueba si un código ya está registrado."""
    for vuelo in lista_vuelos:
        if vuelo["codigo"].lower() == codigo.lower():
            return True

    return False


def puerta_existe(lista_vuelos, puerta):
    """Comprueba si una puerta ya está asignada."""
    for vuelo in lista_vuelos:
        if vuelo["puerta"].lower() == puerta.lower():
            return True

    return False


def generar_codigo_vuelo(lista_vuelos):
    """Genera un código aleatorio y evita duplicados."""
    while True:
        numero = random.randint(100, 999)
        codigo = f"VL{numero}"

        if not codigo_existe(lista_vuelos, codigo):
            return codigo


def generar_puerta_abordaje(lista_vuelos):
    """Genera una puerta libre entre 1 y 30."""
    while True:
        numero = random.randint(1, 30)
        puerta = f"Puerta {numero}"

        if not puerta_existe(lista_vuelos, puerta):
            return puerta


def solicitar_estado_vuelo():
    """Solicita uno de los estados permitidos por el proyecto."""
    while True:
        print("\nEstados disponibles:")
        for estado in ESTADOS_VALIDOS:
            print(f"- {estado}")

        estado = input("Estado del vuelo: ").strip().lower()

        if estado in ESTADOS_VALIDOS:
            return estado

        print("Estado no válido.")


def agregar_vuelo(lista_vuelos):
    """Solicita, valida y agrega un vuelo como diccionario."""
    mostrar_titulo("REGISTRAR VUELO")

    codigo = input("Código de vuelo (Enter = automático): ").strip().upper()

    if codigo == "":
        codigo = generar_codigo_vuelo(lista_vuelos)
        print(f"Código generado: {codigo}")
    elif codigo_existe(lista_vuelos, codigo):
        print("Ese código ya está registrado.")
        return

    aerolinea = solicitar_texto_no_vacio("Aerolínea: ")
    destino = solicitar_texto_no_vacio("Destino: ")
    hora = solicitar_hora()

    puerta = input("Puerta de abordaje (Enter = automática): ").strip()

    if puerta == "":
        puerta = generar_puerta_abordaje(lista_vuelos)
        print(f"Puerta asignada: {puerta}")
    elif puerta_existe(lista_vuelos, puerta):
        print("Esa puerta ya está asignada a otro vuelo.")
        return

    estado = solicitar_estado_vuelo()
    pasajeros = solicitar_numero_entero("Cantidad de pasajeros: ", 0)
    capacidad = solicitar_numero_entero("Capacidad del avión: ", 1)

    if pasajeros > capacidad:
        print("No se puede registrar el vuelo: los pasajeros superan la capacidad.")
        return

    nuevo_vuelo = Vuelo(
        codigo,
        aerolinea,
        destino,
        hora,
        puerta,
        estado,
        pasajeros,
        capacidad,
    )

    lista_vuelos.append(nuevo_vuelo.a_diccionario())

    print("\nVuelo registrado correctamente.")
    print(f"Código: {codigo}")
    print(f"Ocupación: {nuevo_vuelo.calcular_ocupacion()}%")


def buscar_vuelo(lista_vuelos):
    """Busca un vuelo por código y utiliza un objeto Vuelo para mostrarlo."""
    mostrar_titulo("BUSCAR VUELO")
    codigo = solicitar_texto_no_vacio("Código del vuelo: ").upper()

    for datos_vuelo in lista_vuelos:
        if datos_vuelo["codigo"].upper() == codigo:
            vuelo = Vuelo(
                datos_vuelo["codigo"],
                datos_vuelo["aerolinea"],
                datos_vuelo["destino"],
                datos_vuelo["hora"],
                datos_vuelo["puerta"],
                datos_vuelo["estado"],
                datos_vuelo["pasajeros"],
                datos_vuelo["capacidad"],
            )

            print("\nVuelo encontrado:\n")
            print(vuelo.mostrar_informacion())
            return

    print(f"No se encontró el vuelo {codigo}.")


def eliminar_vuelo(lista_vuelos):
    """Elimina un vuelo existente por medio de su código."""
    mostrar_titulo("ELIMINAR VUELO")
    codigo = solicitar_texto_no_vacio("Código del vuelo: ").upper()

    for posicion in range(len(lista_vuelos)):
        if lista_vuelos[posicion]["codigo"].upper() == codigo:
            vuelo = lista_vuelos[posicion]

            if vuelo["estado"] not in ["cancelado", "finalizado"]:
                confirmar = input(
                    "El vuelo no está cancelado ni finalizado. ¿Desea eliminarlo? (s/n): "
                ).strip().lower()

                if confirmar != "s":
                    print("Operación cancelada.")
                    return

            lista_vuelos.pop(posicion)
            print(f"El vuelo {codigo} fue eliminado correctamente.")
            return

    print(f"No existe un vuelo con el código {codigo}.")


def mostrar_todos_los_vuelos(lista_vuelos):
    """Muestra todos los vuelos registrados."""
    mostrar_titulo("LISTADO DE VUELOS")

    if len(lista_vuelos) == 0:
        print("No hay vuelos registrados.")
        return

    for datos_vuelo in lista_vuelos:
        vuelo = Vuelo(
            datos_vuelo["codigo"],
            datos_vuelo["aerolinea"],
            datos_vuelo["destino"],
            datos_vuelo["hora"],
            datos_vuelo["puerta"],
            datos_vuelo["estado"],
            datos_vuelo["pasajeros"],
            datos_vuelo["capacidad"],
        )

        print("-" * 60)
        print(vuelo.mostrar_informacion())

    print("-" * 60)
    print(f"Total de vuelos: {len(lista_vuelos)}")


def mostrar_panel_vuelos(lista_vuelos):
    """Muestra una vista compacta parecida a un panel aeroportuario."""
    mostrar_titulo("PANEL DE VUELOS")

    if len(lista_vuelos) == 0:
        print("No hay vuelos para mostrar.")
        return

    print(f"{'CÓDIGO':<10}{'AEROLÍNEA':<18}{'DESTINO':<18}{'HORA':<8}{'PUERTA':<12}{'ESTADO':<12}")
    print("-" * 78)

    for vuelo in lista_vuelos:
        print(
            f"{vuelo['codigo']:<10}"
            f"{vuelo['aerolinea'][:17]:<18}"
            f"{vuelo['destino'][:17]:<18}"
            f"{vuelo['hora']:<8}"
            f"{vuelo['puerta']:<12}"
            f"{vuelo['estado']:<12}"
        )

    print("-" * 78)
    print(f"Vuelos registrados: {len(lista_vuelos)}")


def calcular_promedio_pasajeros(lista_vuelos):
    """Calcula el promedio de pasajeros y usa math.floor()."""
    if len(lista_vuelos) == 0:
        return 0

    total = 0

    for vuelo in lista_vuelos:
        total += vuelo["pasajeros"]

    promedio = total / len(lista_vuelos)
    return math.floor(promedio)


def contar_estado(lista_vuelos, estado):
    """Cuenta cuántos vuelos tienen un estado determinado."""
    cantidad = 0

    for vuelo in lista_vuelos:
        if vuelo["estado"] == estado:
            cantidad += 1

    return cantidad


def mostrar_estadisticas(lista_vuelos):
    """Presenta estadísticas básicas relacionadas con la operación."""
    mostrar_titulo("ESTADÍSTICAS DEL AEROPUERTO")

    if len(lista_vuelos) == 0:
        print("No hay vuelos registrados para calcular estadísticas.")
        return

    total_pasajeros = 0
    mayor_ocupacion = -1
    vuelo_mayor_ocupacion = None

    for datos_vuelo in lista_vuelos:
        vuelo = Vuelo(
            datos_vuelo["codigo"],
            datos_vuelo["aerolinea"],
            datos_vuelo["destino"],
            datos_vuelo["hora"],
            datos_vuelo["puerta"],
            datos_vuelo["estado"],
            datos_vuelo["pasajeros"],
            datos_vuelo["capacidad"],
        )

        total_pasajeros += vuelo.pasajeros
        ocupacion = vuelo.calcular_ocupacion()

        if ocupacion > mayor_ocupacion:
            mayor_ocupacion = ocupacion
            vuelo_mayor_ocupacion = vuelo.codigo

    print(f"Vuelos registrados      : {len(lista_vuelos)}")
    print(f"Total de pasajeros     : {total_pasajeros}")
    print(f"Promedio de pasajeros  : {calcular_promedio_pasajeros(lista_vuelos)}")
    print(f"Mayor ocupación        : {vuelo_mayor_ocupacion} ({mayor_ocupacion}%)")
    print(f"Programados            : {contar_estado(lista_vuelos, 'programado')}")
    print(f"Abordando              : {contar_estado(lista_vuelos, 'abordando')}")
    print(f"Retrasados             : {contar_estado(lista_vuelos, 'retrasado')}")
    print(f"Cancelados             : {contar_estado(lista_vuelos, 'cancelado')}")
    print(f"Finalizados            : {contar_estado(lista_vuelos, 'finalizado')}")


def guardar_vuelos_en_archivo(lista_vuelos):
    """Guarda los vuelos utilizando el modo 'a' """
    mostrar_titulo("GUARDAR VUELOS")

    if len(lista_vuelos) == 0:
        print("No hay vuelos registrados para guardar.")
        return
    try:
        with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write("\n" + "=" * 60 + "\n")
            archivo.write("REGISTRO DE VUELOS - SISTEMA DE GESTIÓN AEROPORTUARIA\n")
            archivo.write("=" * 60 + "\n")

            for datos_vuelo in lista_vuelos:
                vuelo = Vuelo(
                    datos_vuelo["codigo"],
                    datos_vuelo["aerolinea"],
                    datos_vuelo["destino"],
                    datos_vuelo["hora"],
                    datos_vuelo["puerta"],
                    datos_vuelo["estado"],
                    datos_vuelo["pasajeros"],
                    datos_vuelo["capacidad"],
                )

                archivo.write(vuelo.mostrar_informacion())
                archivo.write("\n" + "-" * 60 + "\n")

        print(f"Información agregada correctamente a '{NOMBRE_ARCHIVO}'.")

    except (IOError, OSError) as error:
        print(f"No se pudo guardar el archivo: {error}")


def leer_vuelos_desde_archivo():
    """Lee el archivo usando el modo 'r'."""
    mostrar_titulo("CONSULTAR ARCHIVO")

    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            if contenido.strip() == "":
                print("El archivo está vacío.")
            else:
                print(contenido)

    except FileNotFoundError:
        print(f"El archivo '{NOMBRE_ARCHIVO}' todavía no existe.")
    except (IOError, OSError) as error:
        print(f"No se pudo leer el archivo: {error}")


def mostrar_informacion_sistema():
    """Muestra información del equipo utilizando platform."""
    mostrar_titulo("INFORMACIÓN DEL SISTEMA")
    print(f"Sistema operativo : {platform.system()}")
    print(f"Versión           : {platform.version()}")
    print(f"Equipo            : {platform.node()}")
    print(f"Plataforma        : {platform.platform()}")
    print(f"Python            : {platform.python_version()}")
