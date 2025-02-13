Algoritmo Ejercicio_11_sueldo_neto_del_trabajador
	Escribir "nombre del trabajador"
	Leer trabajador
	Escribir "numero de horas laboradas"
	Leer horas_laborales
	Escribir "valor por hora laboral"
	Leer valor_hora
	Escribir "horas extra trabajadas"
	Leer horas_extra
	actualizacion_academica = 250000	
	Escribir "cuantos hijos tiene el trabajador"
	Leer hijos
	total_hijos = hijos * 173000
	prima_hogar = 180000
	valor_hora_extra = (valor_hora * 0.25) + (valor_hora) 
	sueldo_base = (horas_laborales * valor_hora + valor_hora_extra)
	descuentos = (sueldo_base * 0.05 ) - (sueldo_base * 0.02) - (sueldo_base * 0.07) + sueldo_base
	asignaciones = total_hijos + valor_hora_extra + prima_hogar + actualizacion_academica
	sueldo_neto = descuentos + total_hijos + prima_hogar + actualizacion_academica
	Escribir "valor de horas extra " valor_hora_extra " COP"
	Escribir "sueldo total base " sueldo_base " COP"
	Escribir "sueldo total con descuentos " descuentos " COP"
	Escribir "adicional hijos " total_hijos " COP"
	Escribir "asignaciones "  asignaciones
	Escribir "sueldo neto" sueldo_neto	
FinAlgoritmo
