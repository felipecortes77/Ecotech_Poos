from dominio.proyecto import Proyecto
from persistencia.conexion import abrir_conexion, marcador_sql


class ProyectoDAO:
    @staticmethod
    def insertar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_fin, estado)
                VALUES ({marca}, {marca},{marca}, {marca},{marca})
            """
            cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin, proyecto.estado))
            proyecto.id = cursor.lastrowid
            conexion.commit()
            return proyecto
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def _fila_a_proyecto(fila):
        return Proyecto(
            id=fila[0],
            nombre=fila[1],
            descripcion=fila[2],
            fecha_inicio=fila[3],
            fecha_fin=fila[4],
            estado=fila[5]
        )

    @staticmethod
    def buscar_por_id(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre, descripcion, fecha_inicio, fecha_fin, estado
                FROM proyecto WHERE id = {marca}
            """
            cursor.execute(sql, (id_proyecto,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return ProyectoDAO._fila_a_proyecto(fila)
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_nombre(nombre_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                SELECT id, nombre, descripcion, fecha_inicio, fecha_fin, estado
                FROM proyecto WHERE nombre LIKE {marca}
            """
            cursor.execute(sql, (f"%{nombre_proyecto}%",))
            filas = cursor.fetchall()
            proyectos = []
            for fila in filas:
                proyectos.append(ProyectoDAO._fila_a_proyecto(fila))
            return proyectos
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, descripcion, fecha_inicio, fecha_fin, estado FROM proyecto")
            filas = cursor.fetchall()
            proyectos = []
            for fila in filas:
                proyectos.append(ProyectoDAO._fila_a_proyecto(fila))
            return proyectos
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE proyecto "
                f"SET nombre = {marca}, fecha_inicio = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(
                sql,
                (proyecto.nombre, proyecto.fecha_inicio, proyecto.id)
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
    def eliminar(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "DELETE FROM proyecto "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (id_proyecto,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion is not None:
                conexion.rollback()
            raise
        finally:
            if conexion is not None:
                conexion.close()