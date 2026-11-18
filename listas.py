# LISTAS

lista = ["dato_1" , "dato_2" , "dato_3"]
print(type(lista))

lista__mixta = ["Hola" , 123 , True , ["ADSO" , "SST"]]

aprendices = ["Miguel" , "Sebastian" , "Lizeth" , "Óscar" , "Elkin"]
print(aprendices[2])

aprendices[0] = "Luis"
print(aprendices)


# Consultar rangos de elementos en la lista

print(aprendices[0:2])
print(aprendices[2:4])
print(aprendices[0::2])


# Concatenar listas

programas_tecnicos = ["Sistemas teleinformáticos" , "Redes"]
programas_tecnologos = ["ADSO" , "SST" , "Topografía"]

programas_sena = programas_tecnicos + programas_tecnologos
print(programas_sena)


# Unir listas con .extend()

nuevos_programas_tecnicos = ["Inteligencia artificial" , "Minería de datos" , "Redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos)


# Medir la longitud con .len()

print(len(programas_tecnicos))
print(len(programas_tecnologos))

# Contar elementos repetidos en una lista con .count()
print(programas_tecnicos)
print(programas_tecnicos.count("Redes"))


# Buscar el índice por elementos

print(aprendices.index("Lizeth"))
print(programas_tecnicos.index("Minería de datos"))


# Copiar una lista con .copy()

nueva_lista_aprendices = aprendices.copy()
print(nueva_lista_aprendices)


# Agregar elementos .append()

nueva_lista_aprendices.append("Adriana")
nueva_lista_aprendices.append("Diana")
print(nueva_lista_aprendices)


# Agrega un elemento en una posición del índice .insert()

nueva_lista_aprendices.insert(1 , "Dayana")
print(nueva_lista_aprendices)


# Eliminar un elemento de la lista 
# .remove() Elimina la primera ocurrencia de la lista

nueva_lista_aprendices.remove("Óscar")
print(nueva_lista_aprendices)

# .pop() Elimina el elemento según su índice

nueva_lista_aprendices.pop(0)
print(nueva_lista_aprendices)


# .clear() Limpia TODOS los elementos de la lista

#nueva_lista_aprendices.clear()
#print(nueva_lista_aprendices)


# Ordenar la listas
# Ordenamiento ascendente A-Z .sort()

nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

# Ordenamiento descendente Z-A

nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)


# Buscar elementos de la lista con "IN"

if "Diana" in nueva_lista_aprendices :
    print(f"Diana se encontró en la lista de aprendices {nueva_lista_aprendices.index("Diana")}")
else :
    print("Diana no se encontró en la lista de aprendices")