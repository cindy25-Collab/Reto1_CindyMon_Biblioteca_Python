from modelo.libro import Libro
class LibroDAO:
    def cargar_libros(self, archivo):
        libros = []

        next(archivo, None)

        for linea in archivo:
            codigo, titulo, autor, anio, categoria, socio = linea.strip().split(";")
            libros.append(Libro(codigo, titulo, autor, anio, categoria, socio))
        
        return libros

    def guardar_libros(self, libros, archivo):
        
            for libro in libros:
                datos = [libro.codigo, libro.titulo, libro.autor, libro.anio,
                        libro.categoria, libro.socio or ""]
                archivo.write(";".join(datos) + "\n")

    def buscar_libro(self, libros, codigo):
        for libro in libros:
            if libro.codigo == codigo:
                return libro
        return None

    def mostrar_todos(self, libros):
        for libro in libros:
            libro.mostrar()

    def mostrar_disponibles(self, libros):
        libros_disponibles = []

        for libro in libros:
            if libro.disponible():
                libros_disponibles.append(libro.mostrar())
        return libros_disponibles

    def buscar_por_titulo(self, libros, palabra):
        resultados = []
        for libro in libros:
            if palabra.lower() in libro.titulo.lower():
                resultados.append(libro)
        return resultados

    def anadir_libro(self, libros, libro):
        if self.buscar_libro(libros, libro.codigo) is not None:
            return False
        libros.append(libro)
        return True