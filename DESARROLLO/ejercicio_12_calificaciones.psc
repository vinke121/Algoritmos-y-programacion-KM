Algoritmo ejercicio_12_calificaciones
	Escribir "ingrese la calificaci�n del examen de Matem�tica: "
	Leer examen_Matematica
	Escribir "ingrese la calificaci�n de la primera tarea de Matem�tica: "
	Leer tarea_Matematica1
	Escribir "ingrese la calificaci�n de la segunda tarea de Matem�tica: "
	Leer tarea_Matematica2
	Escribir "ingrese la calificaci�n de la tercera tarea de Matem�tica: "
	Leer tarea_Matematica3
	
	Escribir "ingrese la calificaci�n del examen de F�sica: "
	Leer examen_Fisica
	Escribir "ingrese la calificaci�n de la primera tarea de F�sica: "
	Leer tarea_Fisica1
	Escribir "ingrese la calificaci�n de la segunda tarea de F�sica: "
	Leer tarea_Fisica2
	
	Escribir "ingrese la calificaci�n del examen de Qu�mica: "
	Leer examen_Quimica
	Escribir "ingrese la calificaci�n de la primera tarea de Qu�mica: "
	Leer tarea_Quimica1
	Escribir "ingrese la calificaci�n de la segunda tarea de Qu�mica: "
	Leer tarea_Quimica2
	Escribir "ingrese la calificaci�n de la tercera tarea de Qu�mica: "
	Leer tarea_Quimica3
	
	promedio_Matematica = (examen_Matematica * 0.90) + (((tarea_Matematica1 + tarea_Matematica2 + tarea_Matematica3) / 3) * 0.10)
	promedio_Fisica = (examen_Fisica * 0.80) + (((tarea_Fisica1 + tarea_Fisica2) / 2) * 0.20)
	promedio_Quimica = (examen_Quimica * 0.85) + (((tarea_Quimica1 + tarea_Quimica2 + tarea_Quimica3) / 3) * 0.15)
	
	promedio_General = (promedio_Matematica + promedio_Fisica + promedio_Quimica) / 3
	
	Escribir "El promedio en Matem�tica es: ", promedio_Matematica
	Escribir "El promedio en F�sica es: ", promedio_Fisica
	Escribir "El promedio en Qu�mica es: ", promedio_Quimica
	Escribir "El promedio general en las tres materias es: ", promedio_General
	
FinAlgoritmo