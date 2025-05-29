from .estado_por_sala import ReporteEstadoPorSala
from .alertas import ReporteAlertas
from .temp_extremas import ReporteTempExtremas

class ReportFactory:
    """
    Fábrica para instanciar reportes según el tipo solicitado.
    """

    @staticmethod
    def crear_reporte(tipo: str, sala):
        if tipo == "estado_por_sala":
            return ReporteEstadoPorSala(sala)
        elif tipo == "alertas":
            return ReporteAlertas(sala)
        elif tipo == "temp_extremas":
            return ReporteTempExtremas(sala)
        else:
            raise ValueError(f"Tipo de reporte desconocido: {tipo}")
