Algoritmo AdivinaElNumero
	Definir numeroSecreto, intento, numero Como Entero
	Definir adivino Como Logico
	
	numeroSecreto = 42  // Pod�s cambiarlo por otro entre 1 y 100
	intento = 0
	adivino = Falso
	
	Mientras intento < 10 Y adivino = Falso Hacer
		Escribir "Intento ", intento + 1, ": Ingrese un n�mero entre 1 y 100:"
		Leer numero
		
		intento = intento + 1
		
		Si numero = numeroSecreto Entonces
			adivino = Verdadero
			Escribir "�Felicitaciones! Adivinaste el n�mero en el intento ", intento, "."
		Sino
			Si numero < numeroSecreto Entonces
				Escribir "El n�mero es mayor."
			Sino
				Escribir "El n�mero es menor."
			FinSi
		FinSi
	FinMientras
	
	Si adivino = Falso Entonces
		Escribir "Lo siento, no adivinaste el n�mero. Era ", numeroSecreto
	FinSi
FinAlgoritmo