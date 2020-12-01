

class Galleta:
    chocolate = False  # Atributos de clase pueden ser cambiados dinamicamente sin instanciar

    def __init__(self, sabor, forma):
        self.sabor = sabor   # Representa atributo de instancia
        self.forma = forma

    def costo(self):
        pass


if __name__ == "__main__":

    Galleta.chocolate = True  # Cambiar los atributos de clase de forma dinamica
    galleta_1 = Galleta("Chocolate","Circular")  # Crear un objeto de tipo galleta o instanciar

    print(f"Atributos galleta 1 : color : [{galleta_1.forma}]")
    print(f"Atributos galleta 1: sabor : [{galleta_1.sabor}]")
    print(f"Atributos galleta 1: chocolate : [{galleta_1.chocolate}]")

    galleta_2 = Galleta("Vainilla","Triangular")
    print(f"Atributos galleta 2: sabor : [{galleta_2.sabor}]")
    print(f"Atributos galleta 2: forma : [{galleta_2.forma}]")

    Galleta.sabor = "Naranja"  # Cambiar los atributos de clase de forma dinamica

    galleta_3 = Galleta("Fresa","Cuadrada")
    galleta_3.sabor = "Caramelo"  # definimos atributos del objeto
    print(f"Atributos galleta 3: sabor : [{galleta_3.sabor}]")
    print(f"Atributos galleta 3: forma : [{galleta_3.forma}]")

    galleta_4 = Galleta("Fresaxyz","Cuadradaxyz")
    print(f"Atributos galleta 4: sabor : [{galleta_4.sabor}]")
