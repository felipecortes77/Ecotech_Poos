class RegistroTiempo:
    def __init__(self, fecha: str, horas: float, id_empleado: int = None, id_proyecto: int = None, id: int = None):
        self.id = id
        self.fecha = fecha
        self.horas = horas
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

    def mostrar_horas(self) -> str:
        return f"Registro #{self.id} -> {self.horas} horas trabajadas el {self.fecha} (Empleado: {self.id_empleado}, Proyecto: {self.id_proyecto})"
