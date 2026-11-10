import math
from datetime import date


class Indicador:
    def __init__(
        self,
        fecha,
        valor,
        verificado_en=None,
        fuente="exchangerate-api"
    ):
        if not isinstance(fecha, str):
            raise TypeError("La fecha del indicador debe ser texto.")
        try:
            date.fromisoformat(fecha)
        except ValueError as error:
            raise ValueError("La fecha debe tener formato AAAA-MM-DD.") from error
        if (
            type(valor) not in (int, float)
            or not math.isfinite(valor)
            or valor <= 0
        ):
            raise ValueError("El valor del indicador debe ser positivo y finito.")

        self.fecha = fecha
        self.valor = valor
        self.fuente = fuente
        self.codigo = "dolar"
        self.unidad = "CLP/USD"
        self.verificado_en = verificado_en
