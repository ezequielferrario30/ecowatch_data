from abc import ABC, abstractmethod

class BaseReporte(ABC):
    @abstractmethod
    def generar(self):
        pass
