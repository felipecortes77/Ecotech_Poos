from persistencia.crear_bd import crear_tablas
from presentacion.menu_departamento import menu_departamento
from presentacion.menu_empleado import menu_empleados
from presentacion.menu_proyecto import menu_proyecto
from presentacion.menu_registrotiempo import menu_registro_tiempo
from persistencia.semilla_bd import cargar_departamentos, cargar_empleados



def menu_principal():
    opcion = ""
    while opcion != "0":
        print("\n-----MENU PRINCIPAL ECOTECH -----")
        print("1. Departamentos")
        print("2. Empleados")
        print("3. Proyectos")
        print("4. Registro de tiempo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_departamento()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            menu_proyecto()
        elif opcion == "4":
            menu_registro_tiempo()
        elif opcion == "0":
            print("Hasta luego.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    from persistencia.conexion import obtener_motor
    print("Motor:", obtener_motor())

    try:
        crear_tablas()
        cargar_departamentos()
        cargar_empleados()
    except Exception as e:
        print(f"No se pudo preparar la base de datos: {e}")
    
    menu_principal()