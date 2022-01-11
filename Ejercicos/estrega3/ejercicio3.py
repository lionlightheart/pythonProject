def comenzar_isbn():
    isbn_con_guiones = ""
    isbn_sin_con_guiones = ""

    isbn_con_guiones = pedir_isbn()
    isbn_sin_guiones = quitar_guiones(isbn_con_guiones)
    validar_isbn(isbn_sin_guiones)


def pedir_isbn():

    return input("Introduce el ISBN con el siguiente formato X-XXX-XXXXX-X: ").upper()


def quitar_guiones(isbn_con_guiones):
    GUION = "-"
    isbn_sin_guiones = ""
    indice = 0

    for indice in range(len(isbn_con_guiones)):
        if isbn_con_guiones[indice] != GUION:
            isbn_sin_guiones += isbn_con_guiones[indice]

    return isbn_sin_guiones


def validar_isbn(isbn_sin_guiones):
    LETRA_X = "X"
    VALOR_X = 10
    VALOR_MODULO = 11
    VALOR_CORRECTO = 0
    SUMA_RESTA = 1
    multiplicacion_maxima = 10
    multiplicacion_minima = 1
    valores_int_isbn = 0
    resultado_final = 0
    indice = 0
    total = 0

    for indice in range(len(isbn_sin_guiones)):
        if isbn_sin_guiones[indice] != LETRA_X:
            valores_int_isbn = int(isbn_sin_guiones[indice])
            total = total + (valores_int_isbn * multiplicacion_maxima)
        else:
            total = total + (VALOR_X * multiplicacion_maxima)
        multiplicacion_minima += SUMA_RESTA
        multiplicacion_maxima -= SUMA_RESTA
    resultado_final = total % VALOR_MODULO

    if resultado_final == VALOR_CORRECTO:
        print("ISBN correcto")
    else:
        print("ISBN incorrecto")


comenzar_isbn()
