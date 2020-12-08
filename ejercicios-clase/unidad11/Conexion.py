import sqlite3
from sqlite3 import Connection


class ConexionDB:

    # Atributo de Conexion global
    __conexion = Connection("")

    def __init__(self, nombre_db, ext="db"):

        self.nombre_db = nombre_db
        self.ext = ext

        if self.nombre_db:
            __conexion = sqlite3.connect("{0}.{1}".format(nombre_db, ext))
            self.cierra_db()
        else:
            print("No se crea la BDD")

    def cierra_db(self):
        if self.__conexion is not None:
            self.__conexion.close()
            print("Cerrando BDD")
        else:
            print("Conexion Nula")

    


if __name__ == "__main__":
    coneccion = ConexionDB("alumnos1")
