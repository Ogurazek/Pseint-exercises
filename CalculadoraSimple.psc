Algoritmo CalculadoraSimple
	
    Definir numero1, numero2, resultado Como Real
    Definir operacion Como Caracter
	
    Escribir "Ingrese el primer n�mero:"
    Leer numero1
	
    Escribir "Ingrese el segundo n�mero:"
    Leer numero2
	
    Escribir "Ingrese la operaci�n (+, -, *, /):"
    Leer operacion
	
    Si operacion = "+" Entonces
        resultado = numero1 + numero2
        Escribir "El resultado es: ", resultado
    Sino
        Si operacion = "-" Entonces
            resultado = numero1 - numero2
            Escribir "El resultado es: ", resultado
        Sino
            Si operacion = "*" Entonces
                resultado = numero1 * numero2
                Escribir "El resultado es: ", resultado
            Sino
                Si operacion = "/" Entonces
                    Si numero2 <> 0 Entonces
                        resultado = numero1 / numero2
                        Escribir "El resultado es: ", resultado
                    Sino
                        Escribir "Error: No se puede dividir por cero."
                    FinSi
                Sino
                    Escribir "Error: Operaci�n no v�lida."
                FinSi
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo
