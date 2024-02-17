def media_aritmetica(numeros):

    total = sum(numeros)
    cantidad = len(numeros)
    if cantidad == 0:
        return 0
    else:
        return total / cantidad

numeros = [10, 20, 30, 40, 50]

media = media_aritmetica(numeros)
print("La media aritmética de la lista es:", media)