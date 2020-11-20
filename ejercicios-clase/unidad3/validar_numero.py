numeros = [1, 3, 6, 9, 2]

while True:
    numero = float(input("Ingrese un numero entre el 0 y el 9 \n "))
    if numero >= 0 and numero <= 9:
        break

if numero in numeros:
    print("El  numero", numero, "se encuentra en la lista", numeros)
else:
    print("El  numero", numero, "no se encuentra en la lista", numeros)
