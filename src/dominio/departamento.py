from dominio.empleado import Empleado


class Departamento:
    def __init__(self, nombre: str, id=None):
        self.id = id
        self.nombre = nombre
        self._empleados: list[Empleado] = []

    def mostrar_datos(self) -> str:
        return f"ID: {self.id} - {self.nombre}"

    def agregar_empleado(self, empleado: Empleado) -> bool:
        if empleado in self._empleados:
            return False

        self._empleados.append(empleado)
        return True

    @property
    def empleados(self) -> tuple:
        return tuple(self._empleados)

    def cantidad_empleados(self) -> int:
        return len(self._empleados)