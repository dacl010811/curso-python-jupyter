import time

while True:
    print("{}\n".format("Menu Principal"),
          "{:15}\n".format("1.- Fibonacci"),
          "{:15}\n".format("2.- Factorial"),
          "{:15}\n".format("3.- Slicing-Listas"),
          "{:15}\n".format("4.- Reloj Digital"),
          "{:15}\n".format("S.- Salir")
          )
    opcion = input("Seleccione la operacion a realizar : \n")

    if opcion == '1':

        """Este parte del codigo realiza el fibonacci de cualquier numero
        """
        numero_serie = int(input("Ingrese  la serie del fibonacci : \n"))
        n1, n2 = 0, 1
        contador = 0

        if numero_serie < 0:
            print("Ingresa un numero positivo")
        elif numero_serie == 0:
            print("El fibonacci del numero {} es  = 0".format(numero_serie))
        elif numero_serie == 1:
            print("El fibonacci del numero {} es  = 1".format(numero_serie))
        else:
            while contador <= numero_serie:
                print(f"[{contador}]:[{n1}]")
                #print("[{num}] : [{fact}]".format(contador))
                time.sleep(.50)
                fact = n1 + n2
                n1 = n2
                n2 = fact
                contador += 1
            time.sleep(4)

    elif opcion == '2':
        numero = int(
            input("Por favor ingresar el numero para generar la serie : \n"))
        fact = 1
        for num in range(1, numero+1):
            fact *= num
            print(f" [{num}] : [{fact}]")
            time.sleep(.75)
        print(f"El factorial del numero : {numero} es igual = {fact}")
    elif opcion == '3':
        pass #  Slicing de listas
    elif opcion == '4':
        """ Reloj Digital
        """
        contador = 0
        while True:
            hora_actual = time.localtime()
            reloj = time.strftime("%I:%M:%S %p", hora_actual)
            print(reloj, end="", flush=True)
            print("\r", end="", flush=True)
            time.sleep(1)
            contador +=1
            if contador == 60:
                break
            
    elif opcion == 'S':
        break  #Salir del programa
    else:
        print("No existe la opcion")
