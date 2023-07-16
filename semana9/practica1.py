lista = [20,65,12,2,8,65,48,1,5,8]
pares = []
impares = []
for num in lista:
    if num % 2 == 0:
     pares.append(num)
    else:
     impares.append(num)
print(pares, impares)