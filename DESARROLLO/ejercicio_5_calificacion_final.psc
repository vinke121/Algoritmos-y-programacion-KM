Algoritmo ejercicio_5_calificacion_final
	//55%
	Escribir "notas de los trabajos"
	Leer nota1
	Leer nota2
	Leer nota3
	nota_final_trabajos = (nota1+nota2+nota3)/3
	Escribir "nota final de trabajos " nota_final_trabajos
	//30%
	Escribir "nota del examen final"
	Leer examen_final
	//15%
	Escribir "nota trabajo final"
	Leer trabajo_final
	calificacion_final = 0.55 * (nota_final_trabajos) + 0.3 * (examen_final)+ 0.15 * (trabajo_final)
	Escribir "nota final de la asignatura " calificacion_final
FinAlgoritmo