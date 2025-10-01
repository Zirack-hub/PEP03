# Programa 11
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de N segundos.
# Escribe un programa que determine la hora de llegada a la ciudad B.

hh = int(input("Introduce horas de salida: "))
mm = int(input("Introduce minutos de salida: "))
ss = int(input("Introduce segundos de salida: "))
n = int(input("Introduce tiempo de viaje en segundos: "))

total_segundos = hh*3600 + mm*60 + ss + n

hh_llegada = (total_segundos // 3600) % 24
mm_llegada = (total_segundos % 3600) // 60
ss_llegada = total_segundos % 60

print(f"Hora de llegada: {hh_llegada:02d}:{mm_llegada:02d}:{ss_llegada:02d}")
