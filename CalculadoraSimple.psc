Algoritmo CalculadoraSimple
	
    Definir numero1, numero2, resultado Como Real
    Definir operacion Como Caracter
	
    Escribir "Ingrese el primer número:"
    Leer numero1
	
    Escribir "Ingrese el segundo número:"
    Leer numero2
	
    Escribir "Ingrese la operación (+, -, *, /):"
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
                    Escribir "Error: Operación no válida."
                FinSi
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo
