from dominio.registrotiempo import RegistroTiempo


class Empleado:
    def __init__(self, nombre: str, correo: str, id_departamento: int, id=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.id_departamento = id_departamento
        self.horas_registradas: list[RegistroTiempo] = []

    def mostrar_datos(self) -> str:
        return f"ID: {self.id} - {self.nombre} - {self.correo} - Departamento ID: {self.id_departamento}"

    def registrar_tiempo(self, tiempo: RegistroTiempo) -> bool:
        self.horas_registradas.append(tiempo)
        return True
