from datetime import datetime
from .sala import Sala

class Reporte:
    """
    Genera reportes sobre los registros de una sala.
    Permite obtener resumen diario de temperaturas y CO2.
    """
    def __init__(self, sala: Sala):
        self.sala = sala

    def resumen_diario(self, fecha: datetime):
        logs = [log for log in self.sala.logs_sala() if log.timestamp.date() == fecha.date()]
        if not logs:
            return "Sin datos para esa fecha"
        temps = [log.temperatura for log in logs]
        co2s = [log.co2 for log in logs]
        return {
            "sala": self.sala.nombre,
            "fecha": fecha.date().isoformat(),
            "max_temp": max(temps),
            "min_temp": min(temps),
            "prom_temp": sum(temps)/len(temps),
            "max_co2": max(co2s),
            "min_co2": min(co2s),
            "prom_co2": sum(co2s)/len(co2s),
            "eventos_criticos": sum(log.es_critico() for log in logs)
        }
