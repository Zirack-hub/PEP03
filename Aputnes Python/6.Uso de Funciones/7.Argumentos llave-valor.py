# El signo "**kwargs" se usa para decir que puedes meter todos los valores que quieras en forma de diccionario
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')