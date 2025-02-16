print("ejercicio_12_calificaciones")
#matematicas 90% examen y 10% tareas  
examen_matematicas = float(input("Calificación del examen de matemáticas: "))
tarea_matematicas1 = float(input("Calificación de la tarea de matemáticas1: "))
tarea_matematicas2 = float(input("Calificación de la tarea de matemáticas2: "))
tarea_matematicas3 = float(input("Calificación de la tarea de matemáticas3: "))

promedio_matematicas = float(examen_matematicas*0.9) + (((tarea_matematicas1 + tarea_matematicas2 + tarea_matematicas3)/3)*0.1)
print("El promedio de matemáticas es: ", promedio_matematicas)

#fisica 80% examen y 20% tareas
examen_fisica = float(input("Calificación del examen de física: "))
tarea_fisica1 = float(input("Calificación de la tarea de física1: "))
tarea_fisica2 = float(input("Calificación de la tarea de física2: "))
promedio_fisica = float(examen_fisica*0.8) + (((tarea_fisica1 + tarea_fisica2)/2)*0.2)
print("El promedio de física es: ", promedio_fisica)

# quimica 85% examen y 15% tareas
examen_quimica = float(input("Calificación del examen de química: "))
tarea_quimica1 = float(input("Calificación de la tarea de química1: "))
tarea_quimica2 = float(input("Calificación de la tarea de química2: "))
tarea_quimica3 = float(input("Calificación de la tarea de química3: "))


promedio_quimica = float(examen_quimica*0.85) + (((tarea_quimica1 + tarea_quimica2 + tarea_quimica3)/3)*0.15)
print("El promedio de química es: ", promedio_quimica)

#promedio general
promedio_general = (promedio_matematicas + promedio_fisica + promedio_quimica)/3
print("El promedio general es: ", promedio_general)
