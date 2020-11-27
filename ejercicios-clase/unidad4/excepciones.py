

def division(dv, dvs):
    """Division
    Args:
        dv (float): Dividendo
        dvs (float): Divisor
    Returns:
        float: Cociente
    """
    res = 0.0
    mensaje = ""

    try:
        res = dv/dvs
    except ZeroDivisionError as ze:
        print("ZeroDivisionError :", ze.__class__)
        mensaje = "La division por cero no es permitida"
    except Exception as e:
        print("Exception : ", e.__class__)
    else:
        print("La division se realizo correctamente")

    return res, mensaje


def verifica_elemento_lista(*args, indice=0):

    dato = -1
    existe = 0

    try:
        if args:
            for index, el in enumerate(args):
                print(f" [{index}] [{el}] ")
                dato = args[indice]
                if not dato is None:
                    existe = 1
        else:
            print(f" No hay datos en la lista {args}")
    except IndexError as ie:
        print(f" [{type(ie)}]: El elemento con el indice: {indice} no existe en la lista.")
    except Exception as e:
        print(f"Excepcion general del programa", e.__class__)
    
    return dato, existe
    

def diccionario():

    llave = 'blanco'

    try:
        colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
        dato = colores[llave]
        print("El dato es : ", dato)
    except KeyError as ke:
        print("La llave  ingresa del diccionario no existe. Error: ", ke.__class__)
    except Exception as e:
        print("Excepcion Global", e.__class__)
    else:
        print(f"El dato con la llave {llave} correcta")
    finally:
        print("Este bloque se ejecuta siempre")


def agregar_una_vez(lista, elemento):

    try:
        if elemento in lista:
            raise ValueError
        else:
            lista.append(elemento)
    except ValueError as ve:
        print(
            f"Error: Imposible añadir elementos duplicados => [{elemento}].", ve.__class__)
    except Exception as e:
        print("Excepcion Genral ", e.__class__)
    else:
        " Pasa por aqui cuando se ejecuta correctamente la logica"
    finally:
        print("Siempre se ejecuta esto........")


if __name__ == "__main__":

    lista = [1, 5, -2]

    """elemento = 7
    agregar_una_vez(lista,10)
    agregar_una_vez(lista,8)
    agregar_una_vez(lista,12)
    print(lista)"""

    index = 200
    dato, existe = verifica_elemento_lista(*lista,indice=index)
    print(f"El dato con el indice = {index} es = {dato} ") if existe != 0 else print(
        "Lo sentimos no existe el elemento")
