from archivos import Archivo

# El archivo lo ponemos en .txt en lugar de .py? para que lea cualquier archivo txt
archivo = Archivo("circulo.py") 
archivo.muestra()
print("EL número de vocales del archivo es: ", archivo.cuentaVocales())
