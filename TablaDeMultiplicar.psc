Algoritmo Sem�foroPeatonal
	bot�n_presionado <- Falso
	Mientras bot�n_presionado = Falso Hacer
		Si SensarBot�n() = Verdadero Entonces
			bot�n_presionado <- Verdadero
		FinSi
	FinMientras
	CambiarLuz("Verde")
	Esperar(30 segundos)
	CambiarLuz("Rojo")
FinAlgoritmo