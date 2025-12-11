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

        datos = [
        ("Tokio", "Japón", 37.4),
        ("Delhi", "India", 30.3),
        ("Shanghái", "China", 27.1),
        ("São Paulo", "Brasil", 22.0),
        ("Ciudad de México", "México", 21.7)
        ]
        
        cursor = conexion.cursor()
        print("Conexión establecida correctamente")
        
        insert = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s)"

    
        cursor.executemany(insert, datos)
        conexion.commit()

        print(f"Se han insertado {cursor.rowcount} filas correctamente")

    print("Tabla creada correctamente")
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")

except Error as a:
            if a.errno == 1050:  # Código de error: table exists
                print("Error: La tabla ya existe.")
            else:
                print(f"Error al crear la tabla: {a}")

finally:
    # Cerrar la conexión si existe
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")