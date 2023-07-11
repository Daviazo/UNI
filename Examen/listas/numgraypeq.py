numeros = [15, 27, 8, 12, 35, 20]
numero_mas_grande = numeros[0]
numero_mas_pequeno = numeros[0]
for numero in numeros:
    if numero > numero_mas_grande:
        numero_mas_grande = numero
    if numero < numero_mas_pequeno:
        numero_mas_pequeno = numero
print("El número más grande es:", numero_mas_grande)
print("El número más pequeño es:", numero_mas_pequeno)