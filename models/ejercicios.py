class Ejercicios:

    
    # EJERCICIO 1 - PAR O IMPAR
   

    def par_o_impar(self, numero):

        if numero % 2 == 0:
            return f"El número {numero} es PAR."
        else:
            return f"El número {numero} es IMPAR."

    
    # EJERCICIO 2 - TABLA DE MULTIPLICAR
    

    def tabla_multiplicar(self, numero):

        tabla = []

        for i in range(1, 11):

            resultado = numero * i

            tabla.append(
                f"{numero} x {i} = {resultado}"
            )

        return tabla

    
    # EJERCICIO 3 - ADIVINA EL NÚMERO
    

    def adivinar_numero(self, numero_secreto, intento):

        if intento < numero_secreto:

            return "El número secreto es MAYOR."

        elif intento > numero_secreto:

            return "El número secreto es MENOR."

        else:

            return "¡Correcto! Has adivinado el número."