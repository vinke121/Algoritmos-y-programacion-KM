print("ejercicio 4")
piezas=int(input("ingrese el numero de piesas: "))
r=int(piezas*50000)
print(f"el valor total de la compra es: {r} COP")
if (r>=5000000):
    empresa=r*0.55
    banco=r*0.30
    credito=r*0.15
    interes=credito*0.20
    print(f"la empresa tendra que invertir: {empresa} COP")
    print(f"el banco le presta: {banco} COP")
    print(f"el valor del credito del fabricante: {credito} COP, y el interes a pagar es: {interes}COP")

elif(r < 5000000):
    empresa=r*0.70
    banco=r*0.30
    print(f"la empresa tendra que invertir: {empresa} COP")
    print(f"el banco le presta: {banco} COP")