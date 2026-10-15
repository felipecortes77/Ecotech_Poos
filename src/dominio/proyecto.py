class Proyecto:
    def __init__(self, nombre: str, descripcion: str, fecha_inicio: str, fecha_fin: str = None,estado = "pendiente", id=None):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._estado = estado

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
    def descripcion(self,valor):
        self._descripcion = valor

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self,valor):
        self._estado = valor

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self._fecha_inicio = valor

    @property
    def fecha_fin(self):
        return self._fecha_fin
    
    @fecha_fin.setter
    def fecha_fin(self,valor):
        self._fecha_fin = valor

    def mostrar_datos(self) -> str:
        return f"ID: {self.id} - Nombre: {self.nombre} - Descripción: {self.descripcion} - Estado: {self.estado} - Inicio: {self.fecha_inicio} - Fin: {self.fecha_fin}"    
        