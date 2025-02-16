print("ejercicio_8_area_triangulo")
a=float(input("ingrese la longitud del triangulo: "))
b=float(input("ingrese la longitud del triangulo: "))
c=float(input("ingrese la longitud del triangulo: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("El area del triangulo es: ", area)