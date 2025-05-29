from .log_reader import CSVLogReader
from .cache import RecentLogsCache
from datetime import datetime, timedelta
from .domain import Log, Sensor, Sala
from .reportes.factory import ReportFactory

def mostrar_alertas_limpio(alertas):
    print(f"\nCantidad de alertas: {alertas['cantidad_alertas']}")
    for i, alerta in enumerate(alertas['alertas'][:3], 1):
        print(f"Alerta {i}: {alerta}")
    if alertas['cantidad_alertas'] > 3:
        print(f"...y {alertas['cantidad_alertas']-3} alertas más.")

def mostrar_extremas_limpio(extremas):
    print(f"\nCantidad de registros extremos: {extremas['cantidad_temp_extremas']}")
    for i, log in enumerate(extremas['registros_extremos'][:3], 1):
        print(f"Extremo {i}: {log}")
    if extremas['cantidad_temp_extremas'] > 3:
        print(f"...y {extremas['cantidad_temp_extremas']-3} más.")

if __name__ == "__main__":
    # 1. Leer logs desde CSV
    file_path = "D:/ecowatch_data_pipeline/data/logs_ambientales_ecowatch.csv"
    reader = CSVLogReader()
    logs = reader.read_logs(file_path)

    # 2. Crear la sala y el sensor de prueba
    sala1 = Sala("Sala_1")
    sensor1 = Sensor("sensor_01", sala1)
    sala1.agregar_sensor(sensor1)

    # 3. Convertir logs crudos en objetos Log y agregarlos al sensor
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

    # 4. Test rápido de cache temporal (opcional, se puede comentar)
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

    # ======================= REPORTES MODULARES (STEP 4/5) =======================

    # 5. Reporte estado por sala (con decorador y pandas)
    reporte_estado = ReportFactory.crear_reporte("estado_por_sala", sala1)
    resultado_estado = reporte_estado.generar()
    print("\nReporte estado por sala:", resultado_estado)

    # Pandas: ver primeros registros y exportar CSV/XLSX
    df_estado = reporte_estado.a_dataframe()
    print("\nPrimeros registros (DataFrame):")
    print(df_estado.head())
    reporte_estado.exportar_csv("estado_sala1.csv")
    reporte_estado.exportar_excel("estado_sala1.xlsx")
    print("-> Exportado como estado_sala1.csv y estado_sala1.xlsx")

    # 6. Reporte de alertas (decorador y print limpio)
    reporte_alertas = ReportFactory.crear_reporte("alertas", sala1)
    resultado_alertas = reporte_alertas.generar()
    mostrar_alertas_limpio(resultado_alertas)

    # 7. Reporte de temperaturas extremas (opcional, decorador y print limpio)
    reporte_extremas = ReportFactory.crear_reporte("temp_extremas", sala1)
    resultado_extremas = reporte_extremas.generar()
    mostrar_extremas_limpio(resultado_extremas)

    print("\n[INFO] Todos los reportes generados correctamente. Revisar archivos .csv/.xlsx exportados.")

