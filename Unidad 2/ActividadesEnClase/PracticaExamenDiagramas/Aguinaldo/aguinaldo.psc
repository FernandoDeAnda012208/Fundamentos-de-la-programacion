Algoritmo aguinaldo
	Escribir "¿Cuanto tiempo llevas trabajando en la empresa?"
	Leer antiguedad
	Escribir "¿Cual es tu sueldo?"
	Leer sueldo
	Si antiguedad > 4 Entonces
		Si sueldo >= 2000 Entonces
			bonoP = 0.2
		SiNo
			bonoP = 0.25
		FinSi
	SiNo
		bonoP = 0.2
	FinSi
	bono = sueldo * bonoP
	Escribir "Tu aguinaldo de este año fue de:", " ", "$",bono
FinAlgoritmo
