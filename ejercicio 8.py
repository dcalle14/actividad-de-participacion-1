def invertir_lista(lista):

    lista_invertida = lista[::-1]
    return lista_invertida


numeros = [1, 2, 3, 4, 5]
numeros_invertidos = invertir_lista(numeros)
print("Lista original:", numeros)
print("Lista invertida:", numeros_invertidos)
