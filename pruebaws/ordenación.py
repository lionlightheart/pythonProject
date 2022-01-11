def pedirvalores():
    valores = [None, None, None, None, None]
    indice = 0
    for indice in range(len(valores)):
        valores[indice] = int(input("introduce un valor"))
    colocarvalores(valores)


def colocarvalores(valores_sin_ordenar):

    for contador in range(len(valores_sin_ordenar) - 1):
        for contador1 in range(len(valores_sin_ordenar) - 1):
            if valores_sin_ordenar[contador1] > valores_sin_ordenar[contador1 + 1]:
                valores_sin_ordenar[contador1], valores_sin_ordenar[contador1 + 1] = valores_sin_ordenar[contador1 + 1], valores_sin_ordenar[contador1]

    print(f"El máximo es: {valores_sin_ordenar[4]}")
    print(f"El minimo es: {valores_sin_ordenar[0]}")




pedirvalores()
