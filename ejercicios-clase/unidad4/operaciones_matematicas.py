
resultado = 0.0  # Variable Global


def suma(sumando_1, sumando_2):
    """Sumar 2 numeros.
    Args:
        sumando_1 (float): Sumando 1.
        sumando_2 (float): Sumando 2.
    Returns:
        float: Suma total.
    """
    return sumando_1 + sumando_2


def restar(num1, num2):
    """Restar 2 numeros.
    Args:
        num1 (float): Valor 1.
        num2 (float): Valor 2.
    Returns:
        float: resultado.
    """
    return num1 - num2


def suma_n_numeros(*args):
    global resultado

    if args:  # Verificar elemetos en una lista
        for num in args:
            print(f"Elemento : [{num}], y es un {type(num)} ")
            resultado += float(num)
    else:
        print("La lista no tiene elementos")

    return resultado


def multiplicar(multiplicando, multiplicador):
    """Multiplica numeros
    Args:
        multiplicando (float):  Dato 1
        multiplicar (float): Dato 2
    Returns:
        float: Producto total
    """
    producto_total = multiplicando*multiplicador

    mensaje = ''
    if producto_total >= 100:
        mensaje = '3 cifras'
    else:
        mensaje = '2 cifras'

    return producto_total, mensaje


def menu():
    """Presenta el menu principal de las operaciones matematicas.
    """
    while True:
        print("""MENU PRINCIPAL
        1.- Sumar
        2.- Restar
        3.- Multiplicar
        4.- Dividir
        5.- Suma-Ideterminados-Posicion
        S.- Salir 
        """)
        opcion = input("Seleccion la operacion a realizar \n")
        if opcion == '1':
            print(20*"-", "SUMA", 20*"-")
            sumando_1 = float(input("Ingrese el primer numero: \n"))
            sumando_2 = float(input("Ingrese el segundo numero: \n"))
            resultado = suma(sumando_1, sumando_2)  # Invocacion
            print(
                f"El resultado de sumar: {sumando_1} + {sumando_2} = {resultado}\n")
        elif opcion == '2':
            print(20*"-", "RESTA", 20*"-")
            num_1 = float(input("Ingrese el primer numero: \n"))
            num_2 = float(input("Ingrese el segundo numero: \n"))
            resultado = restar(num_1, num_2)  # Invocacion
            print(f"El resultado de restar: {num_1} - {num_2} = {resultado}\n")
        elif opcion == '3':
            mul_1 = float(input("Ingrese  el dato 1 \n"))
            mul_2 = float(input("Ingrese  el dato 2 \n"))
            producto_total, mensaje = multiplicar(mul_1, mul_2)
            print(
                f"El producto total es = {producto_total} y la operacion es de {mensaje}")
        elif opcion == '4':
            pass
        elif opcion == '5':
            #lista_valores = [1, 2, 3, 4, 5, '6', 1.2, 'Hola']
            entrada_usuario = input(
                "Ingrese los valores a sumar separados por comas: \n")
            print(entrada_usuario)    
            lista_numeros = entrada_usuario.split(
                ',') if len(entrada_usuario) > 0 else []
            print("L1",lista_numeros)    
            lista_numeros = [elemento.strip(' ') for elemento in lista_numeros] if len(
                lista_numeros) > 0 else []
            print("L2",lista_numeros)    
            producto_total = suma_n_numeros(*lista_numeros)
            print(
                f"El resultado de sumar n = {lista_numeros} es  = {producto_total} ")

        elif opcion == 'S' or opcion == 's':
            caracter = input("Estas seguro de salir del programa : y/n \n")
            if caracter == 'y' or caracter == 'Y':
                break
        else:
            pass


if __name__ == "__main__":
    menu()
