from libro import Libro
from disco import Disco
from revista import Revista
from librero import Librero
from comic import Comic
miLibrero = Librero()

miLibrero.agregaLibro(Libro(autor="korth", titulo="bases", editorial="Pearson"))
miLibrero.agregaDisco(Disco(interprete="Ricardo Montaner", titulo="Vuelve Conmigo", album="Ida y Vuelta Edición Especial", anio=2017))
miLibrero.agregaRevista(Revista(nombreR="Muy interesante", articulosR="Ciencia, Salud, Tecnologia", editorialR="Zinet Media Global",fechaEmision="enero 2020"))
miLibrero.agregarComic(Comic(autor="Gerard Way",titulo="The umbrella academy", anio="2018",editorial="Dark Horse Comics"))
#miLibrero.agregaManga(Manga(autor="Sui ishida", titulo="Tokyo Ghoul: re", editorial="panni"))
miLibrero.muestra()

#manga
##from manga import Manga
#sb = Manga("Platinum end", "Panni")
#sb.manwha()
#tg = Manga(titulo="swzSuicide boy",autor="ParkGee",numero="57",tomo="2",editorial="Lezhin")
#tg.manwha()
#miLibrero = Librero()
#miLibrero.agregaManga(sb)
#miLibrero.agregaManga(tg)
#miLibrero.agregaManga(Manga(autor="Sui ishida", titulo="Tokyo Ghoul: re", editorial="panni"))
# Debes crear tu clase MANGA
#miLibrero.manwha()
