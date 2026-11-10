from dominio.empleado import Empleado
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.empleado_dao import EmpleadoDAO



def menu_empleados():
    opcion = ""
    while opcion != "0":
        print("\n----- EMPLEADOS -----")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            listar_empleados()
            input("Enter para continuar")
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            eliminar_empleado()
        elif opcion == "0":
            print("Saliendo...")
        else:
            print("Opción no válida.")


def pedir_id(mensaje: str):
    try:
        return int(input(mensaje).strip())
    except ValueError:
        print("La ID debe ser un número.")
        return None

def nombre_valido(nombre: str) -> bool:
    if not nombre or not nombre.strip():
        return False
    for caracter in nombre:
        if not (caracter.isalpha() or caracter == " "):
            return False
    return True


def mostrar_departamentos():
    try:
        departamentos = DepartamentoDAO.listar()
        if not departamentos:
            print("No hay departamentos registrados.")
            input("Enter para continuar")
            return False
        print("Departamentos disponibles:")
        for item in departamentos:
            print(item.mostrar_datos())
        return True
    except Exception as e:
        print(f"Error al listar los departamentos: {e}")
        return False


def seleccionar_departamento(id_actual=None):
    if not mostrar_departamentos():
        return id_actual, True

    if id_actual is None:
        mensaje = "ID del departamento (Enter para omitir): "
    else:
        mensaje = "ID del departamento (Enter conserva, 0 quita): "
    texto = input(mensaje).strip()
    if not texto:
        return id_actual, True
    if texto == "0":
        return None, True

    try:
        id_departamento = int(texto)
    except ValueError:
        print("La ID debe ser un número.")
        return id_actual, False

    if DepartamentoDAO.buscar_por_id(id_departamento) is None:
        print("No existe un departamento con esa ID.")
        return id_actual, False
    return id_departamento, True


def registrar_empleado():
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    if not nombre or not correo:
        print("El nombre y el correo no pueden estar vacíos.")
        return

    try:
        id_departamento, valido = seleccionar_departamento()
        if not valido:
            return

        empleado = Empleado(nombre, correo, id_departamento=id_departamento)
        EmpleadoDAO.insertar(empleado)
        print(f"Empleado registrado correctamente. ID: {empleado.id}")
    except Exception as e:
        print(f"No fue posible registrar el empleado: {e}")


def listar_empleados():
    print("Lista de empleados:")
    try:
        empleados = EmpleadoDAO.listar()
        if not empleados:
            print("No hay empleados registrados.")
            return False
        for item in empleados:
            print(item.mostrar_datos())
        return True
    except Exception as e:
        print(f"Error al listar los empleados: {e}")
        return False



def buscar_empleado():
    listar_empleados()
    id_empleado = pedir_id("INGRESE LA ID DEL EMPLEADO:")
    if id_empleado is None:
        return

    try:
        encontrado = EmpleadoDAO.buscar_por_id(id_empleado)
        if encontrado:
            print("Encontrado:", encontrado.mostrar_datos())
        else:
            print("La ID no pertenece a ningún empleado.")
    except Exception as e:
        print(f"Error al buscar el empleado: {e}")


def actualizar_empleado():
    listar_empleados()
    id_empleado = pedir_id("INGRESE LA ID DEL EMPLEADO: ")
    if id_empleado is None:
        return

    nombre_nuevo = input("Nombre nuevo: ").strip()
    correo_nuevo = input("Correo nuevo: ").strip()

    if not nombre_nuevo or not correo_nuevo:
        print("El nombre y el correo no pueden estar vacíos.")
        return

    try:
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado is None:
            print("No se encontró el empleado")
            return

        empleado.nombre = nombre_nuevo
        empleado.correo = correo_nuevo
        id_departamento, valido = seleccionar_departamento(
            empleado.id_departamento
        )
        if not valido:
            return
        empleado.id_departamento = id_departamento

        if EmpleadoDAO.actualizar(empleado):
            print("Empleado actualizado correctamente.")
        else:
            print("No se encontró el empleado.")
    except Exception as e:
        print(f"Error al actualizar el empleado: {e}")


def eliminar_empleado():
    listar_empleados()
    print("Eliminar empleado")
    id_empleado = pedir_id("INGRESE LA ID DEL EMPLEADO: ")
    if id_empleado is None:
        return

    try:
        eliminado = EmpleadoDAO.eliminar(id_empleado)
        if eliminado:
            print("Empleado eliminado correctamente.")
        else:
            print("No se encontró el empleado.")
    except Exception as e:
        print(f"Error al eliminar el empleado: {e}")
