from datetime import datetime
from pathlib import Path

from modelo.libro import Libro
from modelo.socio import Socio
from DAO.libro_DAO import LibroDAO
from DAO.socio_DAO import SocioDAO
from errores.errores_biblioteca import ErrorBiblioteca

# Las rutas se calculan respecto a este archivo, no respecto
# a la carpeta desde la que se ejecute Python.
CARPETA = Path(__file__).resolve().parent
ARCHIVOLIBROS = CARPETA / "libros.txt"
ARCHIVOSOCIOS = CARPETA / "socios.txt"
LOG = CARPETA / "log.txt"

libro_dao = LibroDAO()
socio_dao = SocioDAO()


def guardar_log(evento, detalle):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(LOG, "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}][{evento}][{detalle}]\n")


def prestar_libro(libros, socios):
    codigo_libro = input("Código del libro: ").strip()
    codigo_socio = input("Código del socio: ").strip()

    libro = libro_dao.buscar_libro(libros, codigo_libro)
    socio = socio_dao.buscar_socio(socios, codigo_socio)

    if libro is None:
        return f"El libro con código {codigo_libro} no existe."
    if socio is None:
        return f"El socio con código {codigo_socio} no existe."
    if socio.tiene_libro():
        return f"El socio {socio.nombre} ya tiene un libro prestado."
    if not libro.disponible():
        return f"El libro «{libro.titulo}» ya está prestado."

    libro.socio = socio.codigo
    socio.libro = libro.codigo
    guardar_log("PRESTAMO", f"{libro.titulo} - {socio.nombre}")
    return f"Préstamo realizado: «{libro.titulo}» a {socio.nombre}."


def devolver_libro(libros, socios):
    codigo_socio = input("Código del socio: ").strip()
    socio = socio_dao.buscar_socio(socios, codigo_socio)

    if socio is None:
        return f"El socio con código {codigo_socio} no existe."
    if not socio.tiene_libro():
        return f"El socio {socio.nombre} no tiene ningún libro prestado."

    libro = libro_dao.buscar_libro(libros, socio.libro)
    if libro is None:
        return "No se encuentra el libro asociado al préstamo. Revisa los archivos de datos."

    titulo = libro.titulo
    libro.socio = None
    socio.libro = None
    guardar_log("DEVOLUCION", f"{titulo} - {socio.nombre}")
    return f"Libro «{titulo}» devuelto correctamente por {socio.nombre}."


def obtener_prestamos(libros, socios):
    prestamos = []
    for socio in socios:
        if socio.tiene_libro():
            libro = libro_dao.buscar_libro(libros, socio.libro)
            if libro is not None:
                prestamos.append(f"{socio.nombre} ({socio.codigo}) tiene: «{libro.titulo}» ({libro.codigo})")
    return prestamos


def anadir_elemento(libros, socios):
    print("1. Añadir socio")
    print("2. Añadir libro")
    opcion = input("Elige: ").strip()

    if opcion == "1":
        codigo = input("Código del socio: ").strip()
        nombre = input("Nombre: ").strip()
        email = input("Email: ").strip()
        if not codigo or not nombre or not email:
            return "Todos los campos del socio son obligatorios."
        socio = Socio(codigo, nombre, email)
        if not socio_dao.anadir_socio(socios, socio):
            return "Ese código de socio ya existe."
        guardar_log("ALTA_SOCIO", socio.nombre)
        return f"Socio {socio.nombre} añadido correctamente."

    if opcion == "2":
        codigo = input("Código del libro: ").strip()
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        anio = input("Año: ").strip()
        categoria = input("Categoría: ").strip()
        if not all((codigo, titulo, autor, anio, categoria)):
            return "Todos los campos del libro son obligatorios."
        libro = Libro(codigo, titulo, autor, anio, categoria)
        if not libro_dao.anadir_libro(libros, libro):
            return "Ese código de libro ya existe."
        guardar_log("ALTA_LIBRO", libro.titulo)
        return f"Libro «{libro.titulo}» añadido correctamente."

    return "Opción incorrecta."


