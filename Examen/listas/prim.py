def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_primos = [numero for numero in numeros if es_primo(numero)]
print(numeros_primos)