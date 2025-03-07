producto=int(input("ingrese el monto del producto "))
descuento=int()
resultado=int()
if(producto<=50):
    print(f"no tiene descuento, el total es =${producto}")
elif(producto>50 and producto <=100):
    descuento=producto*0.05
    resultado=producto-descuento
    print(f"el monto del descuento es {descuento}")
    print(f"el total a pagar {resultado}")
elif(producto>100):
    descuento=producto*0.10
    resultado=producto-descuento
    print(f"el monto del descuento es {descuento}")
    print(f"el total a pagar {resultado}")
    
    