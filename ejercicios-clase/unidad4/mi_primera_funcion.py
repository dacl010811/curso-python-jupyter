
# Se ha definido variales globales, x : y
iva = 0.12
y = 0

def saludo(nombre):
    """Esta funcion realiza un saludo por consola, dado el nombre del usuario.
    Args:
        nombre (str): Representa el nombre del usuario a saludar.
    """
    print(f"Hola mundo desde una funcion!!!, Bienvenido {nombre}")


def sumar(a, b):
    """Suma 2 numeros dados por el usuario desde consola.
    Args:
        a (float): Sumando 1
        b (float): Sumando 2
    Returns:
        float: Devuelve el resultado de sumar 2 numeros.
    """
    global iva
    iva = 0.16
    return (a+b) * iva


def dibujar_tabla_n(numero_tabla, limite):
    for i in range(1, limite+1):
        print(f"{numero_tabla} * {i} = {numero_tabla*i}")


if __name__ == "__main__":  # Parte principal del programa : Ejecutor del programa

    nombre = input("Cual es tu nombre : \n")
    saludo(nombre)  # Invocar : Se le envia el argumento

    num_1 = float(input("Ingresa el numero 1 : \n"))
    num_2 = float(input("Ingresa el numero 2 : \n"))
    # Invocacion de la funcion y se le envia los argumentos
    resultado = sumar(b=num_1, a=num_2)
    print(f"El resultado de la funcion suma es = {resultado}")
    print(f"Iva global = {iva} ")
    

    # Invocar a la funcion dibujar_table  de cualquier numero
    tabla = int(input("Ingresa el numero de la tabla a construir : \n"))
    limite = int(input("Ingresa el limite hasta donde construir : \n"))
    dibujar_tabla_n(tabla, limite)
