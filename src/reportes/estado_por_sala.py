from .base import BaseReporte

class ReporteEstadoPorSala(BaseReporte):
    def __init__(self, sala):
        self.sala = sala

    def generar(self):
        logs = self.sala.logs_sala()
        if not logs:
            return f"No hay datos para {self.sala.nombre}"
        temps = [log.temperatura for log in logs]
        return {
            "sala": self.sala.nombre,
            "cantidad_logs": len(logs),
            "max_temp": max(temps),
            "min_temp": min(temps),
            "prom_temp": sum(temps)/len(temps),
        }
