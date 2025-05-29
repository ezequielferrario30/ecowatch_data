# EcoWatch - Sistema de Monitoreo Ambiental

## Descripción

EcoWatch es un sistema modular de ingeniería de datos diseñado para procesar y analizar datos ambientales provenientes de sensores distribuidos en distintas salas. Permite la ingesta, validación, almacenamiento temporal en caché y generación de reportes ejecutivos personalizables que facilitan la toma de decisiones rápidas y basadas en datos.

El sistema está orientado a la extensibilidad y mantenibilidad, aplicando buenas prácticas de programación orientada a objetos y patrones de diseño como Factory y Strategy. Además, cuenta con funcionalidades avanzadas como exportación automática de reportes a CSV y Excel, y logging mediante decoradores.

---

## Estructura del proyecto

ecowatch_data_pipeline/
├── data/
│   └── logs_ambientales_ecowatch.csv
├── src/
│   ├── cache.py
│   ├── log_reader.py
│   ├── main.py
│   ├── domain/
│   │   ├── log.py
│   │   ├── sensor.py
│   │   ├── sala.py
│   │   └── reporte.py
│   ├── reportes/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── estado_por_sala.py
│   │   ├── alertas.py
│   │   └── temp_extremas.py
│   └── utils/
│       ├── __init__.py
│       └── decorators.py
├── tests/
│   └── test_log.py
├── requirements.txt
└── README.md




El sistema:

Lee el archivo CSV con logs ambientales.

Procesa y valida los datos.

Mantiene una caché temporal de los últimos 5 minutos.

Genera reportes (estado por sala, alertas, temperaturas extremas).

Exporta los reportes a archivos CSV y Excel.

Muestra salidas limpias en consola.

Testing
Se incluyen pruebas unitarias básicas con pytest. Para ejecutarlas:



`pytest tests/`

Arquitectura y diseño
Programación Orientada a Objetos para modelar sensores, salas y logs.

Patrón Factory para creación flexible y extensible de reportes.

Patrón Strategy para encapsular lógica de cada tipo de reporte.

Decoradores para logging y posibles extensiones (benchmarking, validaciones).

Caché temporal optimizada para consultas rápidas y manejo de eventos fuera de orden.

Futuras mejoras
Integración con bases de datos para almacenamiento persistente.

Dashboards visuales e interacción en tiempo real.

Alertas automáticas vía email o mensajería.

Más pruebas unitarias y pruebas de integración.

Optimización avanzada para volúmenes masivos de datos.


**Para observar la documentacion de este trabajo podes observarla en el archivo `Ecowatch- documentacion.pdf`**

Autor
Ezequiel Ferrario
GitHub: https://github.com/ezequielferrario30