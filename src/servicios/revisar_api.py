import requests
import math
from datetime import timezone
from email.utils import parsedate_to_datetime


def obtener_datos():
    respuesta = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=(3, 5),
    )
    respuesta.raise_for_status()
    return respuesta.json()


def extraer_clp(datos, moneda:str = "CLP"):
    if not isinstance(datos, dict):
        raise ValueError("Respuesta inesperada.")
    if datos.get("result") != "success":
        raise ValueError("La API no devolvió una respuesta exitosa.")
    rates = datos.get("rates")
    if not isinstance(rates, dict):
        raise ValueError("No hay tasas de cambio disponibles.")
    valor = rates.get(moneda)
    if (
        type(valor) not in (int, float)
        or not math.isfinite(valor)
        or valor <= 0
    ):
        raise ValueError(f"Valor del {moneda} inválido.")
    fecha_actualizacion = datos.get("time_last_update_utc")
    if not isinstance(fecha_actualizacion, str) or not fecha_actualizacion.strip():
        raise ValueError("La API no informó la fecha de actualización.")
    try:
        fecha = parsedate_to_datetime(fecha_actualizacion)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("La fecha de actualización de la API no es válida.") from error
    if fecha.tzinfo is None:
        raise ValueError("La fecha de actualización debe incluir zona horaria.")
    fecha = fecha.astimezone(timezone.utc).date().isoformat()
    return fecha, valor


def extraer_primero(datos):
    return extraer_clp(datos)
