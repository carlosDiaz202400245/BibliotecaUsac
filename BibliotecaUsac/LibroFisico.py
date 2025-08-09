
from BibliotecaUsac.MaterialBiblioteca import MaterialBibioteca


class LibroFisico(MaterialBibioteca):
    def __init__(self, titulo: str, autor: str, num_ejemplar: int):
        super().__init__(titulo, autor)
        self._num_ejemplar = num_ejemplar

    @property
    def num_ejemplar(self):
        return self._num_ejemplar
    def ObtenerDiasDePrestamo(self):
        return 7
    def mostrarInfo(self):
        info = super().mosttrarInfo()
        info += f"Tipo: libro fisico \nEjemplar: {self._num_ejemplar} \n"
        info += f"dias de prestamo max: {self._obtenerDiasPrestamo()} \n"
        return info

