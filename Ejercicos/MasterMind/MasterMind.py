import random


def comenzarjuego():

    """Funcion para inicializar el masterMind,
    en el cual primero elejimos los "colores" y se lo pazsamos jugaraljuego"""

    colores_para_jugar = elegircolores()
    print(colores_para_jugar)
    jugaraljuego(colores_para_jugar)


def elegircolores():

    """En Esta función elegiremos los cuatro colores
    para que empieze el juego mediante un bucle que da 4 vueltas"""

    MAX_COLORES = 4
    colores_elegios = list("*" * 4)
    contador_posicion = 0

    while contador_posicion < MAX_COLORES:
        colores_elegios[contador_posicion] = encontrarcolores()
        contador_posicion += 1
    return colores_elegios


def encontrarcolores():
    """en esta función guradamos los posible colores y devolvemos 1 cada vez que se llama"""
    numeroaleatrio = 0
    lista_colores = list("ABCDEF")
    numeroaleatrio = random.randrange(6)

    return lista_colores[numeroaleatrio]


def jugaraljuego(colore_elegidos):
    """
    esta fución controla  el juego ya que es la que va pidiendo
    los"colores" y manda los datos a las diferentes
    resultado_grafico hace referencia al codigo de numerico ordenado que más adelante seran + o -
    tipo_resultado hace referencia al codigo numerico sin ordenar
    pistas_finales son las pistas ordenadas que se le muestra al jugador
    """
    pedir_colores = ""
    resultado_grafico = ""
    tipo_resultado = ""
    pistas_finales = ""
    elegidos_colores = colore_elegidos
    fin_del_juego = False
    FINAL = True

    while fin_del_juego != FINAL:
        pedir_colores = input("Pon 4 letras de estas opciones A B C D E F: ")
        pedir_colores = pedir_colores.upper()
        fin_del_juego, tipo_resultado = comprobarcolores(pedir_colores, elegidos_colores)
        resultado_grafico = colocarvalores(tipo_resultado)
        pistas_finales = pistasordenadas(resultado_grafico)
        print(pistas_finales)


def comprobarcolores(colores_pedidos, colores_a_comprobar):

    valor_resolver = ""
    letras_acertadas = 0
    posiciones_guardadas = 0
    rango = 4
    posicion = 0
    elegir_final = False
    colores_guardados = list(colores_pedidos)
    guardar_color = list(colores_a_comprobar)
    if colores_guardados == guardar_color:
        elegir_final = True
    else:
        for posicion in range(rango):
            if colores_guardados[posicion] in guardar_color and colores_guardados[posicion] == guardar_color[posicion]:
                elegir_final = False
                valor_resolver = valor_resolver + "1"
            elif colores_guardados[posicion] in guardar_color:
                elegir_final = False
                valor_resolver = valor_resolver + "2"
        return elegir_final, valor_resolver


def colocarvalores(valor_del_resultado):

    resultado_lista = list(valor_del_resultado)
    cont = 0

    pistas_finales = ""
    for cont1 in range(len(resultado_lista)):
        for cont in range(len(resultado_lista) - 1):
            if resultado_lista[cont] > resultado_lista[cont + 1]:
                resultado_lista[cont], resultado_lista[cont + 1] = resultado_lista[cont + 1], resultado_lista[cont]

    return resultado_lista


def pistasordenadas(pistas_en_codigo):
    cont1 = 0
    valor_mas = "1"
    valor_guion = "2"
    mas = "+"
    guion = "-"
    pistas_finales = ""

    for cont1 in range(len(pistas_en_codigo)):
        if pistas_en_codigo[cont1] == valor_mas:
            pistas_finales = pistas_finales + mas
        elif pistas_en_codigo[cont1] == valor_guion:
            pistas_finales = pistas_finales + guion
    return pistas_finales


comenzarjuego()
