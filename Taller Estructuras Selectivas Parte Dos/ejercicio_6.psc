Algoritmo ejercicio_6
	Escribir "ingrese un a�o"
	Leer a�o	
	operacion1=a�o%4
	operacion2=a�o%400
	operacion3=a�o%100
	Si operacion1=0 & operacion2=0 Entonces
		Escribir"es bisiesto"
	SiNo
		si operacion3=1 Entonces			
			Escribir "no es bisiesto"
		FinSi
	Fin Si
FinAlgoritmo
