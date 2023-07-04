def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
print("----- Menú -----")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta de los dos números")
print("3. Mostrar la multiplicación de los dos números")
opcion = input("Seleccione una opción: ")
if opcion == "1":
    resultado = suma(numero1, numero2)
    print("La suma de", numero1, "y", numero2, "es:", resultado)
elif opcion == "2":
    resultado = resta(numero1, numero2)
    print("La resta de", numero1, "y", numero2, "es:", resultado)
elif opcion == "3":
    resultado = multiplicacion(numero1, numero2)
    print("La multiplicación de", numero1, "y", numero2, "es:", resultado)
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")