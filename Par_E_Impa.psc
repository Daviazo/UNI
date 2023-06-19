Algoritmo ParesEImpares
    Definir INICIO, FINAL como Entero
    Escribir "Ingrese el número de inicio del rango:"
    Leer INICIO
    Escribir "Ingrese el número final del rango:"
    Leer FINAL
    Escribir "Números pares en el rango de ", INICIO, " a ", FINAL, ": "
    Para i <- INICIO Hasta FINAL Con Paso 1 Hacer
        Si i % 2 = 0 Entonces
            Escribir i
        FinSi
    FinPara
    Escribir "Números impares en el rango de ", INICIO, " a ", FINAL, ": "
    Para i <- INICIO Hasta FINAL Con Paso 1 Hacer
        Si i % 2 <> 0 Entonces
            Escribir i
        FinSi
    FinPara
FinAlgoritmo