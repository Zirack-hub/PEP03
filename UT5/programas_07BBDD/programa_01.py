import mysql.connector
from mysql.connector import Error

try:
    # Intentar conectarse a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        database="ciudades",
        user="ciudades",
        password="ciudades"
    )

    if conexion.is_connected():
        print("Conexión establecida correctamente")

except Error as e:
    print(f"Error al conectar a la base de datos: {e}")

finally:
    # Cerrar la conexión si existe
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")
