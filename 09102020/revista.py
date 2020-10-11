#clase para el objeto revista 
class Revista():
    def __init__(self,nombreR,articulosR,editorialR,fechaEmision):
        #constructor
        self.nombreR = nombreR
        self.articulosR = articulosR
        self.editorialR = editorialR
        self.fechaEmision = fechaEmision
    
    #metodo

    def muestra(self):
        print(80*"-")
        print("Revista: " + self.nombreR)
        print("Editorial: " + self.editorialR)
        print("Contiene articulos de: " + self.articulosR)
        print("Fecha de emisión: " + self.fechaEmision)
