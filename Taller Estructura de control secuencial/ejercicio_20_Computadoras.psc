Algoritmo ejercicio_20_Computadoras
	Escribir "ingrese el precio al contado (P): "
	Leer P
	Escribir "ingrese el monto de la cuota mensual (T): "
	Leer T
	total_Cuotas = T * 12
	recargo = total_Cuotas - P
	porcentaje_Recargo = (recargo / P) * 100
	Escribir "El porcentaje de recargo aplicado es: ", porcentaje_Recargo, "%"
FinAlgoritmo