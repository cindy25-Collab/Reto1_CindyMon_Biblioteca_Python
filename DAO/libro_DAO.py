from pathlib import Path
from modelo.libro import Libro



class LibroDAO:
    def cargar_libros(archivo):
        libros = []
        for linea in archivo:
            datos = linea.strip().split("|")
            libros.append(Libro(*datos))
        
        return libros

    def guardar_libros(self, libros):
        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            for libro in libros:
                datos = [libro.codigo, libro.titulo, libro.autor, libro.anio,
                        libro.categoria, libro.socio]
                archivo.write("|".join(datos) + "\\n")

    def buscar_libro(self, libros, codigo):
        for libro in libros:
            if libro.codigo == codigo:
                return libro
        return None

    def mostrar_todos(self, libros):
        for libro in libros:
            libro.mostrar()

    def mostrar_disponibles(self, libros):
        for libro in libros:
            if libro.disponible():
                libro.mostrar()

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