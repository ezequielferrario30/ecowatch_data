from typing import List
from .sensor import Sensor

class Sala:
    """
    Representa una sala física que agrupa sensores.
    Permite agregar sensores y obtener todos los logs de la sala.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.sensores: List[Sensor] = []

    def agregar_sensor(self, sensor: Sensor):
        if not isinstance(sensor, Sensor):
            raise TypeError("Solo se pueden agregar objetos de tipo Sensor")
        self.sensores.append(sensor)

    def logs_sala(self):
        logs = []
        for sensor in self.sensores:
            logs.extend(sensor.logs)
        return logs
