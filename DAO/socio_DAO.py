from pathlib import Path
from modelo.socio import Socio



class SocioDAO:
    def cargar_socios(self, archivo):
        socios = []

        next(archivo, None)

        for linea in archivo:
            codigo, nombre, email, libro = linea.strip().split(";")
            socios.append(Socio(codigo, nombre, email, libro))

        return socios

    def guardar_socios(self, socios, archivo):
        
            for socio in socios:
                datos = [socio.codigo, socio.nombre, socio.email, socio.libro or ""]
                archivo.write(";".join(datos) + "\n")

    def buscar_socio(self, socios, codigo):
        for socio in socios:
            if socio.codigo == codigo:
                return socio
        return None

    def mostrar_socios(self, socios):
        for socio in socios:
            socio.mostrar()

    def anadir_socio(self, socios, socio):
        if self.buscar_socio(socios, socio.codigo) is not None:
            return False
        socios.append(socio)
        return True