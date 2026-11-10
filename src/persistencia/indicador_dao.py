from datetime import datetime, timezone

from persistencia.conexion import abrir_conexion, marcador_sql, obtener_motor


class IndicadorDAO:
    @staticmethod
    def guardar(indicador):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            verificado_en = indicador.verificado_en or (
                datetime.now(timezone.utc).isoformat()
            )
            valores = (
                indicador.fuente,
                indicador.codigo,
                indicador.fecha,
                indicador.valor,
                indicador.unidad,
                verificado_en,
            )

            if obtener_motor() == "sqlite":
                sql = f"""
                    INSERT INTO indicador_api
                    (fuente, codigo, fecha, valor, unidad, verificado_en)
                    VALUES ({marca}, {marca}, {marca}, {marca}, {marca}, {marca})
                    ON CONFLICT (fuente, codigo, fecha) DO UPDATE SET
                    valor = excluded.valor,
                    unidad = excluded.unidad,
                    verificado_en = excluded.verificado_en
                """
            else:
                sql = f"""
                    INSERT INTO indicador_api
                    (fuente, codigo, fecha, valor, unidad, verificado_en)
                    VALUES ({marca}, {marca}, {marca}, {marca}, {marca}, {marca})
                    ON DUPLICATE KEY UPDATE
                    valor = VALUES(valor),
                    unidad = VALUES(unidad),
                    verificado_en = VALUES(verificado_en)
                """

            cursor.execute(sql, valores)
            conexion.commit()
            indicador.verificado_en = verificado_en
            return indicador
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT fecha, valor, verificado_en, fuente "
                "FROM indicador_api ORDER BY fecha DESC"
            )
            return [
                (fila[0], fila[1], fila[2], fila[3])
                for fila in cursor.fetchall()
            ]
        finally:
            if conexion is not None:
                conexion.close()