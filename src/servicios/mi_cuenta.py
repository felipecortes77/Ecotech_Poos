from servicios.permisos import exigir_sesion
from persistencia.registrotiempo_dao import RegistroTiempoDAO
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

def mis_registros(sesion):
    exigir_sesion(sesion)
    return RegistroTiempoDAO.listar_por_empleado(
        sesion["empleado_id"]
    )

def actualizar_mis_datos(sesion, nombre, correo):
    exigir_sesion(sesion)
    nombre = Empleado.validar_nombre(nombre)
    correo = Empleado.validar_correo(correo)
    empleado = EmpleadoDAO.buscar_por_id(sesion["empleado_id"])
    if empleado is None:
        raise ValueError("Empleado no encontrado.")
    empleado.nombre, empleado.correo = nombre, correo
    return EmpleadoDAO.actualizar(empleado)