usuarios = []
contrasenas = []
saldos = []
intentos = 3

def agregar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    usuarios.append(usuario.lower())
    contrasenas.append(contrasena)
    saldos.append(0)
def validar_usuario():
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuario = usuario.lower()
    if usuario in usuarios and contrasena == contrasenas[usuarios.index(usuario)]:
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False
def depositar():
    usuario = input("Ingrese su usuario: ")
    monto = input("Ingrese el monto a depositar: ")
    usuario = usuario.lower()
    if usuario in usuarios:
        saldo_index = usuarios.index(usuario)
        saldo_actual = saldos[saldo_index]
        nuevo_saldo = saldo_actual + float(monto)
        saldos[saldo_index] = nuevo_saldo
        print("Se ha depositado", monto, "colones en su cuenta.")
        print("Saldo actual:", nuevo_saldo, "colones.")
    else:
        print("Usuario no encontrado.")
def retirar():
    usuario = input("Ingrese su usuario: ")
    monto = input("Ingrese el monto a retirar: ")
    usuario = usuario.lower()
    if usuario in usuarios:
        saldo_index = usuarios.index(usuario)
        saldo_actual = saldos[saldo_index]
        if saldo_actual >= int(monto) and int(monto) % 1000 == 0:
            nuevo_saldo = saldo_actual - int(monto)
            saldos[saldo_index] = nuevo_saldo
            print("Se han retirado", monto, "colones de su cuenta.")
            print("Saldo actual:", nuevo_saldo, "colones.")
        else:
            if saldo_actual < int(monto):
                print("No tiene suficiente saldo en su cuenta.")
            else:
                print("El monto a retirar debe ser múltiplo de 1000.")
    else:
        print("Usuario no encontrado.")
def ver_saldo():
    usuario = input("Ingrese su usuario: ")
    usuario = usuario.lower()
    if usuario in usuarios:
        saldo_index = usuarios.index(usuario)
        saldo_actual = saldos[saldo_index]
        print("Saldo actual:", saldo_actual, "colones.")
    else:
        print("Usuario no encontrado.")
def mostrar_menu():
    print("----- Menú -----")
    print("1. Depositar dinero a la cuenta")
    print("2. Sacar dinero de la cuenta")
    print("3. Ver saldo")
    print("4. Salir")
agregar_usuario()
while True:
    if validar_usuario():
        break
    else:
        intentos -= 1
        print("Intentos restantes:", intentos)
        if intentos == 0:
            print("Se han realizado 3 intentos incorrectos. El sistema se bloqueará.")
            exit()
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        depositar()
    elif opcion == "2":
        retirar()
    elif opcion == "3":
        ver_saldo()
    elif opcion == "4":
        print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")