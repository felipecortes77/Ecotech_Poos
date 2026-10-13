from dominio.registrotiempo import RegistroTiempo


class Empleado:
    def __init__(self, nombre: str, correo: str, id=None, id_departamento=None):
        self._id = id
        self._nombre = nombre
        self._correo = correo
        self._id_departamento = id_departamento
        self._horas_registradas: list[RegistroTiempo] = []

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
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor

    @property
    def id_departamento(self):
        return self._id_departamento

    @id_departamento.setter
    def id_departamento(self, valor):
        self._id_departamento = valor

    @property
    def horas_registradas(self) -> tuple:
        return tuple(self._horas_registradas)

    def mostrar_datos(self) -> str:
        return f"ID: {self.id} - {self.nombre} - {self.correo}"

    def registrar_tiempo(self, tiempo: RegistroTiempo) -> bool:
        self._horas_registradas.append(tiempo)
        return True