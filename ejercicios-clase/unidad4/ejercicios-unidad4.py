import math


def obtener_lista_numeros(cadena):
    """Valida la entrada de usuario y devuelve una lista de numeros ingresados por teclado.
       Controla espacios en blanco
    Args:
        cadena (str): Entrada de usuario que representa los numeros.
    Returns:
        list: Lista de numeros que fueron extraidos de la entrada de usuario: input()
    """
    # Saca una serie de elementos (numeros) desde la cadena.
    lista_numeros = cadena.split(',') if len(cadena) > 0 else []
    # Controla los espacios en blanco
    lista_numeros = [elemento.strip(' ') for elemento in lista_numeros] if len(
        lista_numeros) > 0 else []

    return lista_numeros if lista_numeros else []


def relacion(num1, num2):
    """[summary]
    Args:
        num1 (float): Primer numero
        num2 (float): Primer numero
    Returns:
        float: Estado 0,1 o -1
    """

    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


def area_rectangulo(ba, al):
    """Calcula el area de un rectangulo.

    Args:
        base (float):  Representa la base del rectangulo.
        altura (float): Representa la altura del rectangulo.

    Returns:
        float: Area del rectangulo
    """
    return (ba*al)


def area_circulo(radio):
    """Calcula el area de un circulo dado el radio.
    Args:
        radio (float): Radio del circulo
    Returns:
        float: El area del circulo
    """
    return (radio**2) * math.pi


def intermedio():
    pass


def separar(lista_numeros):
    """Separar numeros pares e impares
    Args:
        l ([list]): Lista de numeros
    Returns:
        [tupla(list)]: Retorna una tupla de listas
    """

    lista_numeros_pares = []
    lista_numeros_impares = []
    lista_numeros.sort()

    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_numeros_pares.append(numero)
        else:
            lista_numeros_impares.append(numero)

    return lista_numeros_impares, lista_numeros_pares


def calcula_factorial(numero):
    # f (5) =  1 * 2 * 3 * 4 *5
    """Factorial de un numero
    Args:
        numero (float): Numero del cual se genera el factorial : f(num)
    Returns:
        float: Retorna el factual del numero ingresado
    """
    fact = 1.0

    if numero >= 1:
        for e in range(1, numero+1):
            fact *= e
        return fact
    else:
        return 0


def menu():
    """Presenta el menu principal de las operaciones matematicas.
    """
    area = 0.0

    while True:
        print("""MENU PRINCIPAL
        1.- Area del Rectangulo
        2.- Area del Circulo
        3.- Relacion
        4.- Separar
        5.- Factorial
        S.- Salir 
        """)
        opcion = input("Seleccion la operacion a realizar \n")

        if opcion == '1':
            base = float(input("Ingresa la base \n"))
            altura = float(input("Ingresa la altura \n"))
            #area = area_rectangulo(base, altura)
            area = area_rectangulo(al=altura, ba=base)
            print(
                f" El area del rectangulo de :  {base} base * {altura} altura es = {area} ")
        if opcion == '2':
            radio = float(input("Ingresa la radio del circulo \n"))
            area = area_circulo(radio)
            print(
                ' El area del circulo de :  {} es = {:3f} '.format(radio, round(area, 3)))
        if opcion == '3':
            numero_1 = float(input("Ingresa la primer numero \n"))
            numero_2 = float(input("Ingresa el segundo numero \n"))

            resultado = relacion(num2=numero_2, num1=numero_1)

            print(f" {numero_1} > {numero_2} :  El resultado es  {resultado}")

        if opcion == '4':

            entrada_usuario = input(
                " Ingresa los valores separados por una coma \n")

            # Dada la cadena que ingreso el usuario por teclado, extraer los numeros: Lista (str)
            lista_numeros = obtener_lista_numeros(entrada_usuario)

            # Convertir las cadenas de texto que representan los numeros a  enteros : int
            numeros = [int(num)
                       for num in (obtener_lista_numeros(entrada_usuario))]

            # La invocacion a la funcion separar que  retorna 2 listas: pares e impares
            impares, pares = separar(numeros)

            print("La lista de pares es igual : ", pares)
            print("La lista de impares es igual : ", impares)

        elif opcion == '5':
            
            while True:
                entrada_usuario = input("Ingresa el numero para calcular el factorial: \n")      
                if len(entrada_usuario) > 0: 
                    factorial = calcula_factorial(numero=int(entrada_usuario))
                    break

            print(f"El factorial del numero {entrada_usuario} es  = {factorial}")

        elif opcion.upper() == 'S':
            caracter = input("Estas seguro de salir del programa : y/n \n")
            if caracter.lower() == 'y':
                break
        else:
            pass


if __name__ == "__main__":
    menu()
