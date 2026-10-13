# # src/main.py
# from dominio.empleado import Empleado
# from dominio.registrotiempo import RegistroTiempo
# from dominio.departamento import Departamento

# empleado = Empleado(
#     nombre="Ana Torres",
#     correo="ana.torres@ecotech.cl"
# )

# empleado2 = Empleado(
#     nombre = "Juanito Torres",
#     correo ="juanito.torres@ecotech.cl"
# )0

# empleado3 = Empleado(
#     nombre = "Pepe Tapia",
#     correo ="pepe.tapia@ecotech.cl"
# )

# horas = RegistroTiempo("06/07/2013",3)
# horas2 = RegistroTiempo("18/12/2014",2)
# horas3 = RegistroTiempo("25/03/2011",7)

# print(empleado.mostrar_datos())
# print(empleado2.mostrar_datos())
# desarrollo = Departamento("DEP Desarrollo")

# # Uso desde main.py
# empleado.registrar_tiempo(horas)
# empleado2.registrar_tiempo(horas2)
# empleado3.registrar_tiempo(horas3)

# desarrollo.agregar_empleado(empleado)
# desarrollo.agregar_empleado(empleado2)
# desarrollo.agregar_empleado(empleado3)



# for empleado in desarrollo._empleados:
#     for horas in empleado.horas_registradas:
#         print("El empleado " + empleado.nombre + " trabajó " + horas.mostrar_horas())


# print(desarrollo.cantidad_empleados())

# for empleado in desarrollo._empleados:
#     print(empleado.mostrar_datos())

##############################################################################################

# main.py


# empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl")
# print("Antes:", empleado.id)
# # None
# EmpleadoDAO.insertar(empleado)
# print("Después:", empleado.id)
# id generado por la BD


# empleado = Empleado(
#     nombre="Ana Torres",
#     correo="ana.torres@ecotech.cl"
# )

# empleado1 = Empleado(
#     nombre="Juan Torres",
#     correo="juan.torres@ecotech.cl"
# )

# EmpleadoDAO.actualizar(Empleado(
#     id=6,
#     nombre = "Jorge torres",
#     correo = "jorge.torres@ecotech.cl"
# ))

# #EmpleadoDAO.insertar(empleado)

# main.py
# from persistencia.crear_bd import crear_tablas
# from presentacion.menu_departamento import menu_departamento
# from presentacion.menu_empleado import menu_empleados
# from presentacion.menu_proyecto import menu_proyecto
# from presentacion.menu_registrotiempo import menu_registro_tiempo


from persistencia.crear_bd import crear_tablas
from presentacion.menu_departamento import menu_departamento
from presentacion.menu_empleado import menu_empleados
from presentacion.menu_proyecto import menu_proyecto
from presentacion.menu_registrotiempo import menu_registro_tiempo

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
    try:
        crear_tablas()
    except Exception as e:
        print(f"No se pudo preparar la base de datos: {e}")
    
    menu_principal()