Algoritmo ejercicio_19_Mayorista_Agricola
	Escribir "Introduce la cantidad de naranjas compradas "
	Leer naranjas
	Escribir "Introduce el valor por docena "
	Leer Valor_Docena
	Escribir "Introduce el monto total obtenido de la venta de las naranjas "
	Leer venta_total
	valor_total = (naranjas / 12) * Valor_Docena
	ganancia = venta_total - valor_total
	porcentaje_de_ganancia = (ganancia / valor_total) * 100
	Escribir "El porcentaje de ganancia obtenida " porcentaje_de_ganancia "%"
FinAlgoritmo