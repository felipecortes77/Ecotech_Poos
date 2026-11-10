from servicios.permisos import exigir_sesion
from persistencia.registrotiempo_dao import RegistroTiempoDAO
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO


def _exigir_empleado(sesion):
    exigir_sesion(sesion)
    if sesion["rol"] != "empleado":
        raise PermissionError("Esta acción es solo para empleados.")


def obtener_mis_datos(sesion):
    _exigir_empleado(sesion)
    empleado = EmpleadoDAO.buscar_por_id(sesion["empleado_id"])
    if empleado is None:
        raise ValueError("Empleado no encontrado.")
    return empleado


def mis_registros(sesion):
    _exigir_empleado(sesion)
    return RegistroTiempoDAO.listar_por_empleado(
        sesion["empleado_id"]
    )


def actualizar_mis_datos(sesion, nombre, correo):
    _exigir_empleado(sesion)
    nombre = Empleado.validar_nombre(nombre)
    correo = Empleado.validar_correo(correo)
    empleado = obtener_mis_datos(sesion)
    if empleado is None:
        raise ValueError("Empleado no encontrado.")
    empleado.nombre, empleado.correo = nombre, correo
    actualizado = EmpleadoDAO.actualizar(empleado)
    if actualizado:
        sesion["nombre_usuario"] = nombre.lower()
    return actualizado