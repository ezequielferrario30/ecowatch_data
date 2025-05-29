from .base import BaseReporte
from ..utils.decorators import log_ejecucion

class ReporteAlertas(BaseReporte):
    """
    Genera un reporte de alertas ambientales en una sala.
    """

    def __init__(self, sala):
        self.sala = sala

    @log_ejecucion
    def generar(self):
        logs = self.sala.logs_sala()
        alertas = [log for log in logs if log.es_critico()]
        return {
            "sala": self.sala.nombre,
            "cantidad_alertas": len(alertas),
            "alertas": [log.to_dict() for log in alertas]
        }
