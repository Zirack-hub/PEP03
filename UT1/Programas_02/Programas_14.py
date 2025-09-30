# Programa 14
# Escribe un programa que reciba un número de bytes y muestre por pantalla
# cuantos GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.

bytes_total = int(input("Introduce la cantidad de bytes: "))

# Sistema decimal (SI)
GB = bytes_total // 1_000_000_000
MB = (bytes_total % 1_000_000_000) // 1_000_000
KB = (bytes_total % 1_000_000) // 1_000
B = bytes_total % 1_000

print(f"{bytes_total} bytes en sistema decimal (SI): {GB} GB, {MB} MB, {KB} KB, {B} bytes")

# Sistema binario (IEC)
GiB = bytes_total // 1_073_741_824
MiB = (bytes_total % 1_073_741_824) // 1_048_576
KiB = (bytes_total % 1_048_576) // 1_024
B_bin = bytes_total % 1_024

print(f"{bytes_total} bytes en sistema binario (IEC): {GiB} GiB, {MiB} MiB, {KiB} KiB, {B_bin} bytes")
