class Socio:
    def __init__(self, codigo, nombre, email, libro=None):
        self.codigo = str(codigo)
        self.nombre = nombre
        self.email = email
        self.libro = libro or None

    def tiene_libro(self):
        return bool(self.libro)

    def mostrar(self):
        prestamo = self.libro if self.libro else "Sin libros prestados"
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Email: {self.email} | Libro: {prestamo}"
        )