numero = 0
seguir_bucle = False
negativos = 0
positivos = 0
salir_bucle = True

while seguir_bucle != salir_bucle:
    numero = int(input("Pon numero: "))
    if numero != 0:
        if numero < 0:
            negativos += 1
        else:
            positivos += 1
    else:
        seguir_bucle = True


print(f"Hay {positivos} positivos")
print(f"Hay {negativos} negativos")
