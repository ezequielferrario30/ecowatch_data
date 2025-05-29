from .base import BaseReporte

class ReporteAlertas(BaseReporte):
    def __init__(self, sala):
        self.sala = sala

    def generar(self):
        logs = self.sala.logs_sala()
        alertas = [log for log in logs if log.es_critico()]
        return {
            "sala": self.sala.nombre,
            "cantidad_alertas": len(alertas),
            "alertas": [log.to_dict() for log in alertas]
        }
