from io import open
import time

def crear_fichero():
    """Crear un archivo en python
    """
    texto = "Nueva linea1"
    fichero = open('Miprimerarchivo.txt', 'w')
    fichero.write(texto)
    fichero.close()


def leer_fichero():
    fichero = open('Miprimerarchivo.txt', 'r')
    contenido = fichero.read()
    fichero.close
    print(contenido)


def escribir_final_fichero():
    fichero = open('archivo.txt', 'a')
    fichero.write("Nueva Linea X\n")
    fichero.close


def leer_fichero_linea_a_linea():
    fichero = open('archivo.txt', 'r')
    contenido = fichero.readline()
    print(contenido)
    contenido = fichero.readline()
    print(contenido)
    fichero.close

def leer_fichero_linea_a_linea_with():
    contador = 0
    with open('archivo.txt', 'r') as fichero:
        for linea in fichero:
            print(f"[{contador}]:", linea)
            time.sleep(1)
            contador +=1

def lectura_escritura_a_la_vez():
    fichero = open('archivo.txt', 'r+')   # Este tipo de modo debemos apoyarnos del puntero
    contenido = "Python\nHola\nMundo\n"
    fichero.write(contenido)
    fichero.close()

def leer_archivo_puntero():
    fichero = open('archivo.txt', 'r')
    fichero.seek(0)               # seek (0)
    contenido = fichero.read(14) 
    contenido_1 = fichero.read(14) # seek (14)
    print(contenido)
    print(contenido_1)


def leer_archivo_actualizar_linea():
    fichero = open('archivo.txt', 'r+')
    contenido = fichero.readlines()  # Lista de cadenas
    print(type(contenido))
    for indice,linea in enumerate(contenido):
        print("L",linea)
        if indice == 0 : 
            contenido [indice] = "Xime\n"
        time.sleep(0.25)

    print(contenido)   
    fichero.seek(0)
    fichero.writelines(contenido)
    fichero.close()




if __name__ == "__main__":
    # crear_fichero()
    # leer_fichero()
    #escribir_final_fichero()
    #leer_fichero_linea_a_linea()
    #leer_fichero_linea_a_linea_with()
    #lectura_escritura_a_la_vez()
    #leer_archivo_puntero()
    leer_archivo_actualizar_linea()
