cantidad = float(input("Ingresa la cantidad a invertir: "))
tasa_interes = float(input("Ingresa la tasa de interés anual (%): "))
anios = int(input("Ingresa el número de años de la inversión: "))
capital = cantidad * (1 + tasa_interes / 100) ** anios
print("El capital obtenido en la inversión es:", capital)
