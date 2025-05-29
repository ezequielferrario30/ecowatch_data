from abc import ABC, abstractmethod

class BaseReporte(ABC):
    """
    Clase base abstracta para todos los reportes.
    """

    @abstractmethod
    def generar(self):
        pass
