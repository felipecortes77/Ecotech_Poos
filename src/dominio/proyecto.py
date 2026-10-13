class Proyecto:
    def __init__(self, nombre: str, id=None, fecha_inicio: str = None):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio

    def mostrar_datos(self) -> str:
        return f"ID: {self.id} - {self.nombre} - Inicio: {self.fecha_inicio}"
