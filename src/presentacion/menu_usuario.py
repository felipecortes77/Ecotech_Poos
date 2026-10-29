from dominio.usuario import Usuario
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.usuario_dao import UsuarioDAO



def menu_usuarios():
    opcion = ""
    while opcion != "0":
        print("\n----- USUARIOS -----")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuarios")
        print("4. Actualizar usuarios")
        print("5. Eliminar usuarios")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
            input("Enter para continuar")
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            actualizar_usuario()
        elif opcion == "5":
            eliminar_usuario()
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


def registrar_usuario():
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    if not nombre or not correo:
        print("El nombre y el correo no pueden estar vacíos.")
        return

    try:
        id_departamento, valido = seleccionar_departamento()
        if not valido:
            return

        usuario = usuario(nombre, correo, id_departamento=id_departamento)
        UsuarioDAO.insertar(usuario)
        print(f"usuario registrado correctamente. ID: {usuario.id}")
    except Exception as e:
        print(f"No fue posible registrar el usuario: {e}")


def listar_usuarios():
    print("Lista de usuarios:")
    try:
        usuarios = UsuarioDAO.listar()
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        for item in usuarios:
            print(item.mostrar_datos())
    except Exception as e:
        print(f"Error al listar los usuarios: {e}")



def buscar_usuario():
    listar_usuarios()
    id_usuario = pedir_id("INGRESE LA ID DEL usuario:")
    if id_usuario is None:
        return

    try:
        encontrado = UsuarioDAO.buscar_por_id(id_usuario)
        if encontrado:
            print("Encontrado:", encontrado.mostrar_datos())
        else:
            print("La ID no pertenece a ningún usuario.")
    except Exception as e:
        print(f"Error al buscar el usuario: {e}")


def actualizar_usuario():
    listar_usuarios()
    id_usuario = pedir_id("INGRESE LA ID DEL USUARIO: ")
    if id_usuario is None:
        return

    nombre_nuevo = input("Nombre nuevo: ").strip()
    correo_nuevo = input("Correo nuevo: ").strip()

    if not nombre_nuevo or not correo_nuevo:
        print("El nombre y el correo no pueden estar vacíos.")
        return

    try:
        usuario = UsuarioDAO.buscar_por_id(id_usuario)
        if usuario is None:
            print("No se encontró el usuario")
            return

        usuario.nombre = nombre_nuevo
        usuario.correo = correo_nuevo
        id_departamento, valido = seleccionar_departamento(
            usuario.id_departamento
        )
        if not valido:
            return
        usuario.id_departamento = id_departamento

        if UsuarioDAO.actualizar(usuario):
            print("usuario actualizado correctamente.")
        else:
            print("No se encontró el usuario.")
    except Exception as e:
        print(f"Error al actualizar el usuario: {e}")


def eliminar_usuario():
    listar_usuarios()
    print("Eliminar usuario")
    id_usuario = pedir_id("INGRESE LA ID DEL usuario: ")
    if id_usuario is None:
        return

    try:
        eliminado = UsuarioDAO.eliminar(id_usuario)
        if eliminado:
            print("usuario eliminado correctamente.")
        else:
            print("No se encontró el usuario.")
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
