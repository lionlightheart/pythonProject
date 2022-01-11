numero = 0
contador = 0
negativos = 0
positivos = 0


while contador < 10:
    numero = int(input("Pon numero: "))
    if numero < 0:
        negativos += 1
    else:
        positivos += 1

    contador += 1

print(f"Hay {positivos} positivos")
print(f"Hay {negativos} negativos")
