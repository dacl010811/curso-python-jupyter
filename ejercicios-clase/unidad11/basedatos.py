import sqlite3

# DDL : Sentencias de definicion de datos : Crear Objetos en la BDD: Tablas, vistas, VM, funciones paquetes....etc
# DML : Sentencias de manipulacion de datos : Sirven para manipular los datos :  select, insert, update y delete.


def crear_base_de_datos():
    conexion = sqlite3.connect("miprimerabdd.db")
    conexion.commit()
    conexion.close()


def crear_tabla_bdd(nombre_tabla):
    conexion = sqlite3.connect("miprimerabdd.db")
    cursor = conexion.cursor()

    ddl = "CREATE TABLE {0} (nombre VARCHAR(100), apellido VARCHAR(100), telefono VARCHAR(500), edad INTEGER)".format(
        nombre_tabla)
    cursor.execute(ddl)

    conexion.commit()
    conexion.close()


def insertar_registros_bdd():
    conexion = sqlite3.connect("miprimerabdd.db")
    cursor = conexion.cursor()

    dml = "INSERT INTO alumnos VALUES ('Darwin','Calle','1104028566', 30)"

    cursor.execute(dml)
    conexion.commit()
    conexion.close()


def seleccionar_registros(nombre_tabla):
    conexion = sqlite3.connect("miprimerabdd.db")
    cursor = conexion.cursor()

    dml = "SELECT * from {0}".format(nombre_tabla)
    cursor.execute(dml)
    print(cursor)

    alumno = cursor.fetchone()
    print(type(alumno))
    print(alumno)
    conexion.close()


def insertar_multiple_registros():
    conexion = sqlite3.connect("miprimerabdd.db")
    cursor = conexion.cursor()

    objetos_alumno = [('Pablo', 'G', '1104028566', 30),
                      ('Leo', 'A', '1104028566', 30),
                      ('Rafa', 'B', '1104028566', 30),
                      ('David', 'C', '1104028566', 30),
                      ('Peron', 'D', '1104028566', 30)]
    dml = "INSERT INTO alumnos VALUES (?,?,?,?)"
    cursor.executemany(dml, objetos_alumno)

    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    crear_base_de_datos()
    # crear_tabla_bdd("alumnos")
    insertar_registros_bdd()
    seleccionar_registros('alumnos')
    insertar_multiple_registros()
