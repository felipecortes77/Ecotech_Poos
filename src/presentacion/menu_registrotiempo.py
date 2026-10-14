from dominio.registrotiempo import RegistroTiempo
from persistencia.registrotiempo_dao import RegistroTiempoDAO
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.proyecto_dao import ProyectoDAO
from presentacion.menu_empleado import listar_empleados
from presentacion.menu_proyecto import listar_proyectos


def menu_registro_tiempo():
    opcion = ""
    while opcion != "0":
        print("\n----- REGISTRO DE TIEMPO -----")
        print("1. Registrar tiempo")
        print("2. Listar registros")
        print("3. Buscar registro")
        print("4. Actualizar registro")
        print("5. Eliminar registro")
        print("6. Listar registros por empleado")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_tiempo()
        elif opcion == "2":
            listar_registros()
            input("Enter para continuar")
        elif opcion == "3":
            buscar_registro()
        elif opcion == "4":
            actualizar_registro()
        elif opcion == "5":
            eliminar_registro()
        elif opcion == "6":
            listar_registros_por_empleado()
            input("Enter para continuar")
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


def pedir_horas(mensaje: str):
    try:
        horas = float(input(mensaje).strip().replace(",", "."))
    except ValueError:
        print("Las horas deben ser un número.")
        return None

    if horas <= 0:
        print("Las horas deben ser mayores a 0.")
        return None
    if horas > 24:
        print("Las horas no pueden ser más de 24 por día.")
        return None
    return horas


def fecha_valida(fecha: str) -> bool:
    partes = fecha.split("-")
    if len(partes) != 3:
        return False
    if not (partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
        return False
    if len(partes[0]) != 4 or len(partes[1]) != 2 or len(partes[2]) != 2:
        return False
    if int(partes[1]) < 1 or int(partes[1]) > 12:
        return False
    if int(partes[2]) < 1 or int(partes[2]) > 31:
        return False
    return True


def registrar_tiempo():
    fecha = input("Fecha (AAAA-MM-DD): ").strip()
    if fecha == "":
        print("La fecha no puede estar vacía.")
        return
    if not fecha_valida(fecha):
        print("Fecha no válida. Usa el formato AAAA-MM-DD.")
        return

    horas = pedir_horas("Horas trabajadas: ")
    if horas is None:
        return

    if not listar_empleados():
        print("Primero debes registrar un empleado.")
        return
    id_empleado = pedir_id("ID del empleado: ")
    if id_empleado is None:
        return

    if not listar_proyectos():
        print("Primero debes registrar un proyecto.")
        return
    id_proyecto = pedir_id("ID del proyecto: ")
    if id_proyecto is None:
        return

    try:
        if EmpleadoDAO.buscar_por_id(id_empleado) is None:
            print("No existe un empleado con esa ID.")
            return

        if ProyectoDAO.buscar_por_id(id_proyecto) is None:
            print("No existe un proyecto con esa ID.")
            return

        registro = RegistroTiempo(
            fecha=fecha,
            horas=horas,
            id_empleado=id_empleado,
            id_proyecto=id_proyecto
        )
        RegistroTiempoDAO.insertar(registro)
        print(f"Registro de tiempo guardado correctamente. ID: {registro.id()}")
    except Exception as e:
        print(f"No fue posible registrar el tiempo: {e}")


def listar_registros():
    print("Lista de registros de tiempo:")
    try:
        registros = RegistroTiempoDAO.listar()
        if not registros:
            print("No hay registros de tiempo.")
            return False
        for item in registros:
            print(item.mostrar_horas())
        return True
    except Exception as e:
        print(f"Error al listar los registros: {e}")
        return False


def listar_registros_por_empleado():
    if not listar_empleados():
        return
    id_empleado = pedir_id("ID del empleado: ")
    if id_empleado is None:
        return

    try:
        registros = RegistroTiempoDAO.listar_por_empleado(id_empleado)
        if not registros:
            print("Ese empleado no tiene registros de tiempo.")
            return

        total = 0
        for item in registros:
            print(item.mostrar_horas())
            total += item.get_horas()
        print(f"Total de horas: {total}")
    except Exception as e:
        print(f"Error al listar los registros: {e}")


def buscar_registro():
    if not listar_registros():
        return
    id_registro = pedir_id("INGRESE LA ID DEL REGISTRO: ")
    if id_registro is None:
        return

    try:
        encontrado = RegistroTiempoDAO.buscar_por_id(id_registro)
        if encontrado:
            print("Registro encontrado:")
            print(encontrado.mostrar_horas())
        else:
            print("No se encontró el registro.")
    except Exception as e:
        print(f"Error al buscar el registro: {e}")


def actualizar_registro():
    if not listar_registros():
        return
    id_registro = pedir_id("INGRESE LA ID DEL REGISTRO: ")
    if id_registro is None:
        return

    fecha_nueva = input("Fecha nueva (AAAA-MM-DD): ").strip()
    if fecha_nueva == "":
        print("La fecha no puede estar vacía.")
        return
    if not fecha_valida(fecha_nueva):
        print("Fecha no válida. Usa el formato AAAA-MM-DD.")
        return

    horas_nuevas = pedir_horas("Horas nuevas: ")
    if horas_nuevas is None:
        return

    try:
        registro = RegistroTiempoDAO.buscar_por_id(id_registro)
        if registro is None:
            print("No se encontró el registro.")
            return

        registro.set_fecha(fecha_nueva)
        registro.set_horas(horas_nuevas)

        if RegistroTiempoDAO.actualizar(registro):
            print("Registro actualizado correctamente.")
        else:
            print("No se encontró el registro.")
    except Exception as e:
        print(f"Error al actualizar el registro: {e}")


def eliminar_registro():
    if not listar_registros():
        return
    print("Eliminar registro")
    id_registro = pedir_id("INGRESE LA ID DEL REGISTRO: ")
    if id_registro is None:
        return

    try:
        eliminado = RegistroTiempoDAO.eliminar(id_registro)
        if eliminado:
            print("Registro eliminado correctamente.")
        else:
            print("No se encontró el registro.")
    except Exception as e:
        print(f"Error al eliminar el registro: {e}")