#ejercicio 7
max_altura=0
while True:   
    estudiantes=int(input("ingrese la altura del estudiante: "))    
    if (max_altura == 0):
        max_altura=max_altura + estudiantes
    elif(max_altura >= estudiantes):
        max_altura=max_altura
    elif(max_altura < estudiantes):
        max_altura = estudiantes
    print(f"la altura maxima es: {max_altura}")

