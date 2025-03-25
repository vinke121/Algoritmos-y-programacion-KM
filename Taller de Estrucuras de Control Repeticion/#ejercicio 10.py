#ejercicio 10
numero=int(input("ingrese un numero positivo: "))
suma=0

for i in range(1, numero):
    if (numero % i == 0):
        suma = suma+i
if (suma == numero):
    print(f"{numero} es un numero perfecto")
else:
    print(f"{numero} no es un numero perfecto")
        