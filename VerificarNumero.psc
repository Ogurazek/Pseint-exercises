Algoritmo VerificarNumero
	Definir numero Como Entero
	
	Escribir "Ingrese un número:"
	Leer numero
	
	Si numero > 0 Entonces
		Escribir "El número es positivo."
	Sino
		Si numero < 0 Entonces
			Escribir "El número es negativo."
		Sino
			Escribir "El número es cero."
		FinSi
	FinSi
FinAlgoritmo
