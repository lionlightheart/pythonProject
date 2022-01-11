ano = 0
BISIESTO = 0
DIVIDENDO = 4

ano = int(input("introduce un año: "))

if (ano % DIVIDENDO) == BISIESTO:
    print(f"El año {ano} es bisiesto")
else:
    print(f"El año {ano}  no es bisiesto")