from ManejoArchivos import ManejoArchivos

# manejo de contexto with - sintaxis simplificada
'''
with open('prueba.txt','r',encoding='utf8') as archivo:
    print(archivo.read())
'''

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())