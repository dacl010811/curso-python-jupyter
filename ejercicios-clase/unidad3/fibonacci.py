
# 0,1,1,2,3,5,8,13,21,34...etc
# 0 1 2 3 4 5 .................

numero_serie = int(input("Ingrese  la serie del fibonacci"))
n1, n2 = 0, 1
contador = 0

if numero_serie < 0:
    print("Ingresa un numero positivo")
elif numero_serie == 1:
    print("El fibonacci del numero {} es  = 1".format(n1))
else:
    while contador < numero_serie:
        print(n1)
        fact = n1 + n2
        n1 = n2
        n2 = fact
        contador += 1
