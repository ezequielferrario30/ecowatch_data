"""
Módulo para la lectura y validación de logs ambientales de EcoWatch.

Actualmente soporta archivos CSV, pero está diseñado para permitir la extensión a nuevos formatos
como JSON o bases de datos en el futuro. Cada función de lectura se encarga de validar la presencia
y el formato de los campos clave.

Para agregar una nueva fuente, crear una función de lectura específica y aplicar
el mismo esquema de validación.

Campos requeridos: timestamp, sala, estado, temperatura, humedad, co2, mensaje.

Autor: Ezequiel Ferrario
"""

from abc import ABC, abstractmethod
import csv
from datetime import datetime

class LogReader(ABC):
    @abstractmethod
    def read_logs(self, file_path):
        pass

class CSVLogReader(LogReader):
    def read_logs(self, file_path):
        logs_validos = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader, start=2):
                try:
                    timestamp = row['timestamp']
                    sala = row['sala']
                    estado = row['estado']
                    temperatura = float(row['temperatura'])
                    humedad = float(row['humedad'])
                    co2 = float(row['co2'])
                    mensaje = row.get('mensaje', '')
                    datetime.fromisoformat(timestamp)
                    logs_validos.append({
                        "timestamp": timestamp,
                        "sala": sala,
                        "estado": estado,
                        "temperatura": temperatura,
                        "humedad": humedad,
                        "co2": co2,
                        "mensaje": mensaje
                    })
                except (KeyError, ValueError):
                    # Podés loguear errores aquí
                    pass
        return logs_validos
