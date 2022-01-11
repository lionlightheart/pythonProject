"""
16-12-2021 Jueves

Ramon Panadero Dobarrro

PROGRAMACION DAW_D

Pythom 3.10
"""


def iniciar_convertir_a_romanos():
    NO_MAYOR_IGUAL_3000 = 3000
    numero_decimal = 0
    numero_decimal = pedir_numero()
    if int(numero_decimal) < NO_MAYOR_IGUAL_3000:
        converir_decimal_a_romano(numero_decimal)
    else:
        print("No es valido el numero: :_(")


def pedir_numero():
    numero = ""
    numero = input("Pon un número decimal menor a 3000: ")

    return numero


def converir_decimal_a_romano(numero_decimal):
    RESTO_MOD_MIL = 1000
    RESTO_MOD_500 = 500
    RESTO_MOD_100 = 100
    RESTO_MOD_50 = 50
    RESTO_MOD_10 = 10
    RESTO_MOD_5 = 5
    LETRA_I = "I"
    LETRA_V = "V"
    LETRA_X = "X"
    LETRA_L = "L"
    LETRA_C = "C"
    LETRA_D = "D"
    LETRA_M = "M"
    total_division = 0
    numero_decimal_en_int = 0
    total_romano = ""

    numero_decimal_en_int = int(numero_decimal)

    total_division = numero_decimal_en_int // RESTO_MOD_MIL
    for _ in range(total_division):
        total_romano += LETRA_M
    numero_decimal_en_int = numero_decimal_en_int % RESTO_MOD_MIL

    total_division = numero_decimal_en_int // RESTO_MOD_500
    for _ in range(total_division):
        total_romano += LETRA_D
    numero_decimal_en_int = numero_decimal_en_int % RESTO_MOD_500

    total_division = numero_decimal_en_int // RESTO_MOD_100
    for _ in range(total_division):
        total_romano += LETRA_C
    numero_decimal_en_int = numero_decimal_en_int % RESTO_MOD_100

    total_division = numero_decimal_en_int // RESTO_MOD_100
    for _ in range(total_division):
        total_romano += LETRA_C
    numero_decimal_en_int = numero_decimal_en_int % RESTO_MOD_100

    total_division = numero_decimal_en_int // RESTO_MOD_50
    for _ in range(total_division):
        total_romano += LETRA_L
    numero_decimal_en_int = numero_decimal_en_int % RESTO_MOD_50

    total_division = numero_decimal_en_int // RESTO_MOD_10
    for _ in range(total_division):
        total_romano += LETRA_X
    numero_decimal_en_int = numero_decimal_en_int % RESTO_MOD_10

    total_division = numero_decimal_en_int // RESTO_MOD_5
    for _ in range(total_division):
        total_romano += LETRA_V
    numero_decimal_en_int = numero_decimal_en_int % RESTO_MOD_5

    for _ in range(numero_decimal_en_int):
        total_romano += LETRA_I

    print(total_romano)


iniciar_convertir_a_romanos()
