

# Super Clase
class Animal():

    tipo = ''

    def __init__(self):
        pass

    def respirar(self):
        print(" Soy de tipo {}  y  estoy respirando".format(type(self)))

    def comer(self):
        print(" Soy de tipo {}  y estoy comiendo".format(type(self)))

    def dormir(self):
        print(" Soy de tipo {}   y voy a dormir".format(type(self)))

    def __str__(self):
        return " Soy de tipo [{}]".format(type(self))


class Pez(Animal):
    pass


class Perro(Animal):

      def comer(self):
        print("Polimorfismo Perro")


class Gato(Animal):

    def comer(self):
        print("Polimorfismo Gato")


if __name__ == "__main__":

    animal = Animal()
    print("Animal : ", animal)
    animal.respirar()
    
    animal.comer()

    perro = Perro()
    print("Perro : ", perro)
    perro.respirar()
    
    perro.comer()

    pez = Pez()
    print("Pez : ", pez)
    pez.respirar()

    gato = Gato()
    print("Gato : ", gato)
    gato.respirar()
    
    gato.comer()

