from .base import BaseReporte
from ..utils.decorators import log_ejecucion

class ReporteTempExtremas(BaseReporte):
    """
    Reporte de registros con temperaturas fuera de los valores normales.
    """

    def __init__(self, sala):
        self.sala = sala

    @log_ejecucion
    def generar(self):
        logs = self.sala.logs_sala()
        extremas = [log for log in logs if log.temperatura < 10 or log.temperatura > 30]
        return {
            "sala": self.sala.nombre,
            "cantidad_temp_extremas": len(extremas),
            "registros_extremos": [log.to_dict() for log in extremas]
        }
