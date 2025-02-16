print("ejercicio_4_descuento_de_la_tienda")
producto1=float(input("ingrese el valor del primer producto: "))
producto2=float(input("ingrese el valor del segundo producto: "))
producto3=float(input("ingrese el valor del tercer producto: "))
descuento= 0.15*(producto1+producto2+producto3)
total=(producto1+producto2+producto3)-descuento
print("Descuento total de su compra",descuento, "pesos") 
print("Total a pagar",total, "pesos")