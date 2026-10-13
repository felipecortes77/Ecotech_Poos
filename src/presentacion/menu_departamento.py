from persistencia.departamento_dao import DepartamentoDAO
from dominio.departamento import Departamento


def menu_departamento():
    opcion = ""
    while opcion != "0":
        print("\n----DEPARTAMENTOS----")
        print("1. Registrar departamento")
        print("2. Listar departamentos")
        print("3. Buscar departamento")
        print("4. Actualizar departamento")
        print("5. Eliminar departamento")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_departamento()
        elif opcion == "2":
            listar_departamentos()
            input("Enter para continuar")
        elif opcion == "3":
            buscar_departamento()
        elif opcion == "4":
            actualizar_departamento()
        elif opcion == "5":
            eliminar_departamento()
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


def registrar_departamento():
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    departamento = Departamento(nombre)
    try:
        DepartamentoDAO.insertar(departamento)
        print(f"Departamento registrado correctamente. ID: {departamento.id}")
    except Exception as e:
        print(f"No fue posible registrar el departamento: {e}")


def listar_departamentos():
    print("Lista de departamentos:")
    try:
        departamentos = DepartamentoDAO.listar()
        if not departamentos:
            print("No hay departamentos registrados.")
            return
        for item in departamentos:
            print(item.mostrar_datos())
    except Exception as e:
        print(f"Error al listar los departamentos: {e}")


def buscar_departamento():
    listar_departamentos()
    id_departamento = pedir_id("INGRESE LA ID DEL DEPARTAMENTO: ")
    if id_departamento is None:
        return

    try:
        departamento = DepartamentoDAO.buscar_por_id(id_departamento)
        if departamento:
            print("Departamento encontrado:")
            print(departamento.mostrar_datos())
        else:
            print("No se encontró el departamento")
    except Exception as e:
        print(f"Error al buscar el departamento: {e}")


def actualizar_departamento():
    listar_departamentos()
    id_departamento = pedir_id("Ingrese la ID del departamento: ")
    if id_departamento is None:
        return

    nombre_nuevo = input("Nombre nuevo: ").strip()
    if not nombre_nuevo:
        print("El nombre no puede estar vacío.")
        return

    try:
        actualizado = DepartamentoDAO.actualizar(
            Departamento(id=id_departamento, nombre=nombre_nuevo)
        )
        if actualizado:
            print("Departamento actualizado correctamente.")
        else:
            print("No se encontró el departamento.")
    except Exception as e:
        print(f"Error al actualizar el departamento: {e}")


def eliminar_departamento():
    listar_departamentos()
    print("Eliminar departamento")
    id_departamento = pedir_id("Ingrese la ID del departamento: ")
    if id_departamento is None:
        return

    try:
        eliminado = DepartamentoDAO.eliminar(id_departamento)
        if eliminado:
            print("Departamento eliminado correctamente.")
        else:
            print("No se encontró el departamento.")
    except Exception as e:
        print(f"Error al eliminar el departamento: {e}")