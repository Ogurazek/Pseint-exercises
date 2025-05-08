Algoritmo AdivinaElNumero
	Definir numeroSecreto, intento, numero Como Entero
	Definir adivino Como Logico
	
	numeroSecreto = 42  // Podés cambiarlo por otro entre 1 y 100
	intento = 0
	adivino = Falso
	
	Mientras intento < 10 Y adivino = Falso Hacer
		Escribir "Intento ", intento + 1, ": Ingrese un número entre 1 y 100:"
		Leer numero
		
		intento = intento + 1
		
		Si numero = numeroSecreto Entonces
			adivino = Verdadero
			Escribir "¡Felicitaciones! Adivinaste el número en el intento ", intento, "."
		Sino
			Si numero < numeroSecreto Entonces
				Escribir "El número es mayor."
			Sino
				Escribir "El número es menor."
			FinSi
		FinSi
	FinMientras
	
	Si adivino = Falso Entonces
		Escribir "Lo siento, no adivinaste el número. Era ", numeroSecreto
	FinSi
FinAlgoritmo