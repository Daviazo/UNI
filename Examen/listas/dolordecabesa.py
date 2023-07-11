numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares = 0
suma_impares = 0
for indice, numero in enumerate(numeros):
    if indice % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print("Suma de elementos en índices pares:", suma_pares)
print("Suma de elementos en índices impares:", suma_impares)