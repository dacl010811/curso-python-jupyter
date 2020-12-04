

class Mamifero():

    def __init__(self, sangre, huesos, pelaje, pulmones):
        self.sangre = sangre
        self.huesos = huesos
        self.pelaje = pelaje
        self.pulmones = pulmones

    def respirar(self):
        return f"Soy un {type(self)}"

    def __str__(self):
        return (f",{type(self)}:\nSANGRE:{self.sangre}\nHUESOS:{self.huesos}\nPELAJE:{self.pelaje}\nPULMONES:{self.sangre}")

    def dormirM(self):
        return "Estoy durmiendo: Clase  Mamifero"


class Persona(Mamifero):

    def __init__(self, nombre=None, apellido=None, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__(**kwargs)

    def dormirP(self):
        return "Estoy durmiendo: Clase Persona"

    def __str__(self):
        return (f"{type(self)}:\nNOMBRE:{nombre}\nAPELLIDO{apellido}")


class Perro(Mamifero):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Gato(Mamifero):

    def __init__(self, agil=None, **kwargs):
        self.agil = agil
        super().__init__(**kwargs)

    def agil(self):
        return "Soy agil"


class Empleado(Persona, Mamifero):  # Herencia multiple en python

    def __init__(self, institucion=None):
        self.institucion = institucion

    def __str__(self):
        cadena_mamifero = super(Mamifero).__str__()
        cadena_persona = super(Persona).__str__()
        return (f",{type(self)}:\n{cadena_mamifero}{cadena_persona}\nINSTITUCION:{self.institucion}")


if __name__ == "__main__":

    empleado = Empleado("MUNICIPIO")
    print(empleado)
    print(f" Soy un objeto de tipo empleado : {empleado.dormirM()}")
    print(f" Soy un objeto de tipo empleado : {empleado.respirar()}")

    gato = Gato(sangre='O+', huesos='SI',
                pelaje='SI', pulmones='SI')
    print(gato)
    print(f"Gato : [{gato.agil},{gato.sangre},{gato.huesos}]")

    perro = Perro(sangre='O-', huesos='NO',
                  pelaje='SI', pulmones='SI')
    print(f"Perro : [{perro.sangre},{perro.huesos}]")
    print(perro)
