class Libro:
    def __init__(self, codigo, titulo, autor, anio, categoria, socio=None):
        self.codigo = str(codigo)
        self.titulo = titulo
        self.autor = autor
        self.anio = str(anio)
        self.categoria = categoria
        self.socio = socio or None

    def disponible(self):
        return not self.socio

    def mostrar(self):
        estado = "Disponible" if self.disponible() else f"Prestado al socio {self.socio}"
        return (
            f"Código: {self.codigo} | Título: {self.titulo} | Autor: {self.autor} | "
            f"Año: {self.anio} | Categoría: {self.categoria} | Estado: {estado}"
        )