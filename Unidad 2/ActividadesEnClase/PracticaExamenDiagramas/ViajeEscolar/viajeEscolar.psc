Algoritmo viajeEscolar
	Escribir "¿Cuantos alumnos van al viaje?"
	Leer numeroDeAlumnos
	Si numeroDeAlumnos > 100 Entonces
		costo = numeroDeAlumnos * 20
	SiNo
		Si numeroDeAlumnos >= 50 Entonces
			costo = numeroDeAlumnos * 35
		SiNo
			Si numeroDeAlumnos >= 20 Entonces
				costo = numeroDeAlumnos * 40
			SiNo
				costo = numeroDeAlumnos * 70
			FinSi
		FinSi
	FinSi
	Escribir "El costo del viaje es de:", " ", "$", costo
FinAlgoritmo