def menu():
    print("\n===== BIBLIOTECA =====")
    print("1. Mostrar todos los libros")
    print("2. Mostrar libros disponibles")
    print("3. Buscar libro por título")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar socios con libros prestados")
    print("7. Añadir socio o libro")
    print("8. Guardar y salir")


def cargar_datos():
    # Si los archivos no existen todavía, se crean con sus cabeceras.
    if not ARCHIVOLIBROS.exists():
        ARCHIVOLIBROS.write_text(
            "codigo;titulo;autor;anio;categoria;codigo_socio\n",
            encoding="utf-8"
        )
    if not ARCHIVOSOCIOS.exists():
        ARCHIVOSOCIOS.write_text(
            "codigo_socio;nombre;email;codigo_libro\n",
            encoding="utf-8"
        )

    with open(ARCHIVOLIBROS, "r", encoding="utf-8") as archivo:
        libros = libro_dao.cargar_libros(archivo)
    with open(ARCHIVOSOCIOS, "r", encoding="utf-8") as archivo:
        socios = socio_dao.cargar_socios(archivo)

    # Comprobar que las dos caras de cada préstamo coinciden.
    for socio in socios:
        if socio.libro:
            libro = libro_dao.buscar_libro(libros, socio.libro)
            if libro is None:
                raise ValueError(
                    f"El socio {socio.codigo} referencia el libro inexistente {socio.libro}."
                )
            if libro.socio and libro.socio != socio.codigo:
                raise ValueError(
                    f"El libro {libro.codigo} aparece asignado a dos socios distintos."
                )
            libro.socio = socio.codigo

    for libro in libros:
        if libro.socio:
            socio = socio_dao.buscar_socio(socios, libro.socio)
            if socio is None:
                raise ValueError(
                    f"El libro {libro.codigo} referencia al socio inexistente {libro.socio}."
                )
            if socio.libro and socio.libro != libro.codigo:
                raise ValueError(
                    f"El socio {socio.codigo} aparece con más de un libro."
                )
            socio.libro = libro.codigo

    return libros, socios


def guardar_datos(libros, socios):
    with open(ARCHIVOLIBROS, "w", encoding="utf-8") as archivo:
        libro_dao.guardar_libros(libros, archivo)
    with open(ARCHIVOSOCIOS, "w", encoding="utf-8") as archivo:
        socio_dao.guardar_socios(socios, archivo)


def main():
    try:
        libros, socios = cargar_datos()
    except (OSError, ValueError) as error:
        print(f"No se han podido cargar los datos: {error}")
        return

    print(f"Se han cargado {len(libros)} libros.")
    print(f"Se han cargado {len(socios)} socios.")

    opcion = ""
    while opcion != "8":
        menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            resultados = libro_dao.mostrar_todos(libros)
            if resultados:
                print("\n".join(resultados))
            else:
                print("No hay libros registrados.")

        elif opcion == "2":
            resultados = libro_dao.mostrar_disponibles(libros)
            if resultados:
                print("\n".join(resultados))
            else:
                print("No hay libros disponibles.")

        elif opcion == "3":
            palabra = input("Escribe el título o una parte: ").strip()
            resultados = libro_dao.buscar_por_titulo(libros, palabra)
            if resultados:
                for libro in resultados:
                    print(libro.mostrar())
            else:
                print("No se ha encontrado ningún libro.")

        elif opcion == "4":
            print(prestar_libro(libros, socios))

        elif opcion == "5":
            print(devolver_libro(libros, socios))

        elif opcion == "6":
            resultados = obtener_prestamos(libros, socios)
            if resultados:
                print("\n".join(resultados))
            else:
                print("No hay libros prestados.")

        elif opcion == "7":
            print(anadir_elemento(libros, socios))

        elif opcion == "8":
            try:
                guardar_datos(libros, socios)
                print("Datos guardados. ¡Hasta pronto!")
            except OSError as error:
                print(f"No se pudieron guardar los datos: {error}")
                opcion = ""

        else:
            print("Elige un número del 1 al 8.")


if __name__ == "__main__":
    main()