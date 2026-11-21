i = 0
while i < 5 :
    print("Hola mundo")
    i += 1

edad = int(input("Ingrese su edad: "))

while edad < 18 :
    print(f"Eres menor de edad. Tienes {edad} años")
    edad += 1
else: 
    print("Eres mayor de edad")