from modelo.socio import Socio


class SocioDAO:
    def cargar_socios(self, archivo):
        socios = []
        next(archivo, None)  # Saltar la cabecera.

        for numero_linea, linea in enumerate(archivo, start=2):
            linea = linea.rstrip("\r\n")
            if not linea:
                continue
            datos = linea.split(";")
            if len(datos) != 4:
                raise ValueError(f"Formato incorrecto en socios.txt, línea {numero_linea}.")
            codigo, nombre, email, libro = datos
            socios.append(Socio(codigo, nombre, email, libro or None))

        return socios

    def guardar_socios(self, socios, archivo):
        archivo.write("codigo_socio;nombre;email;codigo_libro\n")
        for socio in socios:
            datos = [
                str(socio.codigo), str(socio.nombre), str(socio.email),
                str(socio.libro or "")
            ]
            archivo.write(";".join(datos) + "\n")

    def buscar_socio(self, socios, codigo):
        for socio in socios:
            if socio.codigo == codigo:
                return socio
        return None

    def mostrar_socios(self, socios):
        return [socio.mostrar() for socio in socios]

    def anadir_socio(self, socios, socio):
        if self.buscar_socio(socios, socio.codigo) is not None:
            return False
        socios.append(socio)
        return True