def fahrenheit_a_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

celsius = fahrenheit_a_celsius(fahrenheit)

print("La temperatura equivalente en grados Celsius es:", celsius)
