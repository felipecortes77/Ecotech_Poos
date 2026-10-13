from dominio.empleado import Empleado
from persistencia.conexion import abrir_conexion, marcador_sql


class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                INSERT INTO empleado (nombre, correo, id_departamento)
                VALUES ({marca}, {marca}, {marca})
            """
            cursor.execute(
                sql,
                (empleado.nombre, empleado.correo, empleado.id_departamento)
            )
            empleado.id = cursor.lastrowid
            conexion.commit()
            return empleado
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def _fila_a_empleado(fila):
        return Empleado(
            id=fila[0],
            nombre=fila[1],
            correo=fila[2],
            id_departamento=fila[3]
        )

    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre, correo, id_departamento
                FROM empleado WHERE id = {marca}
            """
            cursor.execute(sql, (id_empleado,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return EmpleadoDAO._fila_a_empleado(fila)
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_correo(correo_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre, correo, id_departamento
                FROM empleado WHERE correo = {marca}
            """
            cursor.execute(sql, (correo_empleado,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return EmpleadoDAO._fila_a_empleado(fila)
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_nombre(nombre_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre, correo, id_departamento
                FROM empleado WHERE nombre LIKE {marca}
            """
            cursor.execute(sql, (f"%{nombre_empleado}%",))
            filas = cursor.fetchall()
            empleados = []
            for fila in filas:
                empleados.append(EmpleadoDAO._fila_a_empleado(fila))
            return empleados
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
                "SELECT id, nombre, correo, id_departamento FROM empleado"
            )
            filas = cursor.fetchall()
            empleados = []
            for fila in filas:
                empleados.append(EmpleadoDAO._fila_a_empleado(fila))
            return empleados
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar_por_departamento(id_departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre, correo, id_departamento
                FROM empleado WHERE id_departamento = {marca}
            """
            cursor.execute(sql, (id_departamento,))
            filas = cursor.fetchall()
            empleados = []
            for fila in filas:
                empleados.append(EmpleadoDAO._fila_a_empleado(fila))
            return empleados
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE empleado "
                f"SET nombre = {marca}, correo = {marca}, "
                f"id_departamento = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(
                sql,
                (
                    empleado.nombre,
                    empleado.correo,
                    empleado.id_departamento,
                    empleado.id
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
    def eliminar(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "DELETE FROM empleado "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (id_empleado,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()