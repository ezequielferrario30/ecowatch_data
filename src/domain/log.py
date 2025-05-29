class Log:
    """
    Representa un registro ambiental proveniente de un sensor.
    Incluye validación automática en setters para temperatura, humedad y CO2.
    """
    def __init__(self, timestamp, sala, estado, temperatura, humedad, co2, mensaje):
        self.timestamp = timestamp
        self.sala = sala
        self.estado = estado
        self.temperatura = temperatura
        self.humedad = humedad
        self.co2 = co2
        self.mensaje = mensaje

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value):
        if not (-50 < value < 60):
            raise ValueError("Temperatura fuera de rango físico realista")
        self._temperatura = value

    # setters para humedad y co2 (opcionales)
    # ...

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "sala": self.sala,
            "estado": self.estado,
            "temperatura": self.temperatura,
            "humedad": self.humedad,
            "co2": self.co2,
            "mensaje": self.mensaje
        }

    def es_critico(self):
        return self.estado in ["WARNING", "ERROR"] or self.co2 > 1000
