# TUPLAS

tupla = ("Elemento 1" , "Elemento 2" , "Elemento 3")
print(type(tupla))

tupla2 = "a" , "b" , "c"
print(type(tupla2))

tupla3 = ("Hola" ,)
print(type(tupla3))

tupla4 = tuple("Hola")
print(type(tupla4))

tupla_mixta = ("Hola" , 123 , True , [1 , 2 , 3])
print(tupla_mixta)

aprendices = ("Dayana" , "John" , "Óscar" , "Luis" , "Pepito")
print(aprendices)

print(aprendices[2]) # Acceder a un elemento de la tupla

print(aprendices[0:3])

print(aprendices[0::2])

tupla_uno = (1, 2, 3)
tupla_dos = (4, 5, 6)
tupla_suma = tupla_uno + tupla_dos
print(tupla_suma)

tupla_multiplicada = tupla_uno * 3
print(tupla_multiplicada)

print(len(tupla_multiplicada))
print(tupla_multiplicada.count(2))
print(tupla_multiplicada.index(3))


lenguajes = ("Python" , "HTML" , "JavaScript" , "CSS")
lenguajes = list(lenguajes)
print(type(lenguajes))
print(lenguajes)

lenguajes.append("C++")
print(lenguajes)

lenguajes = tuple(lenguajes)
print(type(lenguajes))

print("Python" in lenguajes)
print("PHP" in lenguajes)

if "PHP" in lenguajes :
    print("PHP fue encontrado en la tupla")
else :
    print("PHP no fue encontrado en la tupla")


# Empaquetar tuplas

programa1 = "ADSO"
programa2 = "SST"
programa3 = "Topografía"
programas = (programa1 , programa2 , programa3)
print(type(programas))

# Desempaquetar tuplas

ciudades = ("Sogamoso" , "Duitama" , "Tunja")
ciudad1 , ciudad2, ciudad3 = ciudades
print(f"{ciudad1}\n{ciudad2}\n{ciudad3}")

for ciudad in ciudades :
    print(ciudad)