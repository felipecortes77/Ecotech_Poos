class RegistroTiempo:
    def __init__(self,fecha,horas: float):
        self.fecha = fecha
        self.horas = horas
    def mostrar_horas(self) -> str:
        return f"{self.horas} horas en la fecha {self.fecha}"