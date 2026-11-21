# Sentencia match 

# Match días de la semana


dia = int(input("Ingrese el número del día de la semana: "))
match dia :
    case 1 :
        print("Lunes")
    case 2 :
        print("Martes")
    case 3 :
        print("Miércoles")
    case 4 :
        print("Jueves")
    case 5 :
        print("Viernes")
    case 6 :
        print("Sábado")
    case 7 :
        print("Domingo")
    case _ :
        print("Día incorrecto")


# Ejercicio: Faltas aprendiz SENA

falta = (input("Ingrese la falta del aprendíz: ")).lower()

match falta :
    case "comer" :
        print("Llamado de atención por comer en formación")
    case "impuntualidad" :
        print("Llamado de atención por llegar tarde")
    case "uniforme" :
        print("Llamado de atención por no portar el uniforme")
    case "jugar" :
        print("Llamado de atención por jugar en la formación")
    case _ :
        print("Aprendiz sin faltas")