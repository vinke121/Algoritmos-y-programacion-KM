Algoritmo ejercicio_14_cobro_luz
	Escribir "ingrese la lectura anterior (en kilovatios): "
	Leer lectura_Anterior
	Escribir "ingrese la lectura actual (en kilovatios): "
	Leer lectura_Actual
	Escribir "ingrese el costo por kilovatio: "
	Leer costo_Kilovatio
	consumo = lectura_Actual - lectura_Anterior
	monto_Total = consumo * costo_Kilovatio
	Escribir "El monto total a pagar por el consumo de luz eléctrica es: ", monto_Total, " COP"	
FinAlgoritmo
