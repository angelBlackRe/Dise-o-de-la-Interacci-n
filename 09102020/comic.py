class Comic:
    def __init__(self, titulo, anio, autor="Anonimo", editorial="Desconocida"):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio = anio

    def muestra(self):
        s = "El libro {} del autor {} , editorial {} y la fecha de emisión {}".format(
            self.titulo, self.autor, self.editorial, self.anio)
        print(80*"-")
        print(s)
