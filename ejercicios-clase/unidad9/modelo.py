class Persona():

    def __init__(self, nombre, apellido, cedula):
        """Construye un onjeto de tipo {type(self)}.\n

        Args:
            nombre (str): Nombre empleado.\n
            apellido (str): Apellido empleado.\n
            cedula (str): Cedula empleado.\n
        """
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def __str__(self):
        return (f"Objeto Tipo: {type(self)}]:\nNombre:{self.nombre}, Apellido:{self.apellido}, Cedula: {self.cedula}")


class Empleado(Persona):

    TIPO = 'Publico'

    def __init__(self, institucion, tiempo=0, **kwargs):
        self.institucion = institucion
        self.tiempo = tiempo
        super().__init__(**kwargs)

    def timbrar_biometrico(self, hora):
        return (f"Timbre a las : {hora} ")

    def servicio(self):
        return (f"Tengo  años de servicio en : {self.institucion}")

    def __str__(self):
        super_clase = super().__str__()
        return (f"{super_clase}, Institucion:{self.institucion}, Tiempo_Servicio:{self.tiempo}")


if __name__ == "__main__":

    persona = Persona("Jose", "Marquez", "1900345678")
    print(persona)

    empleado = Empleado(nombre="Darwin",
                        apellido="Calle", cedula="1104028566", institucion="SRI", tiempo=10)
    print(empleado)
