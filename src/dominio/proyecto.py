class Proyecto:
    def __init__(self, nombre: str, id=None, fecha_inicio: str = None):
        self._id = id
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self._fecha_inicio = valor

    def mostrar_datos(self) -> str:
        return f"ID: {self.id} - {self.nombre} - Inicio: {self.fecha_inicio}"