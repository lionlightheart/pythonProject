numero_lineas = 0
espacios_blancos = 0
asteriscos = 1
contador = 0
restas_de_espacios = 1

numero_lineas = int(input("pon el número de lineas para la piramide: "))
espacios_blancos = numero_lineas

for contador in range(numero_lineas):
    espacios_blancos -= restas_de_espacios
    print(" "*espacios_blancos, end="")
    print("*"*asteriscos)
    asteriscos += 2
    contador += 1
