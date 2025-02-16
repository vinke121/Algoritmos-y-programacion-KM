print("Ejercicio_11_sueldo_neto_del_trabajador")
trabajador=str(input("ingrese el nombre del trabajador:"))
horas_laboradas=int(input("ingrese las horas laboradas:"))
valor_hora=int(input("ingrese el valor de la hora:"))
horas_extra=int(input("ingrese las horas extras:"))
valor_hora_extra= (valor_hora*0.25)+valor_hora
sueldo_base=(horas_laboradas*valor_hora)+valor_hora_extra
#asignaciones
actualizacion_academica=250000
hijos=int(input("ingrese el numero de hijos:"))
total_hijos=hijos*173000
prima_hogar=180000
asignaciones=actualizacion_academica+total_hijos+prima_hogar
#descuentos #5% pago forzoso, 2% politica habitacional, 7% caja de ahorro
descuentos= (sueldo_base*0.05)-(sueldo_base*0.02)-(sueldo_base*0.07)+sueldo_base
#total
sueldo_neto=sueldo_base+asignaciones-descuentos
print("valor hora extra:",valor_hora_extra, "COP")
print("sueldo base:",sueldo_base, "COP")
print("asignaciones:",asignaciones, "COP")
print("sueldo total con descuentos:",descuentos, "COP")
print("sueldo neto:",sueldo_neto, "COP")