contador = 100
fin_contrador = 200
sumar_pares = 0
sumar_impares = 0
comprobar_pares = 0
comprobar_impares = 0

while contador <= fin_contrador:
    if contador % 2 == 0:
        sumar_pares = sumar_pares + contador
    else:
        sumar_impares = sumar_impares + contador
    contador += 1

print(f"la suma de los pares es: {sumar_pares}")
print(f"la suma de los impares es: {sumar_impares}")
