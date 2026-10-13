from persistencia.conexion import abrir_conexion, obtener_motor


def crear_tablas():
    conexion = None
    try:
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        if obtener_motor() == "sqlite":
            sql_departamento = '''
                CREATE TABLE IF NOT EXISTS departamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
                )
            '''
            sql_proyecto = '''
                CREATE TABLE IF NOT EXISTS proyecto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha_inicio TEXT
                )
            '''
            sql_empleado = '''
                CREATE TABLE IF NOT EXISTS empleado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                id_departamento INTEGER,
                FOREIGN KEY (id_departamento) REFERENCES departamento(id)
                )
            '''
            sql_registro = '''
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT NOT NULL,
                horas REAL NOT NULL,
                id_empleado INTEGER,
                id_proyecto INTEGER,
                FOREIGN KEY (id_empleado) REFERENCES empleado(id),
                FOREIGN KEY (id_proyecto) REFERENCES proyecto(id)
                )
            '''
        else:
            sql_departamento = '''
                CREATE TABLE IF NOT EXISTS departamento (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL
                )
            '''
            sql_proyecto = '''
                CREATE TABLE IF NOT EXISTS proyecto (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                fecha_inicio VARCHAR(20)
                )
            '''
            sql_empleado = '''
                CREATE TABLE IF NOT EXISTS empleado (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                correo VARCHAR(150) NOT NULL,
                id_departamento INT,
                FOREIGN KEY (id_departamento) REFERENCES departamento(id)
                )
            '''
            sql_registro = '''
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INT PRIMARY KEY AUTO_INCREMENT,
                fecha VARCHAR(20) NOT NULL,
                horas FLOAT NOT NULL,
                id_empleado INT,
                id_proyecto INT,
                FOREIGN KEY (id_empleado) REFERENCES empleado(id),
                FOREIGN KEY (id_proyecto) REFERENCES proyecto(id)
                )
            '''

        cursor.execute(sql_departamento)
        cursor.execute(sql_proyecto)
        cursor.execute(sql_empleado)
        cursor.execute(sql_registro)
        conexion.commit()

    except Exception:
        if conexion is not None:
            conexion.rollback()
        raise

    finally:
        if conexion is not None:
            conexion.close()


if __name__ == "__main__":
    crear_tablas()
    print("Base de datos preparada correctamente.")