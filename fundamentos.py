print("Hola mundo")

# Tipo de escritura de las variables
aprendizSena = "Juan"

AprendizSena = "Jorge"

aprendiz_sena = "Felipe"

# tipos de datos Primitivos
name = "Juan Manrique"
print(type(name))
age = 21
print(type(age))
height = 1.75
print(type(height))
activo = True
print(type(activo))
print(type(name)==int)

lista = ["Python" , "JavaScript" , "PHP"]
print(type(lista))

conjunto = {"HTML" , "CSS"}
print(type(conjunto))

byte = b"Hola"
print(type(byte))

complejo = 2 + 3j
print(type(complejo))

nulo = None
print(type(nulo))

# tipos de datos Estructuras

lista = ["HTML", "CSS", "JavaScript"]
print(type(lista))

conjunto = {"Python", "PHP"}
print(type(conjunto))

tupla = ("Java" , "C#")
print(type(tupla))

diccionario = {"nombre":"Juan" , "apellido" : "Manrique" , "edad" : 21}
print(type(diccionario))

rango = range(5)
print(type(rango))

# conversión de tipos de datos o castear

telefono = 3208642230
telefono_str = str(telefono)
print(type(telefono))
print(type(telefono_str))

cedula = "1051956345"
cedula_int = int(cedula)
print(type(cedula), cedula)
print(type(cedula_int), cedula_int)

matriculado = True
print(type(matriculado))
matriculado_int = int(matriculado)
print(type(matriculado_int), matriculado_int)
matriculado_float = float(matriculado)
print(matriculado_float)

promedio = 4.9
print(type(promedio), promedio)
promedio_int = int(promedio)
print(type(promedio_int) , promedio_int)
promedio_bool = bool(promedio)
print(promedio_bool)

edad = 21
print(type(edad) , edad)
edad_float = float(edad)
print(type(edad_float), edad_float)

activo = 0
activo_bool = bool(activo)
print(type(activo_bool) , activo_bool)

texto = "Ejemplo de texto a entero"
texto_int = bool(texto)
print(texto_int)

""" Este es un comentario
de varias lineas
de codigo en bloque"""

# condicional if

if 5 > 2 :
    print("5 es mayor que 2")
else :
    print("5 no es mayor que 2")

name = input("Nombre completo: ")
print("Tu nombre es", name)
programa = input("Cuál es tu programa de formación")
print("Hola,",name," del programa de",programa)
print(f"Hola, mi nombre es {name} y soy del programa {programa}")