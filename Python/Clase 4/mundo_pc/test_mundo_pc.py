from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
from orden import Orden

teclado1 = Teclado('HP', '15 USB')
monitor1 = Monitor('HP', '15 Pulgadas')
raton1 = Raton('HP', '27 USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', '27 Pulgadas')
raton2 = Raton('Acer', 'Blurtooth')
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

teclado3 = Teclado('HP', '15 USB')
monitor3 = Monitor('HP', '15 Pulgadas')
raton3 = Raton('HP', '27 USB')
computadora3 = Computadora('HP', monitor3, teclado3, raton3)

teclado4 = Teclado('Acer', 'Bluetooth')
monitor4 = Monitor('Acer', '27 Pulgadas')
raton4 = Raton('Acer', 'Blurtooth')
computadora4 = Computadora('HP', monitor4, teclado4, raton4)

computadora5 = Computadora('Samsung', monitor1, teclado2, raton1)
computadora6 = Computadora('Gamer', monitor3, teclado1, raton3)


computadoras1 = [computadora1, computadora2, computadora5]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora5)
print(orden1)


computadoras2 = [computadora3, computadora4, computadora6]
orden2 = Orden(computadoras2)
print(orden2)