def factorial(numero):

    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))

resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
