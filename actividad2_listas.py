temperaturas = [18 , 21 , 19 , 24 , 22 , 20 , 17 , 23 , 25 , 21 , 18 , 20 , 22 , 19]
invertida = temperaturas.copy()
invertida.reverse()
print(f"Temperatura Día 1: {temperaturas[0]} °C\nTemperatura Día 7: {temperaturas[6]} °C\nTemperatura Día 13: {temperaturas[-2]} °C\nTemperatura Día 14: {temperaturas[-1]} °C")
print(f"1 semana: {temperaturas[0:7]}\n2 semana: {temperaturas[7:14]}\nDías pares: {temperaturas[1::2]}\nOrden invertido: {invertida}")

primera_semana = round(sum(temperaturas[0:7])/7 , 2)
segunda_semana = round(sum(temperaturas[7:14])/7 , 2)
print(f"Promedio temperatura semana 1: {primera_semana} °C\nPromedio temperatura semana 2: {segunda_semana} °C")

if primera_semana > segunda_semana :
    print("La primera semana tuvo mayor temperatura promedio")
else: 
    print("La segunda semana tuvo mayor temperatura promedio")