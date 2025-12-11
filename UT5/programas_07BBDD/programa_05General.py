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
        try:

            datos =[("Madrid", "España", 6.8)]
            
            cursor = conexion.cursor()
            insert = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s)"
            cursor.executemany(insert, datos)

            print("Los datos se han insertado correctamente")
            select = "SELECT nombre, pais, poblacion_millones FROM ciudades WHERE poblacion_millones < 10"

            cursor.execute(select)
            resultados =cursor.fetchall()
            print("Se eliminaran las siguientes ciudades: ")
            for fila in resultados:
                ciudad, pais, poblacion = fila
                print(f"Ciudad: {ciudad}, Pais:{pais}, Poblacion:{poblacion}")
            
            delete = "DELETE FROM ciudades WHERE poblacion_millones < 10"

            cursor.execute(delete)
            conexion.commit()





        except Error as e:
            # Si hay un error en insert o delete, deshacer cambios
            if 'conexion' in locals() and conexion.is_connected():
                conexion.rollback()
                print("Se produjo un error, se realizó rollback de la transacción.")
            print(f"Error de MySQL: {e}")

except Error as e:
    
    print(f"No se pudo conectar a la base de datos: {e}")
finally:
    # Cerrar la conexión si existe
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")