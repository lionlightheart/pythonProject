import math


def iniciarcalculararea():

    radio1 = 0
    radio2 = 0
    area1 = 0
    area2 = 0

    radio1, radio2 = pedirradio()
    area1, area2 = (calculararea(radio1, radio2))
    print(f"el area de la cora es: {calcularcorona(area1, area2)}")

def pedirradio():
    radio_pedido1 = 0
    radio_pedido2 = 0

    radio_pedido1 = abs(int(input("pon un radio: ")))
    radio_pedido2 = abs(int(input("pon un radio: ")))
    return radio_pedido1, radio_pedido2


def calculararea(acalcular_radio1, acalcular_radio2):
    area1 = 0.0
    area2 = 0.0
    CUADRADO = 2

    area1 = math.pi * acalcular_radio1**CUADRADO
    area2 = math.pi * acalcular_radio2**CUADRADO
    return area1, area2

def calcularcorona(area1, area2):

    area_corona = 0

    if area1 >= area2:
        area_corona = area1 - area2
    else:
        area_corona = area2 - area1

    return area_corona


iniciarcalculararea()
