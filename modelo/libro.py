class Libro:
    def __init__(self, codigo, titulo, autor, anio, categoria, socio=None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.socio = socio

    def disponible(self):
        return self.socio is None

    def mostrar(self):
        estado = self.disponible()
        return self.codigo, "-", self.titulo, "-", self.autor, "-", self.anio, "-", self.categoria, "-", estado