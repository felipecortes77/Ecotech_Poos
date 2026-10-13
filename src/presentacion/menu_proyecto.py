from dominio.proyecto import Proyecto
from persistencia.proyecto_dao import ProyectoDAO


def menu_proyecto():
    opcion = ""
    while opcion != "0":
        print("\n----- PROYECTOS -----")
        print("1. Registrar proyecto")
        print("2. Listar proyectos")
        print("3. Buscar proyecto")
        print("4. Actualizar proyecto")
        print("5. Eliminar proyecto")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_proyecto()
        elif opcion == "2":
            listar_proyectos()
            input("Enter para continuar")
        elif opcion == "3":
            buscar_proyecto()
        elif opcion == "4":
            actualizar_proyecto()
        elif opcion == "5":
            eliminar_proyecto()
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


def registrar_proyecto():
    nombre = input("Nombre: ").strip()
    fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ").strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    if not fecha_inicio:
        fecha_inicio = None

    proyecto = Proyecto(nombre, fecha_inicio=fecha_inicio)
    try:
        ProyectoDAO.insertar(proyecto)
        print(f"Proyecto registrado correctamente. ID: {proyecto.id}")
    except Exception as e:
        print(f"No fue posible registrar el proyecto: {e}")


def listar_proyectos():
    print("Lista de proyectos:")
    try:
        proyectos = ProyectoDAO.listar()
        if not proyectos:
            print("No hay proyectos registrados.")
            return
        for item in proyectos:
            print(item.mostrar_datos())
    except Exception as e:
        print(f"Error al listar los proyectos: {e}")


def buscar_proyecto():
    listar_proyectos()
    id_proyecto = pedir_id("INGRESE LA ID DEL PROYECTO:")
    if id_proyecto is None:
        return

    try:
        encontrado = ProyectoDAO.buscar_por_id(id_proyecto)
        if encontrado:
            print("Proyecto encontrado:")
            print(encontrado.mostrar_datos())
        else:
            print("No se encontró el proyecto")
    except Exception as e:
        print(f"Error al buscar el proyecto: {e}")


def actualizar_proyecto():
    listar_proyectos()
    id_proyecto = pedir_id("INGRESE LA ID DEL PROYECTO: ")
    if id_proyecto is None:
        return

    nombre_nuevo = input("Nombre nuevo: ").strip()
    fecha_nueva = input("Fecha de inicio nueva (AAAA-MM-DD): ").strip()

    if not nombre_nuevo:
        print("El nombre no puede estar vacío.")
        return

    if not fecha_nueva:
        fecha_nueva = None

    try:
        actualizado = ProyectoDAO.actualizar(
            Proyecto(id=id_proyecto, nombre=nombre_nuevo, fecha_inicio=fecha_nueva)
        )
        if actualizado:
            print("Proyecto actualizado correctamente.")
        else:
            print("No se encontró el proyecto.")
    except Exception as e:
        print(f"Error al actualizar el proyecto: {e}")


def eliminar_proyecto():
    listar_proyectos()
    print("Eliminar proyecto")
    id_proyecto = pedir_id("INGRESE LA ID DEL PROYECTO: ")
    if id_proyecto is None:
        return

    try:
        eliminado = ProyectoDAO.eliminar(id_proyecto)
        if eliminado:
            print("Proyecto eliminado correctamente.")
        else:
            print("No se encontró el proyecto.")
    except Exception as e:
        print(f"Error al eliminar el proyecto: {e}")