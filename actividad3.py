weight = float(input("Ingrese su peso corporal en Kg: "))
height = float(input())
imc = 0
peso = ""

if weight < 0 or height < 0:
    print("Ingrese un valor positivo")
else: 
    imc = weight / (height ** 2)
    imc= round(imc, 2)

    if imc >= 30 :
        peso = "obesidad"
    elif imc > 25 and imc < 29.9 :
        peso = "sobrepeso"
    elif imc > 18.5 and imc < 24.9 :
        peso = "un peso normal"
    else :
        peso = "un peso bajo"

    print(f"Su índice de masa corporal es de {imc}. Tiene {peso}")