num_payasos = int(input("Ingresa el número de payasos vendidos: "))
num_munecas = int(input("Ingresa el número de muñecas vendidas: "))
peso_payasos = num_payasos * 112  
peso_munecas = num_munecas * 75  
peso_total = peso_payasos + peso_munecas
print("El peso total del paquete a enviar es:", peso_total, "g")
