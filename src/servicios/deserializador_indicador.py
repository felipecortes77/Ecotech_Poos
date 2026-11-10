from dominio.indicador import Indicador
from servicios.revisar_api import extraer_clp

class DeserializadorIndicador:
    @staticmethod
    def desde_api(datos):
        fecha, valor = extraer_clp(datos)
        return Indicador(
            fecha=fecha,
            valor=valor,
            fuente="exchangerate-api"
        )