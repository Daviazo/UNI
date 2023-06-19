Algoritmo Factorial
    Definir NUM, FACT como Entero
    FACT <- 1
	
    Escribir "Ingrese un número entero:"
    Leer NUM
	
    Para i <- 1 Hasta NUM Con Paso 1 Hacer
        FACT <- FACT * i
    FinPara
	
    Escribir "El factorial de ", NUM, " es: ", FACT
FinAlgoritmo 