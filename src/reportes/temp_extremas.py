from .base import BaseReporte

class ReporteTempExtremas(BaseReporte):
    def __init__(self, sala):
        self.sala = sala

    def generar(self):
        logs = self.sala.logs_sala()
        extremas = [log for log in logs if log.temperatura < 10 or log.temperatura > 30]
        return {
            "sala": self.sala.nombre,
            "cantidad_temp_extremas": len(extremas),
            "registros_extremos": [log.to_dict() for log in extremas]
        }
