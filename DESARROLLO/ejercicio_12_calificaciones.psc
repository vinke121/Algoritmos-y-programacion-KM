Algoritmo ejercicio_12_calificaciones
	Escribir "ingrese la calificación del examen de Matemática: "
	Leer examen_Matematica
	Escribir "ingrese la calificación de la primera tarea de Matemática: "
	Leer tarea_Matematica1
	Escribir "ingrese la calificación de la segunda tarea de Matemática: "
	Leer tarea_Matematica2
	Escribir "ingrese la calificación de la tercera tarea de Matemática: "
	Leer tarea_Matematica3
	
	Escribir "ingrese la calificación del examen de Física: "
	Leer examen_Fisica
	Escribir "ingrese la calificación de la primera tarea de Física: "
	Leer tarea_Fisica1
	Escribir "ingrese la calificación de la segunda tarea de Física: "
	Leer tarea_Fisica2
	
	Escribir "ingrese la calificación del examen de Química: "
	Leer examen_Quimica
	Escribir "ingrese la calificación de la primera tarea de Química: "
	Leer tarea_Quimica1
	Escribir "ingrese la calificación de la segunda tarea de Química: "
	Leer tarea_Quimica2
	Escribir "ingrese la calificación de la tercera tarea de Química: "
	Leer tarea_Quimica3
	
	promedio_Matematica = (examen_Matematica * 0.90) + (((tarea_Matematica1 + tarea_Matematica2 + tarea_Matematica3) / 3) * 0.10)
	promedio_Fisica = (examen_Fisica * 0.80) + (((tarea_Fisica1 + tarea_Fisica2) / 2) * 0.20)
	promedio_Quimica = (examen_Quimica * 0.85) + (((tarea_Quimica1 + tarea_Quimica2 + tarea_Quimica3) / 3) * 0.15)
	
	promedio_General = (promedio_Matematica + promedio_Fisica + promedio_Quimica) / 3
	
	Escribir "El promedio en Matemática es: ", promedio_Matematica
	Escribir "El promedio en Física es: ", promedio_Fisica
	Escribir "El promedio en Química es: ", promedio_Quimica
	Escribir "El promedio general en las tres materias es: ", promedio_General
	
FinAlgoritmo