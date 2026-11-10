from persistencia.crear_bd import crear_tablas
from presentacion.menu_departamento import menu_departamento
from presentacion.menu_empleado import menu_empleados
from presentacion.menu_proyecto import menu_proyecto
from presentacion.menu_registrotiempo import menu_registro_tiempo
from presentacion.menu_usuario_mod import menu_usuarios
from persistencia.semilla_bd import (
    cargar_departamentos,
    cargar_empleados,
    cargar_gerentes,
    cargar_usuarios,
)
from presentacion.menu_usuario import (
    consultar_indicador_api,
    menu_privado,
    solicitar_login,
)


def main():
    try:
        crear_tablas()
        cargar_departamentos()
        cargar_empleados()
        cargar_gerentes()
        cargar_usuarios()
    except Exception as e:
        print(f"No se pudo preparar la base de datos: {e}")
        return

    while True:
        usuario_actual = solicitar_login()
        if usuario_actual is None:
            if input("Enter para reintentar o 0 para salir: ") == "0":
                return
            continue

        if usuario_actual["rol"] == "admin":
            menu_admin(usuario_actual)
        else:
            menu_privado(usuario_actual)

def menu_admin(usuario_actual):
    opcion = ""
    while opcion != "0":
        print("\n-----MENU PRINCIPAL ECOTECH -----")
        print("1. Departamentos")
        print("2. Empleados")
        print("3. Proyectos")
        print("4. Registro de tiempo")
        print("5. Usuarios")
        print("6. Consultar dólar desde la API")
        print("0. Cerrar Sesion")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_departamento()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            menu_proyecto()
        elif opcion == "4":
            menu_registro_tiempo()
        elif opcion == "5":
            menu_usuarios()
        elif opcion == "6":
            consultar_indicador_api(usuario_actual)
        elif opcion == "0":
            print("Sesión cerrada.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    from persistencia.conexion import obtener_motor
    print("Motor:", obtener_motor())
    main()