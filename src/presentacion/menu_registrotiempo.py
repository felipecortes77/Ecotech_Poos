from dominio.registrotiempo import RegistroTiempo
from persistencia.registrotiempo_dao import RegistroTiempoDAO
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.proyecto_dao import ProyectoDAO


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
    return horas


def registrar_tiempo():
    fecha = input("Fecha (AAAA-MM-DD): ").strip()
    if not fecha:
        print("La fecha no puede estar vacía.")
        return

    horas = pedir_horas("Horas trabajadas: ")
    if horas is None:
        return

    id_empleado = pedir_id("ID del empleado: ")
    if id_empleado is None:
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
        print(f"Registro de tiempo guardado correctamente. ID: {registro.id}")
    except Exception as e:
        print(f"No fue posible registrar el tiempo: {e}")


def listar_registros():
    print("Lista de registros de tiempo:")
    try:
        registros = RegistroTiempoDAO.listar()
        if not registros:
            print("No hay registros de tiempo.")
            return
        for item in registros:
            print(item.mostrar_horas())
    except Exception as e:
        print(f"Error al listar los registros: {e}")


def listar_registros_por_empleado():
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
            total += item.horas
        print(f"Total de horas: {total}")
    except Exception as e:
        print(f"Error al listar los registros: {e}")


def buscar_registro():
    listar_registros()
    id_registro = pedir_id("INGRESE LA ID DEL REGISTRO:")
    if id_registro is None:
        return

    try:
        encontrado = RegistroTiempoDAO.buscar_por_id(id_registro)
        if encontrado:
            print("Registro encontrado:")
            print(encontrado.mostrar_horas())
        else:
            print("No se encontró el registro")
    except Exception as e:
        print(f"Error al buscar el registro: {e}")


def actualizar_registro():
    listar_registros()
    id_registro = pedir_id("INGRESE LA ID DEL REGISTRO: ")
    if id_registro is None:
        return

    fecha_nueva = input("Fecha nueva (AAAA-MM-DD): ").strip()
    if not fecha_nueva:
        print("La fecha no puede estar vacía.")
        return

    horas_nuevas = pedir_horas("Horas nuevas: ")
    if horas_nuevas is None:
        return

    try:
        registro = RegistroTiempoDAO.buscar_por_id(id_registro)
        if registro is None:
            print("No se encontró el registro")
            return

        registro.fecha = fecha_nueva
        registro.horas = horas_nuevas

        if RegistroTiempoDAO.actualizar(registro):
            print("Registro actualizado correctamente.")
        else:
            print("No se encontró el registro.")
    except Exception as e:
        print(f"Error al actualizar el registro: {e}")


def eliminar_registro():
    listar_registros()
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