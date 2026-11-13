from modelo.libro import Libro


class LibroDAO:
    def cargar_libros(self, archivo):
        libros = []
        next(archivo, None)  # Saltar la cabecera.

        for numero_linea, linea in enumerate(archivo, start=2):
            linea = linea.rstrip("\r\n")
            if not linea:
                continue
            datos = linea.split(";")
            if len(datos) != 6:
                raise ValueError(f"Formato incorrecto en libros.txt, línea {numero_linea}.")
            codigo, titulo, autor, anio, categoria, socio = datos
            libros.append(Libro(codigo, titulo, autor, anio, categoria, socio or None))

        return libros

    def guardar_libros(self, libros, archivo):
        archivo.write("codigo;titulo;autor;anio;categoria;codigo_socio\n")
        for libro in libros:
            datos = [
                str(libro.codigo), str(libro.titulo), str(libro.autor),
                str(libro.anio), str(libro.categoria), str(libro.socio or "")
            ]
            archivo.write(";".join(datos) + "\n")

    def buscar_libro(self, libros, codigo):
        for libro in libros:
            if libro.codigo == codigo:
                return libro
        return None

    def mostrar_todos(self, libros):
        # El DAO prepara los resultados; main.py es quien los muestra.
        return [libro.mostrar() for libro in libros]

    def mostrar_disponibles(self, libros):
        return [libro.mostrar() for libro in libros if libro.disponible()]

    def buscar_por_titulo(self, libros, palabra):
        palabra = palabra.casefold()
        return [
            libro for libro in libros
            if palabra in libro.titulo.casefold()
        ]

    def anadir_libro(self, libros, libro):
        if self.buscar_libro(libros, libro.codigo) is not None:
            return False
        libros.append(libro)
        return True