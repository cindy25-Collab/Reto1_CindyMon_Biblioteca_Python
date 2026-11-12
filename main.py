from modelo.libro import Libro
from modelo.socio import Socio
from DAO.libro_DAO import LibroDAO
from DAO.socio_DAO import SocioDAO
from errores.errores_biblioteca import ErrorBiblioteca
from datetime import datetime
from pathlib import Path

ARCHIVO = Path(__file__).parent.name / "libros.txt"
ARCHIVO = Path(__file__).parent.name / "socios.txt"
LOG = Path(__file__).parent / "log.txt"
libro_dao = LibroDAO()
socio_dao = SocioDAO()

def guardar_log(evento, detalle):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(LOG, "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}][{evento}][{detalle}]\\n")

def prestar_libro(libros, socios):
    codigo_libro = input("Código del libro: ")
    codigo_socio = input("Código del socio: ")
    try:
        libro = libro_dao.buscar_libro(libros, codigo_libro)
        socio = socio_dao.buscar_socio(socios, codigo_socio)
        if libro is None:
            raise ErrorBiblioteca("El libro no existe", codigo_libro)
        if socio is None:
            raise ErrorBiblioteca("El socio no existe", codigo_socio)
        if socio.tiene_libro():
            raise ErrorBiblioteca("El socio ya tiene un libro", codigo_socio)
        if not libro.disponible():
            raise ErrorBiblioteca("El libro ya está prestado", codigo_libro)
        libro.socio = socio.codigo
        socio.libro = libro.codigo
        guardar_log("PRESTAMO", libro.titulo + " - " + socio.nombre)
        print("Préstamo realizado correctamente.")
    except ErrorBiblioteca as error:
        print(error.mensaje, "- Código:", error.codigo)

def devolver_libro(libros, socios):
    codigo = input("Código del socio: ")
    try:
        socio = socio_dao.buscar_socio(socios, codigo)
        if socio is None:
            raise ErrorBiblioteca("El socio no existe", codigo)
        if not socio.tiene_libro():
            raise ErrorBiblioteca("El socio no tiene ningún libro", codigo)
        libro = libro_dao.buscar_libro(libros, socio.libro)
        if libro is None:
            raise ErrorBiblioteca("No se encuentra el libro", socio.libro)
        libro.socio = ""
        socio.libro = ""
        guardar_log("DEVOLUCION", libro.titulo + " - " + socio.nombre)
        print("Libro devuelto correctamente.")
    except ErrorBiblioteca as error:
        print(error.mensaje, "- Código:", error.codigo)

def mostrar_prestamos(libros, socios):
    hay_prestamos = False
    for socio in socios:
        if socio.tiene_libro():
            libro = libro_dao.buscar_libro(libros, socio.libro)
            if libro is not None:
                print(socio.nombre, "tiene:", libro.titulo)
                hay_prestamos = True
    if not hay_prestamos:
        print("No hay libros prestados.")

def anadir_elemento(libros, socios):
    print("1. Añadir socio")
    print("2. Añadir libro")
    opcion = input("Elige: ")
    if opcion == "1":
        codigo = input("Código del socio: ")
        socio = Socio(codigo, input("Nombre: "), input("Email: "))
        if socio_dao.anadir_socio(socios, socio):
            guardar_log("ALTA_SOCIO", socio.nombre)
            print("Socio añadido.")
        else:
            print("Ese código ya existe.")
    elif opcion == "2":
        codigo = input("Código del libro: ")
        libro = Libro(codigo, input("Título: "), input("Autor: "),
                    input("Año: "), input("Categoría: "))
        if libro_dao.anadir_libro(libros, libro):
            guardar_log("ALTA_LIBRO", libro.titulo)
            print("Libro añadido.")
        else:
            print("Ese código ya existe.")
    else:
        print("Opción incorrecta.")

def menu():
    print("\\n===== BIBLIOTECA =====")
    print("1. Mostrar todos los libros")
    print("2. Mostrar libros disponibles")
    print("3. Buscar libro por título")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar socios con libros prestados")
    print("7. Añadir socio o libro")
    print("8. Guardar y salir")

class main:

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        libros = libro_dao.cargar_libros(ARCHIVO)
    print("Se han cargado", len(libros), "libros.")

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        socios = socio_dao.cargar_socios()
    print("Se han cargado", len(socios), "socios.")
    
    opcion = ""
    while opcion != "8":
        menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            libro_dao.mostrar_todos(libros)
        elif opcion == "2":
            libro_dao.mostrar_disponibles(libros)
        elif opcion == "3":
            palabra = input("Escribe el título o una parte: ")
            resultados = libro_dao.buscar_por_titulo(libros, palabra)
            if len(resultados) == 0:
                print("No se ha encontrado ningún libro.")
            else:
                for libro in resultados:
                    libro.mostrar()
        elif opcion == "4":
            prestar_libro(libros, socios)
        elif opcion == "5":
            devolver_libro(libros, socios)
        elif opcion == "6":
            mostrar_prestamos(libros, socios)
        elif opcion == "7":
            anadir_elemento(libros, socios)
        elif opcion == "8":
            libro_dao.guardar_libros(libros)
            socio_dao.guardar_socios(socios)
            print("Datos guardados. ¡Hasta pronto!")
        else:
            print("Elige un número del 1 al 8.")