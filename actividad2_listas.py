temperaturas = [18 , 21 , 19 , 24 , 22 , 20 , 17 , 23 , 25 , 21 , 18 , 20 , 22 , 19]
print(f"Temperatura Día 1: {temperaturas[0]}°C\nTemperatura Día 7: {temperaturas[6]}°C\nTemperatura Día 13: {temperaturas[-2]}°C\nTemperatura Día 14: {temperaturas[-1]}°C")
print(f"1 semana: {temperaturas[0:7]}\n2 semana: {temperaturas[7:14]}\nDías pares: {temperaturas[1::2]}\nOrden invertido:")

primera_semana = round(sum(temperaturas[0:7])/7 , 2)
print(primera_semana)