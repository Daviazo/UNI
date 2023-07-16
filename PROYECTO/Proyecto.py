print('bienvenido a nuestro sistema'.center(60,' '))
usuarios = {'David' : 'proyecto'}
print('(1)iniciar sesion '.center(60,'-'))
print('(2)Registrar nuevo usuario'.center(60,'-'))
print('(3)Salir'.center(60,'-'))
Menu1= (input('inrgese su opcion a elejir: '))

if Menu1 == '2' :

    nuevouser =str(input('ingrese su nombre de usuario: '))
    nuevacontr = str(input('inrese la contra: '))
    if nuevouser in usuarios:

        print('ERROR ya existe ese usuario por favor inicie sesion')

    else:

        usuarios[ nuevouser ] = nuevacontr
        print('Creado con exito.')

elif Menu1 == '1':

    nuevouser =str(input('ingrese su nombre de usuario: '))
    nuevacontr = str(input('inrese la contra: '))
    if nuevouser in usuarios and usuarios[nuevouser] == nuevacontr:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")  

elif Menu1 == '3':

    print('hasta luego'.center(60,'-'))

else:

    print("seleccione una opcion correcta")
