
archivo = open('prueba.txt', 'r', encoding='utf8')
#print(archivo.read())
#print(archivo.read(16)) # muestra letras
#print(archivo.readline())# muestra lineas indicadas

# iterar el archivo
'''
for linea in archivo:
    print(linea) #itera todos los elementos del archivo
'''

# print(archivo.readlines()[3]) #accedemos a el archivo como lista

# Anexar informacion
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el segundo archivo
print('Se ha terminado el proceso de leer y copiar archivos')