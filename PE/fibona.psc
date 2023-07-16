Algoritmo SerieFibonacci
    Definir num, termino1, termino2, siguienteTermino como Entero
    Escribir "Ingrese el número de términos que desea generar:"
    Leer num
    Escribir "Los primeros ", num, " términos de la serie de Fibonacci son:"
    termino1 <- 0
    termino2 <- 1
    Escribir termino1
    Si num > 1 Entonces
        Escribir termino2
		
        Para i <- 3 Hasta num Con Paso 1 Hacer
            siguienteTermino <- termino1 + termino2
            Escribir siguienteTermino
            termino1 <- termino2
            termino2 <- siguienteTermino
        FinPara
    FinSi
FinAlgoritmo