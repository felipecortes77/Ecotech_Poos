from dominio.departamento import Departamento
from dominio.empleado import Empleado
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.empleado_dao import EmpleadoDAO


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