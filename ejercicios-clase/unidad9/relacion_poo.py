
class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):  # Definicion del constructor
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)

    # Metodos  Sobre escritos    
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
    
    def __del__(self):
        print("Eliminando")
    
    def __len__(self):
        return self.duracion
    


class Catalogo:
    
    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula
    
    def __init__(self,peliculas=[]):  # Denomina Constructor
        self.peliculas = peliculas

    # Metodos    
    def agregar(self,p):  # p será un objeto Pelicula
        self.peliculas.append(p)
        
    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)

if __name__ == "__main__":
    pass