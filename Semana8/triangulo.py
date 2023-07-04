def es_triangulo_rectangulo(a, b, c):
    lados = [a, b, c]
    lados.sort()
    return lados[0]**2 + lados[1]**2 == lados[2]**2
def es_triangulo_isosceles(a, b, c):
    return a == b or b == c or a == c
def es_triangulo_equilatero(a, b, c):
    return a == b == c
def determinar_tipo_triangulo(a, b, c):
    if es_triangulo_equilatero(a, b, c):
        return "equilátero"
    elif es_triangulo_isosceles(a, b, c):
        return "isósceles"
    elif es_triangulo_rectangulo(a, b, c):
        return "rectángulo"
    else:
        return "escaleno"
a = float(input("Ingrese el lado A del triángulo: "))
b = float(input("Ingrese el lado B del triángulo: "))
c = float(input("Ingrese el lado C del triángulo: "))
tipo_triangulo = determinar_tipo_triangulo(a, b, c)
print("El triángulo es", tipo_triangulo)
