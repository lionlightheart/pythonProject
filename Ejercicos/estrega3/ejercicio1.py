def pedir_numero():
    numero = ""
    numero = input("Introduce un numero: ")

    return numero


def calcular_longitud(numero_pedidio):
    longiitud_cadena = ""
    longitud_cadena = str(len(numero_pedidio))
    return longitud_cadena


def definir_armstrong(numero_pedidio, longitud_total):
    """total es el numero que ha introducido el ususario que comparaemos
    con el numero suma para saber si está Armstrong"""

    indice = 0
    numero_en_entero = 0
    numero_suma = 0
    total = int(numero_pedidio)
    longitud_en_numero = int(longitud_total)
    for indice in range(longitud_en_numero):
        numero_en_entero = int(numero_pedidio[indice])
        numero_suma = numero_suma + (numero_en_entero**longitud_en_numero)

    if numero_suma == total:
        print(f"El numero {total} es Armstrong ")
    else:
        print(f"El numero {total} no es Armstrong")


def comenzar_programa():
    numero = pedir_numero()
    longitud = calcular_longitud(numero)
    definir_armstrong(numero, longitud)


comenzar_programa()
