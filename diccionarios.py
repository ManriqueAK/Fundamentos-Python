# DICCIONARIOS

# Estructura

dictionary = {
    "key1" : "value1" ,
    "key2" : "value2" , 
    "key3" : "value3"
}

diccionario_aprendiz = {
    "name" : "Juan" ,
    "last_name" : "Manrique" ,
    "programa" : "ADSO" , 
    "ficha" : "3233140" , 
    "age" : 21 ,
}
print(diccionario_aprendiz)

print(diccionario_aprendiz["name"])

print(diccionario_aprendiz.get("programa"))
print(diccionario_aprendiz.get("correo"))

print(diccionario_aprendiz.keys())
print(diccionario_aprendiz.values())

print(diccionario_aprendiz.items())



# Agregar un nuevo elemento al diccionario

diccionario_aprendiz["correo"] = "manriqueak25@gmail.com"
print(diccionario_aprendiz.keys())

diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz.items())

diccionario_aprendiz.update({"name" : "Sebastian"})
print(diccionario_aprendiz.items())

diccionario_aprendiz.update({"ciudad" : "Duitama"})
print(diccionario_aprendiz.items())

diccionario_aprendiz.popitem()
print(diccionario_aprendiz.items())

diccionario_aprendiz.pop("correo")
print(diccionario_aprendiz.items())

# Eliminar todos los elementos del diccionario


# diccionario_aprendiz.clear()

print("ficha" in diccionario_aprendiz)
print("ciudad" in diccionario_aprendiz )

if "ficha" in diccionario_aprendiz :
    print("La clave ficha está dentro del diccionario")
else :
    print("La clave ficha no está dentro del diccionario")


# 1. Recorrer solo las claves del diccionario

for key in diccionario_aprendiz.keys() :
    print(key)

# 2. Recorrer los valores del diccionario

for value in diccionario_aprendiz.values() :
    print(value)

# 3. Recorrer las claves y valores del diccionario

for key, value in diccionario_aprendiz.items() :
    print(f"{key} : {value}")



# Diccionarios anidados

aprendices = {
    "aprendiz1" : {
        "name" : "Juan" ,
        "last_name" : "Manrique" ,
        "programa" : "ADSO"
    } ,
    "aprendiz2" : {
        "name" : "Felipe" ,
        "last_name" : "Sandoval" ,
        "programa" : "ADSO"
    } ,
    "aprendiz3" : {
        "name" : "Carlos" ,
        "last_name" : "Martinez" ,
        "programa" : "Minas"
    }
}

print(aprendices["aprendiz2"]["programa"])

for aprendiz, datos in aprendices.items() :
    print(f"{aprendiz} : ")
    for clave, valor in datos.items() :
        print(f"{clave} : {valor}")