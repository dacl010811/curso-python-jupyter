
print("Bienvenido al menu principal")

while(True):
    print(''' 
          Acciones del menu
          1.- Saludar
          2.- Sumar 2 numeros
          3.- Salir
     ''')
    respuesta = int(input("Por favor selecciona una opcion:\n"))
    if respuesta == 1:
        print("Hola mundo desde python")
    elif respuesta == 2:
        num_1 = float(input("Ingresa el primer numero:\n"))
        num_2 = float(input("Ingresa el segundo numero:\n"))
        print("El resultado de sumar es : {suma}".format(suma=(num_1+num_2)))
    elif respuesta == 3:
        print("Hasta pronto...")
        break
    else:
        print("La opcion ingresada no existe")
else:
    print("El  ciclo while finalizo")
