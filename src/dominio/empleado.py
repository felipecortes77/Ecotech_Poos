from dominio.registrotiempo import RegistroTiempo

class Empleado:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.horas_registradas :list[RegistroTiempo] = []

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.correo}"

    def registrar_tiempo(self,tiempo: RegistroTiempo):
        self.horas_registradas.append(tiempo)
        return True
