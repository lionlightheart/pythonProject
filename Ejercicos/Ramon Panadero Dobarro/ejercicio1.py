"""
16-12-2021 Jueves

Ramon Panadero Dobarrro

PROGRAMACION DAW_D

Pythom 3.10
"""


def caluclar_mae(lista_1, lista_2):
    divisor = len(lista_1)
    indice = 0
    lista_1_en_enteros = 0
    lista_2_en_enteros = 0
    total_suma = 0
    total_mae = 0

    for indice in range(len(lista_1)):
        lista_1_en_enteros = int(lista_1[indice])
        lista_2_en_enteros = int(lista_2[indice])

        if lista_1_en_enteros >= lista_2_en_enteros:
            total_suma += lista_1_en_enteros - lista_2_en_enteros
        else:
            total_suma += lista_2_en_enteros - lista_1_en_enteros
    total_mae = total_suma / divisor
    print(f"el valor de mae es: {total_mae}")

    return total_mae


def comprobar_cadenas(lista_1, lista_2):
    VERDADERO = True
    FALSO = False

    if len(lista_1) == len(lista_2):
        return VERDADERO
    else:
        return FALSO


def pedir_listas():
    guardar_lista = ""

    guardar_lista = input("Pon un número consecutivos de numeros del 0 al 9 sin ser mayor a 9: ")

    return guardar_lista


def mae():
    SON_IGUALES = True
    iguales = False
    lista_1 = ""
    lista_2 = ""
    valor_mae = 0

    lista_1 = pedir_listas()
    lista_2 = pedir_listas()
    iguales = comprobar_cadenas(lista_1, lista_2)
    if iguales == SON_IGUALES:
        valor_mae = caluclar_mae(lista_1, lista_2)
    else:
        print(f"La cadena {lista_1} y la cadena {lista_2} no son iguales :(")

    return valor_mae


mae()
