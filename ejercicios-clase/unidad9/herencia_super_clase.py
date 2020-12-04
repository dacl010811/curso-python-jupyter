
# Super Clase
class Persona():

    def __init__(self, nombre, apellido, cedula=None):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def __str__(self):
        return (f"OBJETO : {type(self)}:\nNOMBRE:{self.nombre}\nAPELLIDO:{self.apellido}\nCEDULA:{self.cedula}")

    def comer(self):
        return (f"Soy un objeto de tipo {type(self)}, y estoy comiendo")


class Empleado(Persona):

    def __init__(self, institucion, tiempo=0, **kwargs):
        self.institucion = institucion
        self.tiempo = tiempo
        super().__init__(**kwargs)

    def __str__(self):
        super_clase = super().__str__()
        return (f"{super_clase},\nINSTITUCION:{self.institucion}\nTIEMPO:{self.tiempo}\n")

    def timbrar_biometrico(self):
        return "Timbre  en el biometrico"

    def obtener_tiempo_servicio(self):
        return (f"Mi tiempo de servicio en {self.institucion} es de {self.tiempo}")

    def comer(self):
        return (f" Soy un objeto de tipo {type(self)}, y hoy no voy a comer")


class Trabajador(Persona):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def comer(self):
        return (f" Soy un objeto de tipo {type(self)}, no tengo tiempo para almorzar")


if __name__ == "__main__":

    
    # Instanciar o crear un objeto;  Crear objetos
    persona = Persona("Darwin", "Calle", "1104024566")
    print(persona)

    empleado_1 = Empleado(institucion="PETROECUADOR",
                          nombre="NombreA", apellido="ApellidoA")
    print(empleado_1)

    trabajador = Trabajador(nombre="TRabajador1",
                            apellido="Apellido", cedula="19003434343")
    print(trabajador)
