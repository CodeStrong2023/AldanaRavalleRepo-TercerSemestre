from Orden import Orden
from Producto import Producto

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)

producto3 = Producto('Campera', 300.00)
producto4 = Producto('Botas', 250.00)

producto5 = Producto('Medias', 200.00)
producto6 = Producto('Blusa', 350.00)


productos1 = [producto1, producto2]  # lista de productos
orden1 = Orden(productos1)
orden1.agregar_producto(producto5)
orden1.agregar_producto(producto6)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')


productos2 = [producto3, producto4]  # lista de productos
orden2 = Orden(productos2)
orden2.agregar_producto(producto5)
orden2.agregar_producto(producto6)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')
