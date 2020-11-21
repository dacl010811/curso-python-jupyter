

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


def menu():
    """Presenta el menu principal de las operaciones matematicas.
    """
    while True:
        print("""MENU PRINCIPAL
        1.- Sumar
        2.- Restar
        3.- Multiplicar
        4.- Dividir
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
            pass
        elif opcion == '4':
            pass
        elif opcion == 'S' or opcion == 's':
            caracter = input("Estas seguro de salir del programa : y/n \n")
            if caracter == 'y' or caracter == 'Y':
                break
        else:
            pass


if __name__ == "__main__":
    menu()
