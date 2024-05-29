from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as catalogo

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar las peliculas')
        print('3. Eliminar catálogo de peliculas')
        print('4. Salir')
        opcion = int(input('Digite una opción de menú (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_peliculas(pelicula)
        elif opcion == 2:
            catalogo.listar_peliculas()
        elif opcion == 3:
            catalogo.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')
