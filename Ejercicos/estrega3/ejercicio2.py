def pedir_cadenas():
    adn1 = ""
    adn2 = ""
    adn1 = input("Cadena de ADN1: ").upper()
    adn2 = input("Cadena de ADN2: ").upper()

    return adn1, adn2


def comparar_cadenas(cadena_adn1, cadena_adn2):
    cadena_adn_mayor = ""
    cadena_adn_menor = ""
    SUMA_DE_PUNTOS = 1
    indice = 0
    puntos_no_iguales = 0

    cadena_adn_menor, cadena_adn_mayor = ordenar_cadenas(cadena_adn1, cadena_adn2)
    puntos_no_iguales = len(cadena_adn_mayor) - len(cadena_adn_menor)
    for indice in range(len(cadena_adn_menor)):
        if cadena_adn_menor[indice] != cadena_adn_mayor[indice]:
            puntos_no_iguales += SUMA_DE_PUNTOS
    return puntos_no_iguales


def ordenar_cadenas(cadena_adn1, cadena_adn2):
    longitud_cadena_adn1 = 0
    longitud_cadena_adn2 = 0

    longitud_cadena_adn1 = len(cadena_adn1)
    longitud_cadena_adn2 = len(cadena_adn2)

    if longitud_cadena_adn1 <= longitud_cadena_adn2:

        return cadena_adn1, cadena_adn2
    else:
        return cadena_adn2, cadena_adn1


def comenzar_comparar():
    cadena_adn1 = ""
    cadena_adn2 = ""
    distancia_hamming = 0

    cadena_adn1, cadena_adn2 = pedir_cadenas()
    distancia_hamming = comparar_cadenas(cadena_adn1, cadena_adn2)
    print(f"La distancia Hamming es {distancia_hamming} ya que hay {distancia_hamming} ", end="")
    print("que no son iguales en las dos cadenas en la misma posición")


comenzar_comparar()
