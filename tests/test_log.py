import unittest
from src.domain import Log
from src.domain.log import Log
import pytest

class TestLog(unittest.TestCase):
    def test_valid_log(self):
        log = Log(
            timestamp="2025-05-01T08:00:00",
            sala="Sala_1",
            estado="INFO",
            temperatura=25.0,
            humedad=50.0,
            co2=900,
            mensaje="OK"
        )
        self.assertEqual(log.sala, "Sala_1")
        self.assertFalse(log.es_critico())

    def test_critical_log(self):
        log = Log(
            timestamp="2025-05-01T08:00:00",
            sala="Sala_1",
            estado="WARNING",
            temperatura=25.0,
            humedad=50.0,
            co2=1500,
            mensaje="ALERTA"
        )
        self.assertTrue(log.es_critico())

    def test_invalid_temp(self):
        with self.assertRaises(ValueError):
            Log("2025-05-01T08:00:00", "Sala_1", "INFO", 200, 50, 800)

    def test_invalid_humidity(self):
        with self.assertRaises(ValueError):
            Log("2025-05-01T08:00:00", "Sala_1", "INFO", 25, 200, 800)

    def test_invalid_co2(self):
        with self.assertRaises(ValueError):
            Log("2025-05-01T08:00:00", "Sala_1", "INFO", 25, 50, 15000)

if __name__ == "__main__":
    unittest.main()


def test_temperatura_fuera_de_rango():
    with pytest.raises(ValueError):
        Log("2024-01-01T00:00", "A", "INFO", 100, 50, 400, "msg")
