class Libro:
  def __init__(self,titulo,autor="Anonimo",editorial="Desconocida"):
    self.titulo = titulo
    self.autor = autor
    self.editorial = editorial
    
  def muestra(self):
    s = "El libro {} del autor {} y editorial {}".format(self.titulo,self.autor,self.editorial)
    print(80*"-")
    print(s)
    