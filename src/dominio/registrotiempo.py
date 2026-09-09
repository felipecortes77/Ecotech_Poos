class RegistroTiempo:
    def __init__(self,fecha,horas: float):
        self.fecha = fecha
        self.horas = horas
    def mostrar_horas(self) -> str:
        return f"En la fecha {self.fecha} se trabajaron {self.horas} horas"