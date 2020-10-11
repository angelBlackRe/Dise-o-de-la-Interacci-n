class Disco:
    def __init__(self, titulo="", interprete="", album="", anio=""):
        self.titulo = titulo
        self.interprete = interprete
        self.album = album
        self.anio = anio 

    def muestra(self):
        v = "El Disco {} \n Intérprete {} \n Album {} \n Año {}".format(self.titulo, self.interprete, self.album, self.anio)
        print(80*"-")
        print(v)