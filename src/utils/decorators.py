import functools

def log_ejecucion(func):
    """Decorator que loguea la ejecución de funciones."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] Finalizado: {func.__name__}")
        return resultado
    return wrapper
