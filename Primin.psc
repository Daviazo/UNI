Algoritmo NumerosPrimos
    Definir num, i, conta como Entero
    conta <- 0
    Escribir "Ingrese un n�mero entero:"
    Leer num
    Para i <- 1 Hasta num Con Paso 1 Hacer
        Si num % i = 0 Entonces
            conta <- conta + 1
        FinSi
    FinPara
    Si conta = 2 Entonces
        Escribir num, " es un n�mero primo."
    Sino
        Escribir num, " no es un n�mero primo."
    FinSi
FinAlgoritmo