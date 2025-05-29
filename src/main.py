from .log_reader import CSVLogReader
from .cache import RecentLogsCache
from datetime import datetime, timedelta
from .domain import Log, Sensor, Sala, Reporte


if __name__ == "__main__":
    file_path = "D:/ecowatch_data_pipeline/data/logs_ambientales_ecowatch.csv"
    reader = CSVLogReader()
    logs = reader.read_logs(file_path)

    # =================== STEP 3: OO Y PRUEBA RÁPIDA ===================
    # Crear la sala y un sensor de prueba (en la práctica tendrías varios sensores por sala)
    sala1 = Sala("Sala_1")
    sensor1 = Sensor("sensor_01", sala1)
    sala1.agregar_sensor(sensor1)

    # Convertir cada log leído del CSV en un objeto Log y agregarlos al sensor
    for row in logs:
        if row["sala"] == "Sala_1":
            log_obj = Log(
                timestamp=row["timestamp"],
                sala=row["sala"],
                estado=row["estado"],
                temperatura=float(row["temperatura"]),
                humedad=float(row["humedad"]),
                co2=float(row["co2"]),
                mensaje=row.get("mensaje", "")
            )
            sensor1.agregar_log(log_obj)

    # Generar y mostrar un reporte diario para la sala
    reporte = Reporte(sala1)
    # Usamos el día del primer log de la sala (ajustá según tus datos)
    if sensor1.logs:
        fecha_reporte = sensor1.logs[0].timestamp
        print("\nReporte diario de Sala_1:")
        print(reporte.resumen_diario(fecha_reporte))
    else:
        print("No hay logs para Sala_1.")

    # =================== STEP 2: TESTS DE CACHÉ (opcional) ===================
    cache = RecentLogsCache(window_minutes=5)
    for log in logs:
        cache.add_log(log)

    sala_ejemplo = "Sala_1"
    recientes_sala = cache.query_by_sala(sala_ejemplo)
    print(f"Registros recientes para {sala_ejemplo}: {len(recientes_sala)}")

    if logs:
        timestamp_ejemplo = logs[0]["timestamp"]
        registros_timestamp = cache.query_by_timestamp(timestamp_ejemplo)
        print(f"Registros para timestamp {timestamp_ejemplo}: {len(registros_timestamp)}")

    # ---------- MINI TEST MANUAL DE CACHE (late events y ventanas) ----------
    t_base = max(datetime.fromisoformat(log["timestamp"]) for log in logs)
    log_antiguo = logs[0].copy()
    t_antiguo = (t_base - timedelta(minutes=6)).isoformat()
    log_antiguo["timestamp"] = t_antiguo
    log_antiguo["sala"] = "Sala_test_fuera"
    cache.add_log(log_antiguo)

    for i in range(5):
        log = logs[0].copy()
        t_log = (t_base - timedelta(minutes=i)).isoformat()
        log["timestamp"] = t_log
        log["sala"] = f"Sala_test_{i}"
        cache.add_log(log)

    print("\n--- TEST DE CACHE MANUAL ---")
    print(f"Registros totales en cache: {sum(len(v) for v in cache.logs_by_sala.values())}")
    for i in range(5):
        sala_test = f"Sala_test_{i}"
        esta = "Sí" if cache.query_by_sala(sala_test) else "No"
        print(f"¿Incluye la {sala_test}? {esta}")
    print(f"¿Incluye Sala_test_fuera? {'Sí' if cache.query_by_sala('Sala_test_fuera') else 'No'}")
