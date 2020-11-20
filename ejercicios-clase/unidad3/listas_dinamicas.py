
lista_pares = []
lista_impares = []

inicio = int(input("Ingresa el inicio de la serie : \n"))
fin = int(input("Ingresa el final de la serie : \n"))

lista_original = list(range(inicio,fin+1))


for numero in lista_original:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f"Lista original tiene :  {len(lista_original)} elementos. \n => {lista_original} ")
print(f"Lista pares es = {len(lista_pares)} elementos: \n {lista_pares}")
print(f"Lista impares es {len(lista_impares)} elementos: \n {lista_impares}")

print ("**************************Slicing de Pares**************************")

if len(lista_pares) % 2 == 0:
    mitad = len(lista_pares)/2
    lista_1 = lista_pares[0:int(mitad)]
    lista_2 = lista_pares[int(mitad):]
    print(f"{len(lista_1)} elementos : \n {lista_1}")
    print(f"{len(lista_2)} elementos : \n {lista_2}")
else:
    mitad = (len(lista_pares)-1)/2
    lista_1 = lista_pares[0:int(mitad)]
    lista_2 = lista_pares[int(mitad):]
    print(f"{len(lista_1)} elementos : \n {lista_1}")
    print(f"{len(lista_2)} elementos : \n {lista_2}")


print ("**************************Slicing de Impares**************************")

if len(lista_impares) % 2 == 0:
    mitad = len(lista_impares)/2
    lista_1 = lista_impares[0:int(mitad)]
    lista_2 = lista_impares[int(mitad):]
    print(f"{len(lista_1)} elementos : \n {lista_1}")
    print(f"{len(lista_2)} elementos : \n {lista_2}")
else:
    mitad = (len(lista_impares)-1)/2
    lista_1 = lista_impares[0:int(mitad)]
    lista_2 = lista_impares[int(mitad):]
    print(f"{len(lista_1)} elementos : \n {lista_1}")
    print(f"{len(lista_2)} elementos : \n {lista_2}")




