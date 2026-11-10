from dominio.usuario import Usuario
from dominio.empleado import Empleado
from persistencia.conexion import abrir_conexion, marcador_sql


class UsuarioDAO:
    @staticmethod
    def insertar(usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            cursor.execute(
                f"SELECT nombre FROM empleado WHERE id = {marca}",
                (usuario.empleado_id,)
            )
            fila_empleado = cursor.fetchone()
            if fila_empleado is None:
                raise ValueError("El empleado seleccionado no existe.")

            nombre_usuario = Usuario.normalizar_usuario(fila_empleado[0])
            if usuario.nombre_usuario != nombre_usuario:
                raise ValueError(
                    "El nombre de usuario debe coincidir con el nombre "
                    "del empleado asociado."
                )

            cursor.execute(
                f"SELECT id FROM usuario WHERE id_empleado = {marca}",
                (usuario.empleado_id,)
            )
            if cursor.fetchone() is not None:
                raise ValueError("El empleado ya tiene una cuenta de usuario.")

            sql = f"""
                INSERT INTO usuario (nombre_usuario, password_hash, id_empleado, rol)
                VALUES ({marca}, {marca}, {marca}, {marca})
            """
            cursor.execute(
                sql,
                (
                    usuario.nombre_usuario,
                    usuario.password_hash,
                    usuario.empleado_id,
                    usuario.rol
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
            rol=fila[4],
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
                SELECT id, nombre_usuario, password_hash, id_empleado, rol
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
                SELECT id, nombre_usuario, password_hash, id_empleado, rol
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
                SELECT id, nombre_usuario, password_hash, id_empleado, rol
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
                "SELECT id, nombre_usuario, password_hash, id_empleado, rol "
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
    def actualizar(usuario, nombre_empleado=None):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            cursor.execute(
                f"SELECT id_empleado FROM usuario WHERE id = {marca}",
                (usuario.id,)
            )
            fila_cuenta = cursor.fetchone()
            if fila_cuenta is None:
                return False
            if fila_cuenta[0] != usuario.empleado_id:
                raise ValueError(
                    "No se puede cambiar el empleado asociado a la cuenta."
                )
            usuario.rol = Usuario.validar_rol(usuario.rol)

            cursor.execute(
                f"SELECT nombre FROM empleado WHERE id = {marca}",
                (usuario.empleado_id,)
            )
            fila_empleado = cursor.fetchone()
            if fila_empleado is None:
                raise ValueError("El empleado asociado no existe.")

            if nombre_empleado is not None:
                nombre_empleado = Empleado.validar_nombre(nombre_empleado)
                usuario.nombre_usuario = Usuario.normalizar_usuario(
                    nombre_empleado
                )
                cursor.execute(
                    f"UPDATE empleado SET nombre = {marca} WHERE id = {marca}",
                    (nombre_empleado, usuario.empleado_id)
                )
            elif usuario.nombre_usuario != Usuario.normalizar_usuario(
                fila_empleado[0]
            ):
                raise ValueError(
                    "El nombre de usuario debe coincidir con el nombre "
                    "del empleado asociado."
                )

            cursor.execute(
                f"SELECT id FROM usuario WHERE nombre_usuario = {marca} "
                f"AND id != {marca}",
                (usuario.nombre_usuario, usuario.id)
            )
            if cursor.fetchone() is not None:
                raise ValueError("Ese nombre de usuario ya está registrado.")

            sql = (
                "UPDATE usuario "
                f"SET nombre_usuario = {marca}, password_hash = {marca}, "
                f"id_empleado = {marca}, rol = {marca} WHERE id = {marca}"
            )
            cursor.execute(
                sql,
                (
                    usuario.nombre_usuario,
                    usuario.password_hash,
                    usuario.empleado_id,
                    usuario.rol,
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