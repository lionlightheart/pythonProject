numero = 0
contador = 0
positivo_negativo = False
negativo = True

while contador <= 10:
    numero = int(input("Pon numero: "))
    if numero < 0:
        positivo_negativo = True
    contador += 1

if positivo_negativo == negativo:
    print("hay negativo")
else:
    print("no hay negativos")
