Algoritmo SemáforoPeatonal
	botón_presionado <- Falso
	Mientras botón_presionado = Falso Hacer
		Si SensarBotón() = Verdadero Entonces
			botón_presionado <- Verdadero
		FinSi
	FinMientras
	CambiarLuz("Verde")
	Esperar(30 segundos)
	CambiarLuz("Rojo")
FinAlgoritmo