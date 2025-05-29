from typing import List
from .log import Log

class Sensor:
    """
    Representa un sensor de EcoWatch, asociado a una sala.
    Permite almacenar y consultar logs.
    """
    def __init__(self, sensor_id: str, sala: 'Sala'):
        self.sensor_id = sensor_id
        self.sala = sala
        self.logs: List[Log] = []

    def agregar_log(self, log: Log):
        if not isinstance(log, Log):
            raise TypeError("Solo se pueden agregar objetos de tipo Log")
        self.logs.append(log)

    def ultimos_logs(self, n=5):
        return sorted(self.logs, key=lambda x: x.timestamp, reverse=True)[:n]
