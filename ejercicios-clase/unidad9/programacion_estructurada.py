# Definimos unos cuantos clientes
clientes = [
    {'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '1900474097'},
    {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}
]

# Creamos una función que muestra un cliente en una lista a partir del DNI

def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            return
    print('Cliente no encontrado')

# Creamos una función que borra un cliente en una lista a partir del DNI


def borrar_cliente(clientes, dni):
    for i, c in enumerate(clientes):
        if (dni == c['dni']):
            del(clientes[i])
            print(str(c), "> BORRADO")
            return

    print('Cliente no encontrado')

#  código estructurado

if __name__ == "__main__":

    print("==LISTADO DE CLIENTES==")
    print(clientes)

    print("\n==MOSTRAR CLIENTES POR DNI==")
    mostrar_cliente(clientes, '11111111A')
    mostrar_cliente(clientes, '11111111Z')

    print("\n==BORRAR CLIENTES POR DNI==")
    borrar_cliente(clientes, '22222222V')
    borrar_cliente(clientes, '22222222B')

    print("\n==LISTADO DE CLIENTES==")
    print(clientes)
