from BibliotecaUsac.MaterialBiblioteca import MaterialBibioteca


class LibroDigital(MaterialBibioteca):
    def __init__(self, titulo: str, autor: str, pesoMB: float):
        super().__init__(titulo,autor)
        self._pesoMB = pesoMB

    @property
    def pesoMB(self):
        return self._pesoMB

    def obtenerDiasPrestamo(self):
        return 3

    def mostrarInfo(self):
        info = super().mosttrarInfo()
        info += f"Tipo: Digital\nTamaño: {self._pesoMB} \n"
        info += f"Dias de prestamo max: {self.obtenerDiasPrestamo()}\n"
        return info


