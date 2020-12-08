import sqlite3
from sqlite3 import IntegrityError


def crear_tabla_pk(nombre_tabla):

    conexion = sqlite3.connect('miprimerabdd.db')
    cursor = conexion.cursor()

    ddl = """ CREATE TABLE IF NOT EXISTS {0} (
              CI VARCHAR(13) PRIMARY KEY,
              NOMBRE VARCHAR(100),
              APELLIDO VARCHAR(13),
              EDAD INTEGER,
              EMAIL VARCHAR(50)
    )
    """.format(nombre_tabla)
    cursor.execute(ddl)
    conexion.commit()
    conexion.close()


def insertar_multiple_registros(nombre_table):
    conexion = sqlite3.connect("miprimerabdd.db")
    cursor = conexion.cursor()

    objetos_empleados = [('1104028510', 'DARWIN1', 'CALLE', 30, 'dacl010811@gmail.com'),
                         ('1104028511', 'DARWIN2', 'CALLE',
                          30, 'dacl010812@gmail.com'),
                         ('1104028512', 'DARWIN3', 'CALLE',
                          30, 'dacl010813@gmail.com'),
                         ('1104028513', 'DARWIN4', 'CALLE',
                          30, 'dacl010814@gmail.com'),
                         ('1104028514', 'DARWIN5', 'CALLE', 30, 'dacl010814@gmail.com')]

    dml = "INSERT INTO {0} VALUES (?,?,?,?,?)".format(nombre_table)
    cursor.executemany(dml, objetos_empleados)

    conexion.commit()
    conexion.close()


def crear_tabla_auto_pk(nombre_tabla):

    conexion = sqlite3.connect('miprimerabdd.db')
    cursor = conexion.cursor()
    ddl = """ CREATE TABLE IF NOT EXISTS {0} (
              CODIGO_EMPLEADO INTEGER  PRIMARY KEY AUTOINCREMENT,
              CI VARCHAR(13),
              NOMBRE VARCHAR(100),
              APELLIDO VARCHAR(13),
              EDAD INTEGER,
              EMAIL VARCHAR(50)
    )
    """.format(nombre_tabla)
    cursor.execute(ddl)
    conexion.commit()
    conexion.close()


def insertar_multiple_registros_auto(nombre_table):

    conexion = sqlite3.connect("miprimerabdd.db")
    cursor = conexion.cursor()

    objetos_empleados = [('1104028510', 'DARWIN1', 'CALLE', 30, 'dacl010811@gmail.com'),
                         ('1104028511', 'DARWIN2', 'CALLE',
                          30, 'dacl010812@gmail.com'),
                         ('1104028512', 'DARWIN3', 'CALLE',
                          30, 'dacl010813@gmail.com'),
                         ('1104028513', 'DARWIN4', 'CALLE',
                          30, 'dacl010814@gmail.com'),
                         ('1104028514', 'DARWIN5', 'CALLE', 30, 'dacl010814@gmail.com')]

    dml = "INSERT INTO {0} VALUES (null,?,?,?,?,?)".format(nombre_table)
    cursor.executemany(dml, objetos_empleados)

    conexion.commit()
    conexion.close()


def crear_tabla_auto_pk_unique(nombre_tabla):

    conexion = sqlite3.connect('miprimerabdd.db')
    cursor = conexion.cursor()
    ddl = """ CREATE TABLE IF NOT EXISTS {0} (
              CODIGO_EMPLEADO INTEGER  PRIMARY KEY AUTOINCREMENT,
              CI VARCHAR(13) UNIQUE,
              NOMBRE VARCHAR(100),
              APELLIDO VARCHAR(13),
              EDAD INTEGER,
              EMAIL VARCHAR(50)
    )
    """.format(nombre_tabla)
    cursor.execute(ddl)
    conexion.commit()
    conexion.close()


def insertar_multiple_registros_unique(nombre_table):

    try:
        conexion = sqlite3.connect("miprimerabdd.db")
        cursor = conexion.cursor()

        objetos_empleados = [('1104028515', 'DARWIN1', 'CALLE', 30, 'dacl010811@gmail.com'),
                             ('1104028516', 'DARWIN2', 'CALLE',
                              30, 'dacl010812@gmail.com'),
                             ('1104028517', 'DARWIN3', 'CALLE',
                              30, 'dacl010813@gmail.com'),
                             ('1104028518', 'DARWIN4', 'CALLE',
                              30, 'dacl010814@gmail.com'),
                             ('1104028519', 'DARWIN5', 'CALLE', 30, 'dacl010814@gmail.com')]

        dml = "INSERT INTO {0} VALUES (null,?,?,?,?,?)".format(nombre_table)
        cursor.executemany(dml, objetos_empleados)

    except IntegrityError as sqlerr:
        print(
            f" No se puede insertar registros, control unique : {sqlerr.__class__}")
    except Exception as e:
        print(f" Error general")
    finally:
        conexion.commit()
        conexion.close()


if __name__ == "__main__":
    # crear_tabla_pk('empleado')
    # insertar_multiple_registros('empleado')
    # crear_tabla_auto_pk('empleado_auto')
    # insertar_multiple_registros_auto('empleado_auto')
    # crear_tabla_auto_pk_unique('empleado_unique')

    insertar_multiple_registros_unique('empleado_unique')
