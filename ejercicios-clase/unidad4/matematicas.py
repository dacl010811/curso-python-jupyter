import time

resultado = 0.0


def suma(*args):
    """Funcion que realiza la suma de n numeros
    Returns:
        float: Sumatoria de n numeros
    """
    global resultado
    if args:
        for num in args:
            print('[', num, ']')
            time.sleep(.50)
            resultado += float(num)
    else:
        print("No hay nada")

    return resultado


if __name__ == "__main__":
    entrada_usuario = input(
        "Ingresa los valores a sumar separados por comas : \n")

    lista_numeros = entrada_usuario.split(
        ',') if len(entrada_usuario) > 0 else []
    lista_numeros = [e.strip(' ') for e in lista_numeros] if len(
        lista_numeros) > 0 else []
    resultado = suma(*lista_numeros) if len(lista_numeros) > 0 else 0
    print(f"El resultado de la suma es : {lista_numeros} es = : {resultado}") if resultado > 0 else print(
        "No hay datos")
