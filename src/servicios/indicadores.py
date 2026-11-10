import requests
from persistencia.indicador_dao import IndicadorDAO
from servicios.permisos import exigir_sesion
from servicios.deserializador_indicador import DeserializadorIndicador
from servicios.revisar_api import obtener_datos


def consultar_indicador(sesion):
    exigir_sesion(sesion)
    try:
        datos = obtener_datos()
    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            "No fue posible conectarse al servicio de indicadores."
        ) from error
    indicador = DeserializadorIndicador.desde_api(datos)
    return IndicadorDAO.guardar(indicador)