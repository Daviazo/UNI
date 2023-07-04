candidatos = {'A': 'rojo',
    'B': 'verde',
    'C': 'azul'}
opcion = input("Elige un candidato (A, B o C): ").upper()
if opcion in candidatos:
    partido = candidatos[opcion]
    print("Usted ha votado por el partido", partido)
else:
    print("Opción errónea.")