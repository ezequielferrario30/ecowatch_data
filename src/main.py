from log_reader import CSVLogReader
from cache import RecentLogsCache
from datetime import datetime, timedelta

if __name__ == "__main__":
    file_path = "D:/ecowatch_data_pipeline/data/logs_ambientales_ecowatch.csv"
    reader = CSVLogReader()
    logs = reader.read_logs(file_path)

    cache = RecentLogsCache(window_minutes=5)

    # Simulamos que llegan en orden
    for log in logs:
        cache.add_log(log)

    # Consultar los registros recientes de una sala específica
    sala_ejemplo = "Sala_1"
    recientes_sala = cache.query_by_sala(sala_ejemplo)
    print(f"Registros recientes para {sala_ejemplo}: {len(recientes_sala)}")

    # Consultar por timestamp específico
    timestamp_ejemplo = logs[0]["timestamp"]
    registros_timestamp = cache.query_by_timestamp(timestamp_ejemplo)
    print(f"Registros para timestamp {timestamp_ejemplo}: {len(registros_timestamp)}")

    # ---------- MINI TEST MANUAL DE CACHE (late events y ventanas) ----------
    # Simular un log "antiguo" de hace 6 minutos (debería ser eliminado)
    log_antiguo = logs[0].copy()
    t_base = max(datetime.fromisoformat(log["timestamp"]) for log in logs)
    t_antiguo = (t_base - timedelta(minutes=6)).isoformat()
    log_antiguo["timestamp"] = t_antiguo
    log_antiguo["sala"] = "Sala_test_fuera"
    cache.add_log(log_antiguo)

    # Simular logs dentro de la ventana (últimos 5 minutos)
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
