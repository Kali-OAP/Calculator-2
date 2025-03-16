
valor1 = int(input("Ingresa un digito: "))
operacion = input("Ingrese la operacion que desea realizar: ")
valor2 = int(input("Ingrese otro digito: "))

if operacion == "+":
    print("El resultado es: ", valor1 + valor2)
elif operacion == "-":
    print("El resultado es: ", valor1 - valor2)
elif operacion == "*":
    print("El resultado es: ", valor1 * valor2)
elif operacion == "/":
    print("El resultado es: ", valor1 / valor2)
else:
    print("Operacion no valida")

    # Esto termino siendo mas simple que lo que esperaba jajaja, cuando leas esto me avisas, para proceder a desarrollar un juego muy simple XD
    