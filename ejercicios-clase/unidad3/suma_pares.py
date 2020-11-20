import time

# Generar numeros
suma = 0
lista = range(0, 101, 2)

print(type(lista))

for i, e in enumerate(lista):
    print("[", i, "] = ", e)
    time.sleep(1)
    suma += e

print("La sumatoria de los numeros pares es : ", suma)

# Segunda opcion

suma = sum(range(0, 101, 2))
print(suma)

#  tercera opcion
num = 0
suma_1 = 0
while num <= 100:
    if num % 2 == 0:
        suma_1 += num
    num += 1
else:
    print("El resultado de sumar los pares es : ", suma_1)
