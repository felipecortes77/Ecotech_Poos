# persistencia/empleado_dao.py
from persistencia.conexion import abrir_conexion, obtener_motor

class DepartamentoDAO:
    @staticmethod
    def insertar(departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"
        
        sql = f"""
            INSERT INTO departamento (nombre, _empleados)
            VALUES ({marcador}, {marcador})
        """
        cursor.execute(sql, (departamento.nombre, departamento._empleados))
        departamento.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return departamento
