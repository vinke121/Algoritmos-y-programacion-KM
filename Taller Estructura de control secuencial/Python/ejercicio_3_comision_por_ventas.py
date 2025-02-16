print("ejercicio_3_comision_por_ventas")
sueldo=int(input("sueldo base del vendedor:"))
venta1=int(input("venta numero 1: "))
venta2=int(input("venta numero 2: "))
venta3=int(input("venta numero 3: "))
comision=0.10*(venta1+venta2+venta3)
total=comision+sueldo
print("la comision total es: ", comision)
print("el total generado por las ventas es: ",total)