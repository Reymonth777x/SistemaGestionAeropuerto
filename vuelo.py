import math


class Vuelo:
    """Representa un vuelo y sus datos principales."""

    def __init__(self, codigo, aerolinea, destino, hora, puerta, estado, pasajeros, capacidad):
        self.codigo = codigo
        self.aerolinea = aerolinea
        self.destino = destino
        self.hora = hora
        self.puerta = puerta
        self.estado = estado
        self.pasajeros = pasajeros
        self.capacidad = capacidad

    def calcular_ocupacion(self):
        """Calcula el porcentaje de ocupación usando math.floor()."""
        if self.capacidad == 0:
            return 0

        porcentaje = (self.pasajeros / self.capacidad) * 100
        return math.floor(porcentaje)

    def mostrar_informacion(self):
        """Devuelve la información completa del vuelo en forma de texto."""
        return (
            f"Código de vuelo    : {self.codigo}\n"
            f"Aerolínea          : {self.aerolinea}\n"
            f"Destino            : {self.destino}\n"
            f"Hora de salida     : {self.hora}\n"
            f"Puerta de abordaje : {self.puerta}\n"
            f"Estado             : {self.estado.upper()}\n"
            f"Pasajeros          : {self.pasajeros}\n"
            f"Capacidad          : {self.capacidad}\n"
            f"Ocupación          : {self.calcular_ocupacion()}%"
        )

    def a_diccionario(self):
        """Convierte el objeto en el diccionario solicitado por el proyecto."""
        return {
            "codigo": self.codigo,
            "aerolinea": self.aerolinea,
            "destino": self.destino,
            "hora": self.hora,
            "puerta": self.puerta,
            "estado": self.estado,
            "pasajeros": self.pasajeros,
            "capacidad": self.capacidad,
        }
