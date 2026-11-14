nota1 = float(input("Ingrese la nota: "))
nota2 = float(input("Ingrese la nota: "))
nota3 = float(input("Ingrese la nota: "))
promedio = ((nota1 + nota2 + nota3) / 3)
promedio = round(promedio, 2)

if promedio < 5 :
    print(f"Te faltan {5 - promedio} puntos para obtener la nota máxima")
else :
    print("No te hacen falta puntos para la nota máxima")

if promedio >= 3 :
    print(f"Aprobaste. Tu promedio fue de {promedio}")
else :
    print(f"Reprobaste. Te hicieron falta {3 - promedio} puntos para aprobar")

