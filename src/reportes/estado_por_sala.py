from .base import BaseReporte
from ..utils.decorators import log_ejecucion
import pandas as pd

class ReporteEstadoPorSala(BaseReporte):
    """
    Genera un reporte resumen de estado ambiental de una sala.
    """

    def __init__(self, sala):
        self.sala = sala

    @log_ejecucion
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

    def a_dataframe(self):
        """
        Exporta los logs de la sala como un DataFrame de pandas.
        """
        logs = self.sala.logs_sala()
        data = [log.to_dict() for log in logs]
        return pd.DataFrame(data)

    def exportar_csv(self, filename):
        """
        Exporta los logs de la sala a un archivo .csv.
        """
        df = self.a_dataframe()
        df.to_csv(filename, index=False)

    def exportar_excel(self, filename):
        """
        Exporta los logs de la sala a un archivo .xlsx.
        """
        df = self.a_dataframe()
        df.to_excel(filename, index=False)
