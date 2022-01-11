"""
16-12-2021 Jueves

Ramon Panadero Dobarrro

PROGRAMACION DAW_D

Pythom 3.10
"""

def transpuesta():

    datos = [[1, 2], [3, 4]]
    indice = 0
    indice1 = 0
    datos_ordenados = [[],[]]

    for indice in range(len(datos)):
        for indice1 in range(len(datos)):
            datos_ordenados[indice][indice1] += datos[indice][indice1]
            print(datos_ordenados)ç

    # No funiona na


transpuesta()