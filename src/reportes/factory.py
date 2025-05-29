from .estado_por_sala import ReporteEstadoPorSala
from .alertas import ReporteAlertas
from .temp_extremas import ReporteTempExtremas


class ReportFactory:
    @staticmethod
    def crear_reporte(tipo: str, sala):
        if tipo == "estado_por_sala":
            return ReporteEstadoPorSala(sala)
        elif tipo == "alertas":
            return ReporteAlertas(sala)
        else:
            raise ValueError(f"Tipo de reporte desconocido: {tipo}")

class ReportFactory:
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
