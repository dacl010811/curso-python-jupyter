
class Biblioteca():


    lectores = []    # Atributo de clase
   
    def __init__(self, direccion, recepcion, nombre):
        print("Init")
        self.direccion = direccion
        self.recepcion = recepcion
        self.nombre = nombre
    
    def __str__(self):
        print("str")
        return (f" Direccion: {self.direccion} - Recepcion : {self.recepcion} - Nombre : {self.nombre} ")

    def __del__(self):
        print("del")
        print("Va a eliminar el objeto de la memoria : {}".format(self.nombre))

    def obtener_lectores(self):
        self.lectores = ['Eugenio Espejo','Bolivar']



class Lector:
    libros_prestados = 0
    multa = 0

    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad


class Libro:

    autor = []

    def __init__(self, nombre, tipo, anno, editorial):
        self.nombre = nombre
        self.tipo = tipo
        self.anno = anno
        self.editorial = editorial


class Autor:
    nombre = ""
    nacionalidad = ""
    fecha_nacimiento = ""

    def __init__(self):
        pass


if __name__ == "__main__":

    biblioteca = Biblioteca("Quito", "Python", "Municipal")
    biblioteca.obtener_lectores()
    print("Lectores",biblioteca.lectores)
    print(biblioteca)

    biblioteca1 = Biblioteca("GYE", "HOla", "Municipal Gye")
    print("Lectores",biblioteca1.lectores)
    print(biblioteca1)
