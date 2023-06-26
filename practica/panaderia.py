precio_regular = 3000
num_barras_no_frescas = int(input("Ingresa el número de barras vendidas que no son frescas: "))
descuento = 0.6 * precio_regular 
costo_total = (precio_regular - descuento) * num_barras_no_frescas
print("Precio regular de una barra de pan:", precio_regular)
print("Descuento por no ser fresca:", descuento)
print("Costo total final:", costo_total)
