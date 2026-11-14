# IF

if True: 
    print("Se ejecuta la instrucción")

# ELSE

age = 12

if age > 18:
    print("Eres un adulto")
else :
    print("Eres joven")

# ELIF

if False:
    print("Primera condición")
elif True:
    print("Segunda condición")
else :
    print("Todas las condiciones son falsas")

if age < 18 :
    print("Eres menor de dad")
elif age >= 18 and age < 65: 
    print("Eres un adulto")
else :
    print("Eres un vejete")

# Estructura condicional anidada

if True:
    if False:
        print("Se ejectua la instrucción")
    elif True:
        print("Se ejecuta la instrucción")
    else:
        print("No se ejecuta la instrucción")
else:
    print("No se ejecuta la instrucción")

# Ejercicio 

if age < 18 :
    if age > 12 and age < 18:
        print("Eres un adolescente")
    else :
        print("Eres un niño")
else:
    if age >= 18 and age < 65 :
        print("Eres un adulto")
    else :
        print("Eres un adulto mayor")


# Ejercicio partido con IF

marcador_Colombia = int(input("Ingrese el marcador de Colombia: "))
marcador_Chile = int(input("Ingrese el marcador de Chile: "))

if marcador_Colombia > marcador_Chile :
    print("Ganó Colombia")
elif marcador_Colombia == marcador_Chile :
    print("Quedó en empate")
else :
    print("Ganó Chile")

# Operador ternario

numero = 4

if numero % 2 == 0:
    print("Es un número par")
else :
    print("El número es impar")

print("El número es par" if numero % 2 == 0 else "El número es impar")