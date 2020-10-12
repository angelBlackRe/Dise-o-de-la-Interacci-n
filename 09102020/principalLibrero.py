from libro import Libro
from disco import Disco
from revista import Revista
from librero import Librero
from comic import Comic
from manga import Manga
miLibrero = Librero()

miLibrero.agregaLibro(
    Libro(autor="korth", titulo="bases", editorial="Pearson"))
miLibrero.agregaDisco(Disco(interprete="Ricardo Montaner",
                            titulo="Vuelve Conmigo", album="Ida y Vuelta Edición Especial", anio=2017))
miLibrero.agregaDisco(Disco(interprete="Michael Jackson",
                            titulo="Bllie Jean", album="Thriller", anio=1983))
miLibrero.agregaDisco(Disco(interprete="Zara Larsson",
                            titulo="Lush Life", album="So Good", anio=2017))
miLibrero.agregaDisco(Disco(interprete="Hailee Steinfeld",
                            titulo="Love Myself", album="Haiz", anio=2015))
miLibrero.agregaDisco(Disco(interprete="Carly Rae Jepsen",
                            titulo="I Really Like You", album="Emotion", anio=2015))

miLibrero.agregaRevista(Revista(nombreR="Muy interesante", articulosR="Ciencia, Salud, Tecnologia",
                                editorialR="Zinet Media Global", fechaEmision="enero 2020"))
miLibrero.agregarComic(Comic(autor="Gerard Way", titulo="The umbrella academy",
                             anio="2018", editorial="Dark Horse Comics"))

# Manga
miLibrero.agregaManga(Manga(titulo="Suicide boy",autor="ParkGee",numero=57,tomo=2,editorial="Lezhin"))

miLibrero.agregaManga(Manga(autor="Sui ishida", titulo="Tokyo Ghoul: re",numero=20,tomo=1, editorial="Panni"))

miLibrero.agregaManga(Manga(titulo="Platinum end",autor="Tsugumi Ohba",numero=6,tomo=3,editorial="Panni"))

miLibrero.agregaManga(Manga(ittulo="Attack on titan", autor="Hajime Isayama",numero=152,tomo=8, editorial="panni"))

miLibrero.agregaManga(Manga(ittulo="Holic", autor="Anonimo",numero=1,tomo=1, editorial="Clamp"))


miLibrero.muestra()


