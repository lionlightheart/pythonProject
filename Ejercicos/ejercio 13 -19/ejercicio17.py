numero = 0
enero = 1
febreo = 2
marzo = 3
abril = 4
mayo = 5
junio = 6
julio = 7
agosto = 8
septiembre = 9
octubre = 10
noviembre = 11
diciembre = 12

numero = int(input("Introduce un numero: "))

if numero == enero:
    print(f"El {numero} coresponde a enero")
elif numero == febreo:
    print(f"El {numero} coresponde a febreo")
elif numero == marzo:
    print(f"El {numero} coresponde a marzo ")
elif numero == abril:
    print(f"El {numero} coresponde a abril ")
elif numero == mayo:
    print(f"El {numero} coresponde a mayo")
elif numero == junio:
    print(f"El {numero} coresponde a junio")
elif numero == julio:
    print(f"El {numero} coresponde a julio")
elif numero == agosto:
    print(f"El {numero} coresponde a agosto")
elif numero == septiembre:
    print(f"El {numero} coresponde a septiembre")
elif numero == octubre:
    print(f"El {numero} coresponde a octubre")
elif numero == noviembre:
    print(f"El {numero} coresponde a noviembre")
elif numero == diciembre:
    print(f"El {numero} coresponde a diciembre")
else:
    print(f"{numero} no es un valor válido")
