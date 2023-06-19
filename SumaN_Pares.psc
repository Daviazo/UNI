Algoritmo SumaNumerosPares
    Definir SUM, NUM como Entero
    SUM <- 0
	
    Para NUM <- 1 Hasta 100 Con Paso 1 Hacer
        Si NUM % 2 = 0 Entonces
            SUM <- SUM + NUM
        FinSi
    FinPara
	
    Escribir "La suma de los números pares del 1 al 100 es:", SUM
FinAlgoritmo