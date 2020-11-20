
# crear un conjunto

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos","Darwin"}
administradores = {"Juan", "Marta"}

administradores.discard('Juan')
administradores.add('Marcos')
administradores.add("Darwin")

for usuario in usuarios:
    if usuario in administradores:
        print(f" El usuario {usuario} es administador")
    else:
        print(f" El usuario {usuario} no es administador")
