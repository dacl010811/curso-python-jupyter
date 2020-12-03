class Persona():

    def __init__(self, nombre, apellido, cedula, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        super().__init__(**kwargs)


    def __str__(self):
        return (f""" 
         Nombre : {self.nombre}\n
         Apellido : {self.nombre}\n 
         Cedula : {self.cedula}\n    
        """)


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


if __name__ == "__main__":
    empleado = Empleado("SRI", 10 ,nombre="Darwin",
                        apellido="Calle", cedula="1104028566")
    print(empleado.nombre)
    print(empleado.apellido)
    print(empleado.cedula)
    print(empleado.institucion)
    print(empleado.tiempo)
