# menu_usuario.py
from getpass import getpass
from servicios.autenticacion import autenticar
from servicios.mi_cuenta import (
    actualizar_mis_datos,
    mis_registros,
    obtener_mis_datos,
)
from servicios.indicadores import consultar_indicador


def solicitar_login():
    nombre = input("Usuario: ")
    clave = getpass("Contraseña: ")
    try:
        usuario = autenticar(nombre, clave)
    except (TypeError, ValueError):
        print("No se pudo validar el acceso.")
        return None
    if usuario is None:
        print("Usuario o contraseña incorrectos.")
    else:
        print("Sesión iniciada correctamente.")
        return usuario

def mostrar_perfil(usuario_actual):
    if usuario_actual is None:
        print("Inicie sesión para ver el perfil.")
        return
    try:
        empleado = obtener_mis_datos(usuario_actual)
        print(f"Usuario: {usuario_actual['nombre_usuario']}")
        print(f"Ficha: {empleado.mostrar_datos()}")
    except (PermissionError, ValueError) as error:
        print(f"No fue posible consultar la ficha: {error}")


def modificar_mis_datos(usuario_actual):
    nombre = input("Nuevo nombre: ").strip()
    correo = input("Nuevo correo: ").strip()
    try:
        if actualizar_mis_datos(usuario_actual, nombre, correo):
            print("Nombre y correo actualizados correctamente.")
        else:
            print("No se pudo actualizar la ficha.")
    except (PermissionError, TypeError, ValueError) as error:
        print(f"No fue posible actualizar la ficha: {error}")
    except Exception as error:
        print(f"Error al actualizar la ficha: {error}")


def consultar_mis_registros(usuario_actual):
    try:
        registros = mis_registros(usuario_actual)
        if not registros:
            print("No tienes registros de tiempo.")
            return
        total_horas = 0
        for registro in registros:
            print(registro.mostrar_horas())
            total_horas += registro.horas
        print(f"Total de horas: {total_horas}")
    except (PermissionError, ValueError) as error:
        print(f"No fue posible consultar tus registros: {error}")
    except Exception as error:
        print(f"Error al consultar tus registros: {error}")


def consultar_indicador_api(usuario_actual):
    try:
        indicador = consultar_indicador(usuario_actual)
        print(f"Actualizado: {indicador.fecha}")
        print(f"Dólar: {indicador.valor:,.2f} {indicador.unidad}")
    except PermissionError as error:
        print(f"No tienes permiso para consultar la API: {error}")
    except (RuntimeError, ValueError) as error:
        print(f"No fue posible consultar la API: {error}")


def menu_privado(usuario_actual):
    if usuario_actual is None:
        print("Debe iniciar sesión.")
        return "9"
    if usuario_actual.get("rol") != "empleado":
        print("Este menú está disponible solo para empleados.")
        return "9"
    while True:
        print("\n----- MI CUENTA -----")
        print("1. Ver mi ficha")
        print("2. Modificar mi nombre y correo")
        print("3. Consultar mis registros de tiempo")
        print("4. Consultar dólar desde la API")
        print("0. Cerrar sesión")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("Sesión cerrada.")
            return "0"
        if opcion == "1":
            mostrar_perfil(usuario_actual)
        elif opcion == "2":
            modificar_mis_datos(usuario_actual)
        elif opcion == "3":
            consultar_mis_registros(usuario_actual)
        elif opcion == "4":
            consultar_indicador_api(usuario_actual)
        else:
            print("Opción no válida.")
