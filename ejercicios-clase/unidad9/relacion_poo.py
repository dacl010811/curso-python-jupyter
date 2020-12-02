
class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):  # Definicion del constructor
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        #print('Se ha creado la película:',self.titulo)

    # Metodos  Sobre escritos    
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
    
    """def __del__(self):
        print("Eliminando")"""
    
    def __len__(self):
        return self.duracion
    

class Catalogo:
    
    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula
    
    def __init__(self,peliculas=[]):  # Denomina Constructor
        self.peliculas = peliculas

    def __str__(self):
        return 'Peliculas: {}'.format(self.peliculas)

    # Metodos    
    def agregar(self,pelicula):  # p será un objeto Pelicula
        self.peliculas.append(pelicula)

    # Metodos    
    def eliminar(self,pelicula):  # p será un objeto Pelicula
        if pelicula in self.peliculas:
            self.peliculas.remove(pelicula)
        else:
            print ("La pelicula no se encuentra")
        
    def mostrar(self):
        for p in self.peliculas:
            print("El catalogo tiene : ",p)  # Print toma por defecto str(p)

if __name__ == "__main__":
    
    pelicula_1 = Pelicula("Batman",180,"2020")
    pelicula_2 = Pelicula("Superman",180,"2020")
    pelicula_3 = Pelicula("EndGame",180,"2018")
    pelicula_4 = Pelicula("Larva",180,"2019")

   
    catalogo_1 = Catalogo([pelicula_1])
    print("Catalogo 1: ",catalogo_1)
    
    catalogo_1.agregar(pelicula_2)
    catalogo_1.agregar(pelicula_3)
    catalogo_1.agregar(pelicula_4)

    catalogo_1.mostrar()

    catalogo_1.eliminar(pelicula_4)
    catalogo_1.eliminar(pelicula_3)
    catalogo_1.eliminar(pelicula_2)
    catalogo_1.eliminar(pelicula_1)

    #Forzando eliminar
    catalogo_1.eliminar(pelicula_1)


    print("Resultado :")
    catalogo_1.mostrar()

