# Proyecto Biblioteca

## ¿Qué es esta aplicación?

Este proyecto es una pequeña aplicación de biblioteca hecha en Python.
Permite guardar información de libros y socios, consultar qué libros hay
disponibles y registrar préstamos y devoluciones.

Los datos se guardan en dos archivos de texto:

-   `libros.txt`: contiene los libros.
-   `socios.txt`: contiene los socios.

## ¿Cómo ejecutar el programa?

1.  Abrir la carpeta del proyecto en el editor de código.

2.  Comprobar que Python está instalado.

3.  Abrir una terminal dentro de la carpeta del proyecto.

4.  Ejecutar:

    ``` bash
    python main.py
    ```

En algunos equipos puede ser necesario escribir `python3 main.py`. La
versión actual no necesita instalar librerías externas.

## ¿Qué se puede hacer ahora?

Desde el menú se puede:

1.  Mostrar todos los libros.
2.  Mostrar los libros disponibles.
3.  Buscar libros por título.
4.  Prestar un libro a un socio.
5.  Registrar la devolución de un libro.
6.  Consultar qué socios tienen libros prestados.
7.  Añadir nuevos socios o libros.
8.  Guardar los cambios y salir.

## Posibles mejoras para el futuro

Estas son ideas para seguir mejorando la aplicación. Se pueden hacer
poco a poco.

### 1. Comprobar mejor los datos

-   Comprobar que el año de publicación sea un número válido.
-   Comprobar que el correo electrónico tenga un formato correcto.
-   Evitar que se añadan libros o socios con campos vacíos.
-   Mostrar mensajes claros cuando un dato no sea correcto.

### 2. Mejorar los préstamos

-   Añadir una fecha límite de devolución.
-   Avisar cuando un libro lleve demasiado tiempo prestado.
-   Permitir que un socio tenga más de un libro prestado, si las normas
    de la biblioteca lo permiten.

### 3. Añadir más búsquedas

-   Buscar libros por autor.
-   Buscar libros por categoría.
-   Buscar socios por nombre o código.
-   Buscar usando solo una parte del título.

### 4. Mejorar el menú

-   Separar las opciones de libros y socios en submenús.
-   Pedir confirmación antes de salir.
-   Mostrar mensajes claros cuando una operación termine correctamente.

### 5. Proteger los datos

-   Crear una copia de seguridad antes de guardar cambios.
-   Comprobar que los archivos tienen el formato correcto.
-   Evitar que un error al guardar deje los archivos vacíos o
    incompletos.
-   Guardar un historial de préstamos y devoluciones.

### 6. Hacer pruebas

-   Probar qué ocurre si se busca un libro que no existe.
-   Comprobar que no se puede prestar un libro que ya está prestado.
-   Comprobar que un socio no recibe otro préstamo si ya tiene uno,
    según las reglas actuales.
-   Comprobar que una devolución deja el libro disponible.
-   Probar qué ocurre si los archivos están vacíos o tienen datos
    incorrectos.

### 7. Mejorar la presentación

-   Mostrar los libros y socios en columnas para facilitar la lectura.


## Organización del proyecto

-   `main.py`: muestra el menú, recibe las opciones y enseña los
    resultados.
-   `DAO/`: contiene las clases que leen, guardan y buscan información.
-   `modelo/`: contiene las clases que representan los libros y los
    socios.
-   `errores/`: contiene clases relacionadas con los errores.
-   `libros.txt`: guarda los datos de los libros.
-   `socios.txt`: guarda los datos de los socios.
-   `log.txt`: guarda un registro de algunas acciones.