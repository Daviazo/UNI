Algoritmo ParesEImpares
    Definir INICIO, FINAL como Entero
    Escribir "Ingrese el n�mero de inicio del rango:"
    Leer INICIO
    Escribir "Ingrese el n�mero final del rango:"
    Leer FINAL
    Escribir "N�meros pares en el rango de ", INICIO, " a ", FINAL, ": "
    Para i <- INICIO Hasta FINAL Con Paso 1 Hacer
        Si i % 2 = 0 Entonces
            Escribir i
        FinSi
    FinPara
    Escribir "N�meros impares en el rango de ", INICIO, " a ", FINAL, ": "
    Para i <- INICIO Hasta FINAL Con Paso 1 Hacer
        Si i % 2 <> 0 Entonces
            Escribir i
        FinSi
    FinPara
FinAlgoritmo