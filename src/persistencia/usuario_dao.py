from dominio.usuario import Usuario
from persistencia.conexion import abrir_conexion, marcador_sql


class UsuarioDAO:
    @staticmethod
    def insertar(usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                INSERT INTO usuario (nombre_usuario, password_hash, id_empleado)
                VALUES ({marca}, {marca}, {marca})
            """
            cursor.execute(
                sql,
                (
                    usuario.nombre_usuario,
                    usuario.password_hash,
                    usuario.empleado_id
                )
            )
            usuario.id = cursor.lastrowid
            conexion.commit()
            return usuario
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def _fila_a_usuario(fila):
        return Usuario(
            nombre_usuario=fila[1],
            password_hash=fila[2],
            empleado_id=fila[3],
            id=fila[0]
        )

    @staticmethod
    def buscar_por_id(id_usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre_usuario, password_hash, id_empleado
                FROM usuario WHERE id = {marca}
            """
            cursor.execute(sql, (id_usuario,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return UsuarioDAO._fila_a_usuario(fila)
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_nombre_usuario(nombre_usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre_usuario, password_hash, id_empleado
                FROM usuario WHERE nombre_usuario = {marca}
            """
            cursor.execute(sql, (nombre_usuario,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return UsuarioDAO._fila_a_usuario(fila)
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_empleado(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre_usuario, password_hash, id_empleado
                FROM usuario WHERE id_empleado = {marca}
            """
            cursor.execute(sql, (id_empleado,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return UsuarioDAO._fila_a_usuario(fila)
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
                "SELECT id, nombre_usuario, password_hash, id_empleado "
                "FROM usuario"
            )
            filas = cursor.fetchall()
            usuarios = []
            for fila in filas:
                usuarios.append(UsuarioDAO._fila_a_usuario(fila))
            return usuarios
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE usuario "
                f"SET nombre_usuario = {marca}, password_hash = {marca}, "
                f"id_empleado = {marca} WHERE id = {marca}"
            )
            cursor.execute(
                sql,
                (
                    usuario.nombre_usuario,
                    usuario.password_hash,
                    usuario.empleado_id,
                    usuario.id
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
    def eliminar(id_usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM usuario WHERE id = {marca}"
            cursor.execute(sql, (id_usuario,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()