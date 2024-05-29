
# Declaramos una variable
try:
    archivo = open('prueba.txt','w', encoding='utf8') # La w significa write
    archivo.write('Programamos con diferentes tipos de archivos, ahora de txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como, por ejemplo: acción, ejecucion y produccion\n')
    archivo.write('Las letras son: \nr read leer, \na append anexar, \nw write escribe, \nx crea un archive')
    archivo.write('\nt esta es para texto o text, \nn es para archivos binarios, \nw+ y r+ leen y escriben\n')
    archivo.write('Saludos\n')
    archivo.write('Con esto terminamos.')
except Exception as e:
    print(e)
finally: # Siempre se ejecuta
    archivo.close() # Cerramos el archivo
# archivo.write('Todo quedo perfecto') -> Este es un error, no se puede modificar un archivo luego de cerrarlo