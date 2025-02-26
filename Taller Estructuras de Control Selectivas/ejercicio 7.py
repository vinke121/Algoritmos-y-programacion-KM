print("ejercicio 7")

km=float(input("ingrese la distancia de kilometros: "))

if(km<=300):
    print("el total a pagar es 50.000 COP")
elif(300 < km <=1000):
    cancela=(70000+30000*(km-300))
    print(f"el total a pagar es: {cancela} COP")
elif(km>1000):
    cancela=(150000+9000*(km-1000))
    print(f"el total a pagar es: {cancela} COP")