def jugarahoracado():
    # funcion que inicial el juego
    palabra = " "

    palabra = pedirpalabrajugador1()

    compruebaplabrajugador2(palabra)


def pedirpalabrajugador1():
    # pedimos palabra a jugador 1
    return input("Pon una plabara: ")


def compruebaplabrajugador2(comprobar_palabra):

    letra = " "
    # variable que nos ayuda a comprobar la letra en el for de la linea 27
    letras = " "
    # varible donde gurado las letras que ya he puesto
    letras_guardadas = " "
    puntacion = 0
    fallos = 0

    while puntacion < len(comprobar_palabra):
        letra = input("pon letra")

        if letra in letras_guardadas:
            fallos += 1

        else:
            if letra in comprobar_palabra:
                letras_guardadas = letras_guardadas + letra
                for letras in comprobar_palabra:
                    if letra == letras:
                        puntacion += 1
            else:
                fallos += 1
    print(f"letras guradas de fallos: {letras_guardadas}")
    print(f"fallos: {fallos} ")


jugarahoracado()
