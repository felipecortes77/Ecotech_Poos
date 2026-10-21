# En un archivo Python de prueba:
import requests
import math

def obtener_datos():
    respuesta = requests.get(
        #"https://mindicador.cl/api/dolar",
        "https://open.er-api.com/v6/latest/USD",
        timeout=(3, 5),
    )
    print("Estado HTTP:", respuesta.status_code)
    respuesta.raise_for_status()
    return respuesta.json()


import math

def extraer_clp(datos, moneda:str = "CLP"):
    # Verificar que la respuesta sea un diccionario.
    if not isinstance(datos, dict):
        raise ValueError("Respuesta inesperada.")
    
    # Comprobar que el resultado sea exitoso
    if datos.get("result") != "success":
        raise ValueError("La API no devolvió una respuesta exitosa.")

    # Obtener el diccionario de tasas de cambio.
    rates = datos.get("rates")
    if not isinstance(rates, dict):
        raise ValueError("No hay tasas de cambio disponibles.")

    # Extraer el valor del CLP.
    valor = rates.get(moneda)

    # Aceptar solo números finitos y mayores que cero.
    if (
        type(valor) not in (int, float)
        or not math.isfinite(valor)
        or valor <= 0
    ):
        raise ValueError(f"Valor del {moneda} inválido.")

    # Devolver la fecha de actualización y el valor del CLP como una tupla.
    fecha = datos.get("time_last_update_utc")
    return fecha, valor



try:
    datos = obtener_datos()
    fecha, valor = extraer_clp(datos)
    fecha, valor2 = extraer_clp(datos,"ANG")
    fecha, valor3 = extraer_clp(datos,"AUD")

    print(fecha)
    print(valor,valor2,valor3)
except requests.exceptions.RequestException:
    # Controlar fallos de conexión, espera, HTTP o decodificación JSON.
    print("No pudimos consultar el servicio. Reintente.")
except (ValueError, KeyError, TypeError):
    # Controlar valores inválidos, claves ausentes o tipos incorrectos.
    print("La respuesta no contiene un indicador válido.")
