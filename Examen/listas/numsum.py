lista_numeros = []
for i in range(1, 11):
    lista_numeros.append(i)
lista_resultado = [numero * 2 for numero in lista_numeros]
for numero in lista_resultado:
    print(numero)