numeroA = 0
numeroB = 0
numeroResultado = 0
contador = 0

numeroA = int(input("introduce un número: "))
numeroB = int(input("introduce un número: "))

numeroResultado = numeroA

while contador < numeroB:

    numeroResultado = numeroResultado * numeroA
    contador += 1

print(numeroResultado)
