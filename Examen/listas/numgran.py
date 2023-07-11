numeros = [10, 5, 8, 20, 15, 12]
numero_mas_grande = float('-inf')
segundo_numero_mas_grande = float('-inf')
for numero in numeros:
    if numero > numero_mas_grande:
        numero_mas_grande = numero
for numero in numeros:
    if numero > segundo_numero_mas_grande and numero < numero_mas_grande:
        segundo_numero_mas_grande = numero
print(segundo_numero_mas_grande)