Estudiantes={}
total_estudiantes=10

#creacion del diccionario
for i in range (1, total_estudiantes+1):
    nombre_estudiante=input("ingrese el nombre del estudiante: ")
    nota_del_estudiante=float(input("ingrese la nota del estudiante de 1 a 10: "))
    Estudiantes[str(i)] = {"nombre estudiante": nombre_estudiante, "nota del estudiante": nota_del_estudiante}
print(Estudiantes)


# nombres de los estudiantes aprobados y reprobados
Estudiantes_Aprobados=[]
Estudiantes_reprobados=[]
for estudiante in Estudiantes.values():
    if Estudiantes["nota_del_estudiante"] >= 6.0:
        Estudiantes_Aprobados=Estudiantes["nombre estudiante"]
    elif Estudiantes["nota_del_estudiante"] < 6.0:
        Estudiantes_reprobados=Estudiantes["nombre estudiante"]
    print(Estudiantes_Aprobados)
    print(Estudiantes_reprobados)

#generador de promedio.
promedio_notas=()
for i in Estudiantes["nota_del_estudiante"]:
   promedio_notas = Estudiantes in Estudiantes.values / Estudiantes.len["nota_del_estudiante"]
   print(promedio_notas)




