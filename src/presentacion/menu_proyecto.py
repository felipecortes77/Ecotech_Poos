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


def nombre_valido(nombre: str) -> bool:
    for caracter in nombre:
        if not (caracter.isalnum() or caracter == " "):
            return False
    return True


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


def registrar_proyecto():
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    if not nombre_valido(nombre):
        print("El nombre solo puede tener letras, números y espacios.")
        return

    fecha_inicio = input("Fecha de inicio (AAAA-MM-DD, Enter para omitir): ").strip()
    if fecha_inicio == "":
        fecha_inicio = None
    elif not fecha_valida(fecha_inicio):
        print("Fecha no válida. Usa el formato AAAA-MM-DD.")
        return

    proyecto = Proyecto(nombre, fecha_inicio=fecha_inicio)
    try:
        ProyectoDAO.insertar(proyecto)
        print(f"Proyecto registrado correctamente. ID: {proyecto.id()}")
    except Exception as e:
        print(f"No fue posible registrar el proyecto: {e}")


def listar_proyectos():
    print("Lista de proyectos:")
    try:
        proyectos = ProyectoDAO.listar()
        if not proyectos:
            print("No hay proyectos registrados.")
            return False
        for item in proyectos:
            print(item.mostrar_datos())
        return True
    except Exception as e:
        print(f"Error al listar los proyectos: {e}")
        return False


def buscar_proyecto():
    if not listar_proyectos():
        return
    id_proyecto = pedir_id("INGRESE LA ID DEL PROYECTO: ")
    if id_proyecto is None:
        return

    try:
        encontrado = ProyectoDAO.buscar_por_id(id_proyecto)
        if encontrado:
            print("Proyecto encontrado:")
            print(encontrado.mostrar_datos())
        else:
            print("No se encontró el proyecto.")
    except Exception as e:
        print(f"Error al buscar el proyecto: {e}")


def actualizar_proyecto():
    if not listar_proyectos():
        return
    id_proyecto = pedir_id("INGRESE LA ID DEL PROYECTO: ")
    if id_proyecto is None:
        return

    nombre_nuevo = input("Nombre nuevo: ").strip()
    if nombre_nuevo == "":
        print("El nombre no puede estar vacío.")
        return
    if not nombre_valido(nombre_nuevo):
        print("El nombre solo puede tener letras, números y espacios.")
        return

    fecha_nueva = input("Fecha de inicio nueva (AAAA-MM-DD, Enter para omitir): ").strip()
    if fecha_nueva == "":
        fecha_nueva = None
    elif not fecha_valida(fecha_nueva):
        print("Fecha no válida. Usa el formato AAAA-MM-DD.")
        return

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
    if not listar_proyectos():
        return
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