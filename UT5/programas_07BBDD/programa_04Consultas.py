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

        
        
        cursor = conexion.cursor()
        print("Conexión establecida correctamente")
        
        select = "SELECT nombre, pais, poblacion_millones FROM ciudades WHERE poblacion_millones > 25"

        cursor.execute(select)
        resultados =cursor.fetchall()

        for fila in resultados:
            ciudad, pais, poblacion = fila
            print(f"Ciudad: {ciudad}, Pais:{pais}, Poblacion:{poblacion}")

        ##for fila in cursor:


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