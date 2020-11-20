# -*- coding: utf-8 -*-

cadena = "zeréP nauJ,01"

# Juan Pérez ha sacado un 10 de nota.
cadena_invertida = cadena[::-1]

print(cadena_invertida[3:], "ha sacado un", cadena_invertida[:2], " de nota.")

print("{p1} ha sacado un {p2} de nota. ".format(
    p1=cadena_invertida[3:], p2=cadena_invertida[:2]))

print("{} ha sacado un {} de nota.".format(cadena_invertida[3:], cadena_invertida[:2]))

print("mdsdsfdsfds","fdsfsdfdsf","fdsfsdfsdf","fdsfsdfdsf")

print("mdsdsfdsfds"+"fdsfsdfdsf"+"fdsfsdfsdf"+"fdsfsdfdsf")



"""print(cadena_invertida) # "10,Juan Pérez"
parte_1 = cadena_invertida[3:]
print("P1 : "+parte_1)
parte_2 = cadena_invertida[:2]
print("P2 :"+parte_2)
print(parte_1+" has sacado un "+parte_2+" de nota.")"""


a,b,c = 1,'Hola',True

a = 1
b = 'Hola'
c = True
