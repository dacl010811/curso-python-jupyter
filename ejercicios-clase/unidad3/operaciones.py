

# Ingreso de numeros
n1 = float(input("Ingresar numero 1 : \n"))
n2 = float(input("Ingresar numero 2 : \n"))

while True:
    print('''Que operacion deseas realizar
        1.- Sumar 2 numeros
        2.- Restar 2 numeros
        3.- Multiplicar 2 numeros
        4.- Salir
    ''')
    respuesta = input("Selecciona una operacion:\n")

    if respuesta == "1":
        print("La respuesta de sumar es :  {} + {} = {}".format(n1, n2, n1+n2))
    elif respuesta == '2':
        print("La respuesta  de restar es :  {} - {} = {}".format(n1, n2, n1-n2))
    elif respuesta == '3':
        print("La respuesta  de multiplicar es :  {} * {} = {}".format(n1, n2, n1*n2))
    elif respuesta == '4':
        print("Hasta pronto!!!!")
        break
    else:
        print("Selecciona la opcion correcta \n")

print("Se termino el programa.....")
