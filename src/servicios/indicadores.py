from servicios.permisos import exigir_sesion
from servicios.deserializador_indicador import DeserializadorIndicador
from servicios.revisar_api import obtener_datos
from persistencia.indicador_dao import IndicadorDAO

def consultar_indicador(sesion):
    exigir_sesion(sesion)
    try:
        datos = obtener_datos()
        dato = DeserializadorIndicador.desde_api(datos)
    except (requests.exceptions.RequestException, ValueError, KeyError, TypeError):
        return buscar_respaldo()
        # Intentar guardar. Si falla la BD, informar ese fallo.
        # Devolver dato, origen y mensaje para que el menú muestre.

def obtener_historial(sesion):
    exigir_sesion(sesion)
    return IndicadorDAO.listar()
    # En el menú, dentro de su manejo de errores:

#ESTO VA EN EL MENU
historial = obtener_historial(usuario_actual)
for dato in historial:
    print(f"{dato.fecha}: {dato.valor:.2f} {dato.unidad}")