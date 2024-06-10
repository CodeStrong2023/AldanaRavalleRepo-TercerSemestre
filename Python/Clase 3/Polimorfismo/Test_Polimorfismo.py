from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Ana', 500.000)
imprimir_detalles(empleado)

gerente = Gerente('Natalia', 600.000, 'Sistemas')
imprimir_detalles(gerente)