import pickle


def guardar_en_binario(nombre_archivo, dato):
    #dato = [1, 2, 3, 4]
    fichero = open(nombre_archivo, "wb")
    pickle.dump(dato, fichero)
    fichero.close()


def leer_archivo_binario():
    fichero = open("fichero_binario.txt", "rb")
    lista_original = pickle.load(fichero)
    print(lista_original)


def suma_binario(lista):
    suma = 0
    for numero in lista:
        print(numero)
        suma += numero

    print("R:", suma)
    return suma


if __name__ == "__main__":
    # guardar_en_binario()
    # leer_archivo_binario()

    guardar_en_binario('suma.dat', suma_binario([1, 2, 3, 4]))


# Input :   1 2 3 4 5  6 7 8 8
# lista = [1, 2 ,3 4 5  6 7 8 8]
# suma(1 2 3 4 5  6 7 8 8) #args
# suma(lista)
