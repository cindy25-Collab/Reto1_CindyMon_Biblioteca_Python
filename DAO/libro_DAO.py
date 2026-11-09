libros = []

def lista_libros(archivo):
    for linea in archivo:
        codigo, titulo, autor, anio, categoria = linea.strip().split("|")
        if anio > 0:
            libros.append(codigo, titulo, autor, anio, categoria)

    return libros

def esta_dosponible(Libro):
        if Libro.codigo_socio is not None:
            return Libro.codigo_socio
        else:
            return Libro.codigo_socio is None

def buscar_libro(titulo):
    for libro in  libros:
        if titulo == libro.titulo.lower():
            if esta_dosponible(libro):
                return libro

def prestar_libro(codigo_libro, codigo_socio):
    for libro in libros:
        if codigo_libro == libro.codigo_libro.lower():
            libro.codigo_socio = codigo_socio

def devolver_libro(codigo_libro):
    for libro in libros:
        if codigo_libro == libro.codigo_libro.lower():
            libro.codigo_socio = None

def agregar_libro(Libro):
    if Libro is not libros:
        libros.append(Libro)