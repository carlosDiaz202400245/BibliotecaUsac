class Biblioteca:
    def __init__(self):
        self._materiales = []

    def agregarMaterial(self,material):
        self._materiales.append(material)

    def listarMaterial(self):
        return self._materiales

    def buscarMaterialPorCodigo(self,codigo):
        for material in self._materiales:
            if material.codigo == codigo:
                return material
        return None

    def prestarMaterial(self,codigo):
        material = self.buscarMaterialPorCodigo(codigo)
        if material:
            return material.prestar()
        return False

    def devolverMaterial(self,codigo):
        material = self.buscarMaterialPorCodigo(codigo)
        if material:
            return material.devolver()
        return False



