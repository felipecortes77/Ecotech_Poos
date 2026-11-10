from getpass import getpass
from dominio.empleado import Empleado
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.usuario_dao import UsuarioDAO
from presentacion.menu_empleado import listar_empleados
from servicios.autenticacion import (
    crear_hash,
    registrar_usuario as crear_cuenta,
)


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

def registrar_usuario():
    try:
        if not listar_empleados():
            return
        empleados = EmpleadoDAO.listar()
        if not empleados:
            print("No hay empleados para asociar a una cuenta.")
            return

        id_empleado = pedir_id("ID del empleado para la nueva cuenta: ")
        if id_empleado is None:
            return
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado is None:
            print("No existe un empleado con esa ID.")
            return

        cuenta_existente = UsuarioDAO.buscar_por_empleado(empleado.id)
        if cuenta_existente is not None:
            print(
                f"{empleado.nombre} ya tiene una cuenta "
                f"({cuenta_existente.nombre_usuario}, rol "
                f"{cuenta_existente.rol})."
            )
            return

        clave = getpass("Contraseña: ")
        try:
            Usuario.validar_clave(clave)
        except (TypeError, ValueError) as error:
            print(error)
            return
        if clave != getpass("Repita la contraseña: "):
            print("Las contraseñas no coinciden.")
            return

        print("Seleccione el rol:")
        print("1. Administrador")
        print("2. Empleado")
        opcion_rol = input("Opción: ").strip()
        roles = {"1": "admin", "2": "empleado"}
        rol = roles.get(opcion_rol)
        if rol is None:
            print("Opción de rol no válida.")
            return

        cuenta = crear_cuenta(empleado.id, empleado.nombre, clave, rol)
        print(
            f"Cuenta creada correctamente. Usuario: "
            f"{cuenta.nombre_usuario} - Rol: {cuenta.rol} - ID: {cuenta.id}"
        )
    except (TypeError, ValueError, PermissionError) as error:
        print(f"No fue posible crear la cuenta: {error}")
    except Exception as error:
        print(f"Error al crear la cuenta: {error}")


def listar_usuarios():
    print("Lista de usuarios:")
    try:
        usuarios = UsuarioDAO.listar()
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        for item in usuarios:
            mostrar_usuario(item)
    except Exception as e:
        print(f"Error al listar los usuarios: {e}")


def mostrar_usuario(usuario):
    print(
        f"ID: {usuario.id} - Usuario: {usuario.nombre_usuario} "
        f"- Rol: {usuario.rol}"
    )


def buscar_usuario():
    id_usuario = pedir_id("Ingrese la ID del usuario: ")
    if id_usuario is None:
        return

    try:
        encontrado = UsuarioDAO.buscar_por_id(id_usuario)
        if encontrado:
            print("Usuario encontrado:")
            mostrar_usuario(encontrado)
        else:
            print("La ID no pertenece a ningún usuario.")
    except Exception as e:
        print(f"Error al buscar el usuario: {e}")


def actualizar_usuario():
    listar_usuarios()
    id_usuario = pedir_id("Ingrese la ID del usuario a actualizar: ")
    if id_usuario is None:
        return

    try:
        usuario = UsuarioDAO.buscar_por_id(id_usuario)
        if usuario is None:
            print("No se encontró el usuario.")
            return

        empleado = EmpleadoDAO.buscar_por_id(usuario.empleado_id)
        if empleado is None:
            print("No se encontró el empleado asociado al usuario.")
            return

        print(
            f"Cuenta seleccionada: {usuario.nombre_usuario} "
            f"(rol: {usuario.rol})"
        )
        nombre_nuevo = input(
            f"Nombre nuevo del empleado [{empleado.nombre}]: "
        ).strip()
        if not nombre_nuevo:
            nombre_nuevo = empleado.nombre
        nombre_nuevo = Empleado.validar_nombre(nombre_nuevo)

        clave_nueva = getpass(
            "Nueva contraseña (Enter para conservarla): "
        )
        if clave_nueva:
            Usuario.validar_clave(clave_nueva)
            if clave_nueva != getpass("Repita la nueva contraseña: "):
                print("Las contraseñas no coinciden.")
                return
            usuario.password_hash = crear_hash(clave_nueva)

        print("Seleccione el rol (Enter para conservarlo):")
        print("1. Administrador")
        print("2. Empleado")
        opcion_rol = input(f"Rol actual [{usuario.rol}]: ").strip()
        roles = {"1": "admin", "2": "empleado"}
        if opcion_rol:
            rol_nuevo = roles.get(opcion_rol)
            if rol_nuevo is None:
                print("Opción de rol no válida.")
                return
            usuario.rol = Usuario.validar_rol(rol_nuevo)

        if UsuarioDAO.actualizar(usuario, nombre_empleado=nombre_nuevo):
            print(
                f"Usuario actualizado: {usuario.nombre_usuario} "
                f"(rol: {usuario.rol})."
            )
        else:
            print("No se pudo actualizar el usuario.")
    except (TypeError, ValueError) as e:
        print(f"No fue posible actualizar el usuario: {e}")
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
