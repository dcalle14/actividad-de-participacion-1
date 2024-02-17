filas = 3
columnas = 3

matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

import random

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(1, 100)

print("Matriz:")
for fila in matriz:
    print(fila)
