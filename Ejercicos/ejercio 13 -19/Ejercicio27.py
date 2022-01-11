numero = 0
seguir_bucle = False
hubo_diez = False
salir_bucle = True

while seguir_bucle != salir_bucle:
    numero = int(input("Pon numero: "))
    if numero != -1:
        if numero > 10 or numero < -1:
            print("no es un número válido")
            break
        else:
            if numero == 10:
                hubo_diez = True

    else:
        seguir_bucle = True

if hubo_diez == True:
    print(f"Hay un 10")
else:
    print("No hay ningún 10")
