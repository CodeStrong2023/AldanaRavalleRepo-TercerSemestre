import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd',
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input('Ingrese un id_persona para buscarlo (separa por comas):  ')
            llaves_primarias = (tuple(entrada.split(',')),) # convertimos una tupla en tuplas
            cursor.execute(sentencia,llaves_primarias) # se ejecuta la sentencia
            registros = cursor.fetchall() # fechall/fechone para recuperar registros como lista
            for registro in registros: # iterar los registros para verlos como tupla
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()