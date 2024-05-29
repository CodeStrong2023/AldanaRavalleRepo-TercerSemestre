from numerosIgualesException import NumerosIgualesException

resultado = None

try:
    a = int(input('Ingrese el primer número: '))
    b = int(input('Ingrese el segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son numeros iguales')
    resultado = a / b

except TypeError as e:
    print(f'TypeError | Ocurrio un error: {type(e)}')

except ZeroDivisionError as e:
    print(f'ZeroDivisionError | Ocurrio un error: {type(e)}')

except Exception as e:  # ZeroDivisionError
    print(f'Exception | Ocurrio un error: {type(e)}')

else:
    print('No se arrojo ninguna excepcion')

finally: # siempre se va a ejecutar
    print('Ejecucion de este bloque finally')

print(f'El resultado es: {resultado}')
print('sigamos...')