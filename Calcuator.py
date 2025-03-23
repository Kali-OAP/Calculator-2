
def calculator():
    try:
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
    except ValueError:
        print("ingrese un valor no una letra")

calculator()