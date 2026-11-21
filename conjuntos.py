# CONJUNTOS

conjunto = {"Elemento1" , "Elemento2"}
print(type(conjunto))

conjunto2 = set()
print(type(conjunto2))

conjunto3 = {}
print(type(conjunto3))

programas = {"ADSO" , "SST" , "Minería" , "ADSO" , "SST"}
print(len(programas))


# Metodos

frutas = {"mango" , "guayaba" , "mora"}
frutas.add("sandia")
print(frutas)
frutas.add("mora")
print(frutas)

frutas.remove("mango")
print(frutas)

frutas.discard("mora")
print(frutas)

frutas.add("manzana")
frutas.add("mandarina")

frutas.pop()
print(frutas)

# frutas.clear()
# print(frutas)

del frutas


# Verificar la pertenencia de un elemento en un conjunto

aprendices = {"Felipe" , "Andrés" , "Pepito"}

print("Felipe" in aprendices)
print("Juan" in aprendices)


# Operaciones de la teoría de conjuntos

aprendices_formacion = {"Jennifer" , "Lizeth" , "Diana" , "Alejandra" , "Adriana"}
aprendices_apoyo = {"Diana" , "Adriana" , "Luis" , "Sebastian" , "Óscar"}

union_aprendices = aprendices_formacion | aprendices_apoyo
print(union_aprendices)

union_aprendices2 = aprendices_formacion.union(aprendices_apoyo)
print(union_aprendices2)

interseccion_aprendices = aprendices_formacion & aprendices_apoyo
print(interseccion_aprendices)

interseccion_aprendices2 = aprendices_formacion.intersection(aprendices_apoyo)
print(interseccion_aprendices2)

diferencia_aprendices = aprendices_formacion - aprendices_apoyo
print(diferencia_aprendices)

diferencia_aprendices2 = aprendices_formacion.difference(aprendices_apoyo)
print(diferencia_aprendices2)

simetrica_aprendices = aprendices_formacion.symmetric_difference(aprendices_apoyo)
print(simetrica_aprendices)