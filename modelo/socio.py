class Socio:
    def __init__(self, codigo, nombre, email, libro=None):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.libro = libro

    def tiene_libro(self):
        return self.libro is None

    def mostrar(self):
        return self.codigo, "-", self.nombre, "-", self.email
