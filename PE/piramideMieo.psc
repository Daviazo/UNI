Algoritmo GizZza
    Definir altura, i, j como Entero
    Escribir "Ingrese la altura de la pirámide:"
    Leer altura
    Para i <- 1 Hasta altura Con Paso 1 Hacer
        Para j <- 1 Hasta altura - i Con Paso 1 Hacer
            Escribir " "Sin Saltar
        FinPara
        Para j <- 1 Hasta 2 * i - 1 Con Paso 1 Hacer
            Escribir "*"Sin Saltar
        FinPara
        Escribir ""
    FinPara
FinAlgoritmo