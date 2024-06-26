import time
from functools import lru_cache

# Simulación de una función costosa de computar
@lru_cache(maxsize=32)  # maxsize define el tamaño máximo de la caché
def expensive_computation(n):
    print(f"Computing {n}...")
    time.sleep(2)  # Simula una operación costosa que toma tiempo
    return n * n

def main():
    start_time = time.time()
    
    # Llamadas iniciales a la función, estas se calcularán y se almacenarán en caché
    print(expensive_computation(4))
    print(expensive_computation(10))
    print(expensive_computation(4))  # Esta llamada usará el valor en caché
    
    print(f"Time taken: {time.time() - start_time} seconds")
    
    start_time = time.time()
    
    # Llamadas subsecuentes que usan los valores en caché
    print(expensive_computation(10))  # Esta llamada usará el valor en caché
    print(expensive_computation(5))
    
    print(f"Time taken: {time.time() - start_time} seconds")
    
if _name_ == "_main_":
    main()