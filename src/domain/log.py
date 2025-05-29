from datetime import datetime

class Log:
    """
    Representa un registro ambiental de un sensor de EcoWatch.
    Incluye validaciones de datos y lógica de alerta crítica.
    """
    def __init__(self, timestamp: str, sala: str, estado: str, temperatura: float, humedad: float, co2: float, mensaje: str = ""):
        self.timestamp = self._validar_timestamp(timestamp)
        self.sala = sala
        self.estado = estado
        self.temperatura = self._validar_temperatura(temperatura)
        self.humedad = self._validar_humedad(humedad)
        self.co2 = self._validar_co2(co2)
        self.mensaje = mensaje

    def _validar_timestamp(self, ts):
        if isinstance(ts, str):
            try:
                return datetime.fromisoformat(ts)
            except Exception:
                raise ValueError("Formato de timestamp inválido")
        if isinstance(ts, datetime):
            return ts
        raise ValueError("Timestamp inválido")

    def _validar_temperatura(self, t):
        t = float(t)
        if not (-40 <= t <= 80):
            raise ValueError("Temperatura fuera de rango físico")
        return t

    def _validar_humedad(self, h):
        h = float(h)
        if not (0 <= h <= 100):
            raise ValueError("Humedad fuera de rango físico")
        return h

    def _validar_co2(self, c):
        c = float(c)
        if not (0 <= c <= 10000):
            raise ValueError("CO2 fuera de rango físico")
        return c

    def es_critico(self):
        return self.estado == "WARNING" or self.co2 > 1000

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "sala": self.sala,
            "estado": self.estado,
            "temperatura": self.temperatura,
            "humedad": self.humedad,
            "co2": self.co2,
            "mensaje": self.mensaje
        }
