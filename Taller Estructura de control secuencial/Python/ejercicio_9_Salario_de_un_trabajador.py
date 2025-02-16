print("Ejercicio_9_Salario_de_un_trabajador")
valor_hora=float(input("ingrese el valor de la hora del trabajador: "))
horas=float(input("ingrese las horas trabajadas: "))
sueldo_sinD=valor_hora*horas
impuestos=sueldo_sinD*0.20
sueldo_conD=sueldo_sinD-impuestos
print("El sueldo sin descuentos es: ",sueldo_sinD)
print("El valor de los impuestos es: ",impuestos)
print("El sueldo con descuentos es: ",sueldo_conD)