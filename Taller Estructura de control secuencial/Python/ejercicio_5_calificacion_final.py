print("ejercicio_4_descuento_de_la_tienda")
#55%
nota1=float(input("ingrese el valor de la primera nota:"))
nota2=float(input("ingrese el valor de la segunda nota:"))
nota3=float(input("ingrese el valor de la tercera nota:"))  
nota_final_trabajos=float((nota1+nota2+nota3)/3)
print("la nota final de los trabajos es:",nota_final_trabajos)
#30%
examen_final=float(input("ingrese el valor del examen final:"))
#15%
trabajo_final=float(input("ingrese el valor del trabajo final:"))
calificacion_final=float((nota_final_trabajos*0.55)+(examen_final*0.30)+(trabajo_final*0.15))
print("la calificacion final es:",calificacion_final)