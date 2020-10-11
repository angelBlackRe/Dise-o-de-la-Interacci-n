# _*_ coding:utf-8 _+_
from sys import exit
class Archivo:
  # contructor
  def __init__(self,nombreArchivo):
    self.nombre = nombreArchivo
    try:
      self.f = open(self.nombre, "r")
    except:
      print("No se puede abrir el archivo ", self.f)
      exit()
      
  # destructor    
  def __del__(self):
    try:
      self.f.close()
    except:
      print("Hasta luego")
      exit()
      
  def muestra(self):
    noLinea = 1
    for línea in self.f:
      s = "{:4}: {}".format(noLinea, línea)
      print(s,end="")
      noLinea += 1
    print()
    self.f.seek(0)
    
  def cuentaVocales(self):
    def vocalesCadena(s):
      cvs = 0
      for i in s:
        if i.lower() in set("aeiouáéíóúü"):
          cvs += 1
      return cvs
        
    contador = 0
    for linea in self.f:
      contador += vocalesCadena(linea)
    self.f.seek(0)
    return contador
      
      