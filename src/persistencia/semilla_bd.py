from dominio.departamento import Departamento
from dominio.empleado import Empleado
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.usuario_dao import UsuarioDAO
from servicios.autenticacion import registrar_usuario

USUARIOS_ADMIN = [
    ("admin123", "juan.perez@ecotech.cl"),
    ("Admin2026!", "maria.gonzalez@ecotech.cl"),
    ("Admin2026!", "carlos.silva@ecotech.cl"),
    ("Admin2026!", "ana.rodriguez@ecotech.cl"),
    ("Admin2026!", "jose.munoz@ecotech.cl"),
]

USUARIOS_EMPLEADO = [
    ("Empleado2026!", "laura.rojas@ecotech.cl"),
    ("Empleado2026!", "pedro.diaz@ecotech.cl"),
    ("Empleado2026!", "sofia.contreras@ecotech.cl"),
    ("Empleado2026!", "miguel.soto@ecotech.cl"),
    ("Empleado2026!", "carolina.martinez@ecotech.cl"),
]


def cargar_departamentos():
    datos = [
        ("Desarrollo", "Desarrollo y mantenimiento de soluciones tecnologicas"),
        ("Recursos Humanos", "Gestion del talento y bienestar del equipo"),
        ("Operaciones", "Coordinacion de procesos y servicios"),
        ("Finanzas", "Administracion financiera y presupuestos"),
        ("Ventas", "Relacion con clientes y desarrollo comercial"),
    ]
    nombres_existentes = {
        departamento.nombre for departamento in DepartamentoDAO.listar()
    }

    for nombre, descripcion in datos:
        if nombre in nombres_existentes:
            print(f"Ya existe: {nombre}")
            continue

        departamento = Departamento(nombre, descripcion)
        DepartamentoDAO.insertar(departamento)
        nombres_existentes.add(nombre)
        print(f"Creado: {nombre}")


def cargar_empleados(departamento_demo=None):
    if isinstance(departamento_demo, Departamento):
        departamento_demo = departamento_demo.id

    if departamento_demo is None:
        departamentos = DepartamentoDAO.listar()
        departamento = next(
            (
                item for item in departamentos
                if item.nombre == "Desarrollo"
            ),
            None
        )
        if departamento is None:
            raise ValueError(
                "No existe el departamento 'Desarrollo'; "
                "cargue los departamentos antes que los empleados."
            )
        departamento_demo = departamento.id

    if DepartamentoDAO.buscar_por_id(departamento_demo) is None:
        raise ValueError(
            f"No existe el departamento con ID {departamento_demo}."
        )

    datos = [
        ("Juan Perez", "juan.perez@ecotech.cl"),
        ("Maria Gonzalez", "maria.gonzalez@ecotech.cl"),
        ("Carlos Silva", "carlos.silva@ecotech.cl"),
        ("Ana Rodriguez", "ana.rodriguez@ecotech.cl"),
        ("Jose Muñoz", "jose.munoz@ecotech.cl"),
        ("Laura Rojas", "laura.rojas@ecotech.cl"),
        ("Pedro Diaz", "pedro.diaz@ecotech.cl"),
        ("Sofia Contreras", "sofia.contreras@ecotech.cl"),
        ("Miguel Soto", "miguel.soto@ecotech.cl"),
        ("Carolina Martinez", "carolina.martinez@ecotech.cl"),
        ("Francisco Morales", "francisco.morales@ecotech.cl"),
        ("Daniela Herrera", "daniela.herrera@ecotech.cl"),
        ("Andres Figueroa", "andres.figueroa@ecotech.cl"),
        ("Camila Castro", "camila.castro@ecotech.cl"),
        ("Diego Guzman", "diego.guzman@ecotech.cl"),
        ("Valentina Navarro", "valentina.navarro@ecotech.cl"),
        ("Gabriel Torres", "gabriel.torres@ecotech.cl"),
        ("Beatriz Flores", "beatriz.flores@ecotech.cl"),
        ("Ricardo Alvarez", "ricardo.alvarez@ecotech.cl"),
        ("Paula Mendoza", "paula.mendoza@ecotech.cl"),
    ]
    for nombre, correo in datos:
        existente = EmpleadoDAO.buscar_por_correo(correo)
        if existente is not None:
            print(f"Ya existe: {correo}")
            continue
        empleado = Empleado(
            nombre,
            correo,
            id_departamento=departamento_demo
        )
        EmpleadoDAO.insertar(empleado)
        print(f"Creado: {correo}")


def cargar_usuarios():
    for rol, usuarios in (
        ("admin", USUARIOS_ADMIN),
        ("empleado", USUARIOS_EMPLEADO),
    ):
        cuentas_rol = [
            cuenta for cuenta in UsuarioDAO.listar()
            if cuenta.rol == rol
        ]
        for clave, correo in usuarios:
            empleado = EmpleadoDAO.buscar_por_correo(correo)
            if empleado is None:
                if len(cuentas_rol) >= len(usuarios):
                    print(
                        f"Se conserva la cuenta {rol}: no se encontró\nel correo semilla '{correo}'\n(posiblemente actualizado en la ficha)."
                    )
                    continue
                raise ValueError(
                    f"No existe el empleado asociado al correo '{correo}'."
                )

            nombre_usuario = empleado.nombre.strip().lower()
            cuenta = UsuarioDAO.buscar_por_empleado(empleado.id)
            cuenta_nombre = UsuarioDAO.buscar_por_nombre_usuario(
                nombre_usuario
            )
            if cuenta_nombre is not None and cuenta_nombre.empleado_id != empleado.id:
                raise ValueError(
                    f"El nombre de usuario '{nombre_usuario}' ya está "
                    "asociado a otro empleado."
                )

            if cuenta is not None:
                if cuenta.rol != rol:
                    raise ValueError(
                        f"El usuario '{nombre_usuario}' ya existe con otro rol."
                    )
                if cuenta.nombre_usuario != nombre_usuario:
                    cuenta.nombre_usuario = nombre_usuario
                    if not UsuarioDAO.actualizar(cuenta):
                        raise ValueError(
                            f"No se pudo actualizar la cuenta de "
                            f"'{empleado.nombre}'."
                        )
                continue

            if cuenta_nombre is not None:
                raise ValueError(
                    f"Ya existe una cuenta con el nombre '{nombre_usuario}'."
                )

            registrar_usuario(empleado.id, nombre_usuario, clave, rol)
            print(f"Cuenta {rol} creada: {nombre_usuario}")

def cargar_gerentes():
    asignaciones = {
        "Desarrollo": "juan.perez@ecotech.cl",
        "Recursos Humanos": "maria.gonzalez@ecotech.cl",
        "Operaciones": "carlos.silva@ecotech.cl",
        "Finanzas": "ana.rodriguez@ecotech.cl",
        "Ventas": "jose.munoz@ecotech.cl",
    }
    empleados = {
        correo: EmpleadoDAO.buscar_por_correo(correo)
        for correo in asignaciones.values()
    }
    departamentos = {
        departamento.nombre: departamento
        for departamento in DepartamentoDAO.listar()
    }

    for nombre_departamento, correo_gerente in asignaciones.items():
        departamento = departamentos.get(nombre_departamento)
        empleado = empleados[correo_gerente]
        if departamento is None or empleado is None:
            raise ValueError(
                f"Falta el departamento o empleado gerente para "
                f"'{nombre_departamento}'."
            )
        if departamento.gerente:
            continue
        departamento.gerente = empleado.nombre
        DepartamentoDAO.actualizar(departamento)
