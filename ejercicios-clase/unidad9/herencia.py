class Producto:


    def __init__(self, referencia, tipo, nombre, pvp, descripcion, provincia, productor=None, distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia  # Creando un atributo de Instancia   *args  **kwargs
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor
        self.provincia = provincia

    def __str__(self):
        return " {}  : {} - {}".format(type(self), self.nombre, self.tipo)


class Adorno(Producto):
    pass


class Libro(Producto):
    pass


class Articulo(Producto):
    pass


if __name__ == "__main__":
    producto = Producto('000A', 'ADORNO', 'Vaso Adornado', 15,
                        'Vaso de porcelana con dibujos', "Quito", productor="Productor1",)
    print(producto)

    adorno = Adorno('000A', 'ADORNO2', 'Vaso Adornado2', 30,
                    'Vasos', "Quito")
    print(adorno)

    libro = Libro('000A', 'ADORNO', 'Vaso Adornado', 15,
                  'Vaso de porcelana con dibujos', "Quito", productor="Productor1", distribuidor="Distribuidor 1")
    print(libro)

    articulo = Articulo('000A', 'ARticulo', 'Vaso Adornado', 15,
                        'Vaso de porcelana con dibujos', "Quito", productor="Productor", distribuidor="Dis1", isbn="YYYYY", autor="Darwin")
    print(articulo)

    articulo1 = Articulo('000A', 'ARticulo', 'Vaso Adornado', 15,
                        'Vaso de porcelana con dibujos', "Quito", autor="Darwin")
    print(articulo1)
