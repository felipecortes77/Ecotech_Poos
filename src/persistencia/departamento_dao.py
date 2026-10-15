from dominio.departamento import Departamento
from persistencia.conexion import abrir_conexion, marcador_sql


class DepartamentoDAO:
    @staticmethod
    def insertar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                INSERT INTO departamento (nombre, descripcion, gerente)
                VALUES ({marca}, {marca}, {marca})
            """
            cursor.execute(
                sql,
                (
                    departamento.nombre,
                    departamento.descripcion,
                    departamento.gerente
                )
            )
            departamento.id = cursor.lastrowid
            conexion.commit()
            return departamento
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def _fila_a_departamento(fila):
        return Departamento(
            id=fila[0],
            nombre=fila[1],
            descripcion=fila[2],
            gerente=fila[3]
        )

    @staticmethod
    def buscar_por_id(id_departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre, descripcion, gerente
                FROM departamento WHERE id = {marca}
            """
            cursor.execute(sql, (id_departamento,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return DepartamentoDAO._fila_a_departamento(fila)
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
                "SELECT id, nombre, descripcion, gerente FROM departamento"
            )
            filas = cursor.fetchall()
            departamentos = []
            for fila in filas:
                departamentos.append(DepartamentoDAO._fila_a_departamento(fila))
            return departamentos
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE departamento "
                f"SET nombre = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (departamento.nombre, departamento.id))
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
    def eliminar(id_departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "DELETE FROM departamento "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (id_departamento,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()