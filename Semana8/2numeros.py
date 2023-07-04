def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
def comparar_numeros(num1, num2):
    if num1 == num2:
        print(" Los dos números son iguales.")
    else:
        print(" Los dos números son diferentes.")

        if num1 > num2:
            print(" El primer número es mayor que el segundo.")
        else:
            print(" El segundo número es mayor o igual que el primero.")
numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")
if es_numero(numero1) and es_numero(numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)
    comparar_numeros(numero1, numero2)
else:
    print(" Al menos uno de los valores ingresados no es un número.")
