from dominio.registrotiempo import RegistroTiempo
from persistencia.conexion import abrir_conexion, marcador_sql


class RegistroTiempoDAO:
    @staticmethod
    def insertar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                INSERT INTO registro_tiempo
                (fecha, horas, id_empleado, id_proyecto)
                VALUES ({marca}, {marca}, {marca}, {marca})
            """
            cursor.execute(
                sql,
                (
                    registro.fecha,
                    registro.horas,
                    registro.id_empleado,
                    registro.id_proyecto
                )
            )
            registro.id = cursor.lastrowid
            conexion.commit()
            return registro
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def _fila_a_registro(fila):
        return RegistroTiempo(
            id=fila[0],
            fecha=fila[1],
            horas=fila[2],
            id_empleado=fila[3],
            id_proyecto=fila[4]
        )

    @staticmethod
    def buscar_por_id(id_registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, fecha, horas, id_empleado, id_proyecto
                FROM registro_tiempo WHERE id = {marca}
            """
            cursor.execute(sql, (id_registro,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return RegistroTiempoDAO._fila_a_registro(fila)
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
                "SELECT id, fecha, horas, id_empleado, id_proyecto "
                "FROM registro_tiempo"
            )
            filas = cursor.fetchall()
            registros = []
            for fila in filas:
                registros.append(RegistroTiempoDAO._fila_a_registro(fila))
            return registros
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar_por_empleado(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, fecha, horas, id_empleado, id_proyecto
                FROM registro_tiempo WHERE id_empleado = {marca}
            """
            cursor.execute(sql, (id_empleado,))
            filas = cursor.fetchall()
            registros = []
            for fila in filas:
                registros.append(RegistroTiempoDAO._fila_a_registro(fila))
            return registros
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar_por_proyecto(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, fecha, horas, id_empleado, id_proyecto
                FROM registro_tiempo WHERE id_proyecto = {marca}
            """
            cursor.execute(sql, (id_proyecto,))
            filas = cursor.fetchall()
            registros = []
            for fila in filas:
                registros.append(RegistroTiempoDAO._fila_a_registro(fila))
            return registros
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE registro_tiempo "
                f"SET fecha = {marca}, horas = {marca}, "
                f"id_empleado = {marca}, id_proyecto = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(
                sql,
                (
                    registro.fecha,
                    registro.horas,
                    registro.id_empleado,
                    registro.id_proyecto,
                    registro.id
                )
            )
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "DELETE FROM registro_tiempo "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (id_registro,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()