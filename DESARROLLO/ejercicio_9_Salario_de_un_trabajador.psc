Algoritmo Ejercicio_9_Salario_de_un_trabajador
	Escribir "valor de la hora del trabajador"
	Leer valor_hora
	Escribir "horas trabajadas"
	Leer horas
	sueldo_sinD = valor_hora * horas
	impuesto = sueldo_sinD * 0.20
	sueldo_conD = sueldo_sinD - impuesto
	Escribir "sueldo sin descuento ", sueldo_sinD
	Escribir "descuento de impuestos ", impuesto
	Escribir "sueldo con descuento ", sueldo_conD
FinAlgoritmo
