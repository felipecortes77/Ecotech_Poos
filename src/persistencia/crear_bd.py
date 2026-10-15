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
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL DEFAULT '',
                gerente TEXT
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
                nombre VARCHAR(100) NOT NULL,
                descripcion varchar(100) NOT NULL,
                gerente VARCHAR(100)
                )
            '''
            sql_proyecto = '''
                CREATE TABLE IF NOT EXISTS proyecto (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                descripcion VARCHAR(100) NOT NULL,
                fecha_inicio DATE NOT NULL,
                fecha_fin DATE,
                estado VARCHAR(20) NOT NULL
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

        if obtener_motor() == "sqlite":
            cursor.execute("PRAGMA table_info(departamento)")
            columnas = {fila[1] for fila in cursor.fetchall()}
            if "descripcion" not in columnas:
                cursor.execute(
                    "ALTER TABLE departamento "
                    "ADD COLUMN descripcion TEXT NOT NULL DEFAULT ''"
                )
            if "gerente" not in columnas:
                cursor.execute(
                    "ALTER TABLE departamento ADD COLUMN gerente TEXT"
                )
        else:
            cursor.execute("SHOW COLUMNS FROM departamento")
            columnas = {fila[0] for fila in cursor.fetchall()}
            if "descripcion" not in columnas:
                cursor.execute(
                    "ALTER TABLE departamento "
                    "ADD COLUMN descripcion VARCHAR(100) NOT NULL DEFAULT ''"
                )
            if "gerente" not in columnas:
                cursor.execute(
                    "ALTER TABLE departamento ADD COLUMN gerente VARCHAR(100)"
                )

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