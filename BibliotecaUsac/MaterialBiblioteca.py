import random
import string
from datetime import datetime,timedelta

class MaterialBibioteca:
    def __init__(self,titulo:str, autor:str):
        self._titulo = titulo
        self._autor = autor
        self._codigo = self._generarCodigo()
        self._estado_prestamo = "disponible"
        self._fecha_prestamo = None
        self._fecha_devuelto = None

    @property
    def titulo(self):
        return self.titulo

    @property
    def autor(self):
        return self.autor

    @property
    def codigo(self):
        return self._codigo
    @property
    def estado_prestamo(self):
        return self._estado_prestamo

    def _generarCodigo(self):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for i in range(8))

    def prestar(self):
        if self._estado_prestamo == "disponible":
            self._estado_prestamo = "No disponible"
            self._fecha_prestamo = datetime.now()
            return True
        return False

    def devolver(self):
        if self._estado_prestamo == "No disponible":
            self._estado_prestamo = "Disponible"
            self._fecha_devuelto = datetime.now()
            return True
        return False

    def dias_restantes(self):
        if self._estado_prestamo != "No disponible" or not self._fecha_prestamo:
            return 0
        dias_prestamo = self._obtenerDiasPrestamo()
        fecha_devuelto = self._fecha_prestamo + timedelta(days=dias_prestamo)

        return (fecha_devuelto - datetime.now()).days

    def _obtenerDiasPrestamo(self):
        raise   NotImplementedError("metodo implementado en las subclases")

    def mosttrarInfo(self):
        info = f"Titulo: {self._titulo}\nAutor: {self._autor}\nCodigo: {self._codigo}"
        info += f"Estado: {self._estado_prestamo}\n"
        if self._fecha_prestamo == "No disponible":
            info += f"Fecha prestamo: {self._fecha_prestamo.strftime ('%Y-%m-%d %H:%M')}\n"
            info += f"dias restantes: {self.dias_restantes()}\n"

            return info

