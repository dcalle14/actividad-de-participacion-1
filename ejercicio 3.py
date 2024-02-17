import random

cantidad_numeros = 5

numeros_aleatorios = [random.randint(1, 100) for _ in range(cantidad_numeros)]

print("Números aleatorios:")

for numero in numeros_aleatorios:
    print(numero)