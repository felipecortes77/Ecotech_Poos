class RegistroTiempo:
    def __init__(self, fecha: str, horas: float, id_empleado: int = None, id_proyecto: int = None, id: int = None):
        self._id = id
        self._fecha = fecha
        self._horas = horas
        self._id_empleado = id_empleado
        self._id_proyecto = id_proyecto

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        self._horas = valor

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, valor):
        self._id_empleado = valor

    @property
    def id_proyecto(self):
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, valor):
        self._id_proyecto = valor

    def mostrar_horas(self) -> str:
        return f"Registro #{self.id} -> {self.horas} horas trabajadas el {self.fecha} (Empleado: {self.id_empleado}, Proyecto: {self.id_proyecto})"