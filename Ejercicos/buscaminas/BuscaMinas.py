"""
#######################################################################################
#  02/01/2022 15:39                                                                   #
#  Ramón Panadero Dobarro                                                             #
#  DAW_D 1º                                                                           #
#  Busca minas V0.0 alpha                                                                #
#######################################################################################
"""
import random

def data_input():
    return int(input())


def generar_tablero():
    eje_x = 0
    eje_y = 0
    contador = 0
    contador1 = 0
    tablero = []

    print("Introduce el ancho: ", end="")
    eje_x = data_input()
    print("Introduce el alto: ", end="")
    eje_y = data_input()
    print(f"{eje_x}, {eje_y}") # Borrar
    tablero = [["x " for x in range(eje_x)] for y in range(eje_y)]

    return tablero, eje_x, eje_y


def mostar_tablero(tablero_puro, eje_x, eje_y):
    for contador in range(eje_y):
        for contador1 in range(eje_x):
            print(f"{tablero_puro[contador][contador1]}", end="")
        print("")



def colocar_minas(minas, eje_x, eje_y):
    tablero_con_minas = [["x " for x in range(eje_x)] for y in range(eje_y)]
    mina_grafica = "m "
    random_x = 0
    random_y = 0

    random_x = random.randrange(eje_x)
    random_y = random.randrange(eje_y)
    for _ in range(minas):
        if tablero_con_minas[random_x][random_y] == mina_grafica:
            random_x = random.randrange(eje_x)
            random_y = random.randrange(eje_y)
            tablero_con_minas[random_x][random_y] = mina_grafica
        else:
            tablero_con_minas[random_x][random_y] = mina_grafica
        random_x = random.randrange(eje_x)
        random_y = random.randrange(eje_y)
    return tablero_con_minas


def generar_minas(casillas):
    porcentaje_de_minas = 0.10

    catidad_de_minas = 0
    catidad_de_minas = round(porcentaje_de_minas * casillas)
    return catidad_de_minas


def comprobar_datos(tablero, tablero_con_minas, eje_x, eje_y):
    dato_x = 0
    dato_y = 0
    vida = True
    mina = "m "

    print("Introduce el eje x:", end="")
    dato_x = data_input()
    print("Introduce el eje y:", end="")
    dato_y = data_input()
    if dato_x in range(eje_x) and dato_y in range(eje_y):
        if tablero_con_minas[dato_x][dato_y] == mina:
            tablero[dato_x][dato_y] = mina
            vida = True
            return tablero, vida
        else:
            print("perdiste")
            vida = False
            return tablero, vida
    else:
        print("Sos re bobo")
    return tablero, vida


def jugar_buscaminas():
    casillas = 0
    vida = True
    verdadero_faslo = True
    tablero = []

    tablero, eje_x, eje_y = generar_tablero()
    casillas = eje_x * eje_y
    minas = generar_minas(casillas)
    tablero_con_minas = colocar_minas(minas, eje_x, eje_y)
    mostar_tablero(tablero, eje_x, eje_y)
    while vida == verdadero_faslo and tablero != tablero_con_minas:
        tablero, vida = comprobar_datos(tablero, tablero_con_minas, eje_x, eje_y)
        mostar_tablero(tablero, eje_x, eje_y)


jugar_buscaminas()
