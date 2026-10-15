from dominio.empleado import Empleado


class Departamento:
    def __init__(self, nombre: str, descripcion: str = "", gerente=None, id=None):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._gerente = gerente
        self._empleados: list[Empleado] = []

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
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    @property
    def gerente(self):
        return self._gerente

    @gerente.setter
    def gerente(self,valor):
        self._gerente = valor

    @property
    def empleados(self) -> tuple:
        return tuple(self._empleados)

    def mostrar_datos(self) -> str:
        return f"ID: {self.id} - Nombre: {self.nombre} - Gerente: {self.gerente}"

    def agregar_empleado(self, empleado: Empleado) -> bool:
        if empleado in self._empleados:
            return False

        self._empleados.append(empleado)
        return True

    def cantidad_empleados(self) -> int:
        return len(self._empleados)