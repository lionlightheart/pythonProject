numero1 = 0
numero2 = 0
operador = ""
SUMA = "+"
RESTA = "-"
MULTIPLICACION = "*"
DIVISON = "/"
POTECIA = "^"
resultado = 0

numero1 = int(input("Introduce numero 1: "))
numero2 = int(input("Introduce numero 2: "))
operador = str(input("Introdue unos de estos operadores: + , - , * , / , ^ "))

if SUMA == operador:
    resultado = numero1 + numero2
    print(f"La suma de {numero1} + {numero2} = {resultado}")
elif operador == RESTA:
    resultado = numero1 - numero2
    print(f"La resta de {numero1} - {numero2} = {resultado}")
elif operador == MULTIPLICACION:
    resultado = numero1 * numero2
    print(f"La multiplicacion de {numero1} * {numero2} = {resultado}")
elif operador == DIVISON:
    resultado = numero1 // numero2
    print(f"La division de {numero1} / {numero2} = {resultado}")
elif operador == POTECIA:
    resultado = numero1 ** numero2
    print(f"La suma de {numero1} ^ {numero2} = {resultado}")
