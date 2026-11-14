# Operadores aritméticos

a = 10
b = 3

suma = a + b
print(f"La suma de {a} y {b} es igual a {suma}")

resta = a - b
print(f"La resta de {a} y {b} es igual a {resta}")

producto = a * b
print(f"El producto de {a} y {b} es igual a {producto}")

division = a / b
print(f"El cociente de {a} y {b} es igual a {division}")

modulo = a // b
print(f"El cociente entero de {a} y {b} es igual a {modulo}")

residuo = a % b
print(f"El residuo de la division entre {a} y {b} es igual a {residuo}")

potencia = a ** b
print(f"{a} elevado a la {b} es igual a {potencia}")

# presedencia de operadores

resultado = a + b * 2
print(f"El resultado de la operación es: {resultado}")

resultado_2 = (a + b) * 2
print(resultado_2)
resultado_3 = 10 * 3 // 3
print(resultado_3)

resultado_4 = ((a+b)*(a-b) / (a*b)) - ((a**b)%3)
print(resultado_4)

#librerías en Python

import math

print(math.pi)
print(math.e)
print(math.sqrt(16))

import random
print(random.random())