import mysql.connector
from mysql.connector import Error

try:
    # Intentar conectarse a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        database="PLANETAS",
        user="PLANETAS",
        password="PLANETAS"
    )

    if conexion.is_connected():
        cursor = conexion.cursor()
        print("Conexión establecida correctamente")

        crearTabla = """
        CREATE TABLE planetas(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        tipo VARCHAR (50),
        lunas INT
        );"""
        cursor.execute(crearTabla)
        datos = [
        ("Tierra", "Planeta Azul", 1),
        ("Marte", "Planeta Rojo ", 2),
        ]
        
        
        insert = "INSERT INTO planetas (nombre, tipo, lunas) VALUES (%s, %s, %s)"

    
        cursor.executemany(insert, datos)
        conexion.commit()

        print(f"Se han insertado {cursor.rowcount} filas correctamente")

        select = "SELECT id, nombre, tipo, lunas FROM planetas WHERE id = 1"

        cursor.execute(select)
        resultados =cursor.fetchall()

        for fila in resultados:
            id,nombre, tipo, lunas = fila
            print(f"El planeta: {nombre}, del tipo:{tipo}, con :{lunas} lunas, tiene la id: {id}")
    
    


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