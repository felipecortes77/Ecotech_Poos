import re

from dominio.registrotiempo import RegistroTiempo


class Empleado:
    @staticmethod
    def validar_nombre(nombre: str) -> str:
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto.")
        nombre = nombre.strip()
        if (
            not nombre
            or len(nombre) > 100
            or any(
                not (caracter.isalpha() or caracter in " '-.’")
                for caracter in nombre
            )
        ):
            raise ValueError("Ingrese un nombre válido de hasta 100 caracteres.")
        return nombre

    @staticmethod
    def validar_correo(correo: str) -> str:
        if not isinstance(correo, str):
            raise TypeError("El correo debe ser texto.")
        correo = correo.strip()
        if (
            len(correo) > 150
            or re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo) is None
        ):
            raise ValueError("Ingrese un correo electrónico válido.")
        return correo

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