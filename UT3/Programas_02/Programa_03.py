"""
Escribe un programa que use los módulos platform y os para:
- Mostrar el procesador donde se ejecuta el programa.
- Mostrar el sistema operativo y versión donde se ejecuta el programa.
- Mostrar el nombre del host donde se ejecuta el programa.
- Mostrar el directorio actual.
"""

import platform
import os

print("Información del sistema")
print("-" * 40)
print(f"Procesador: {platform.processor()}")
print(f"Sistema operativo: {platform.system()}")
print(f"Versión del sistema operativo: {platform.version()}")
print(f"Nombre del host: {platform.node()}")
print(f"Directorio actual: {os.getcwd()}")
