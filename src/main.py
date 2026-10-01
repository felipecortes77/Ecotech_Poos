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
# )

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
from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO
import sys
crear_tablas()

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




def registrar_empleado():
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    empleado = Empleado(nombre, correo)
    try:
        EmpleadoDAO.insertar(empleado)
        print("Empleado registrado correctamente.")
    except Exception:
        print("No fue posible registrar el empleado.")

def listar_empleados():
    print("Lista de empleados:")
    for item in EmpleadoDAO.listar():
        print(item.mostrar_datos())
    

def eliminar_empleado():
    listar_empleados()
    eliminar = input("Ingrese la ID del empleado: ")
    try:
        eliminado = EmpleadoDAO.eliminar(eliminar)
        if(eliminado):
            print("Se elimino correctamente")
        else:
            print("No se encontro la ID")
    except:
        print("Error")

def actualizar_empleado():
    listar_empleados()
    buscar = input("Ingrese la ID del empleado: ")
    nombre_nuevo = input("Nombre: ").strip()
    correo_nuevo = input("Correo: ").strip()

    EmpleadoDAO.actualizar(Empleado(
        id= buscar,
        nombre = nombre_nuevo,
        correo = correo_nuevo
    ))

def buscar_empleado():
    buscar = input("Ingrese la ID del empleado: ")
    encontrado = EmpleadoDAO.buscar_por_id(buscar)
    if(encontrado):
        print("Encontrado:", encontrado.mostrar_datos())
    else:
        print("no encontrado")


#Menú

def menu_general():
    print("\n===== ECOTECH =====")
    print("1. Ver el menú de empleados")
    print("2. Ver el menú de departamentos")
    # print("3. Buscar empleado")
    # print("4. Actualizar empleado")
    # print("5. Eliminar empleado")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        menu_empleados()
    # elif opcion == "2":
    #     listar_empleados()
    #     input("Enter para continuar")
    # elif opcion == "3":
    #     buscar_empleado()
    # elif opcion == "4":
    #     actualizar_empleado()
    # elif opcion == "5":
    #     eliminar_empleado()
    elif opcion == "0":
        print("Hasta luego")
        sys.exit(0)
    else:
        print("Opción no válida.")

def menu_empleados():
    print("\n===== ECOTECH =====")
    print("1. Registrar empleado")
    print("2. Listar empleados")
    print("3. Buscar empleado")
    print("4. Actualizar empleado")
    print("5. Eliminar empleado")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_empleado()
    elif opcion == "2":
        listar_empleados()
        input("Enter para continuar")
    elif opcion == "3":
        buscar_empleado()
    elif opcion == "4":
        actualizar_empleado()
    elif opcion == "5":
        eliminar_empleado()
    elif opcion == "0":
        menu_general()
    else:
        print("Opción no válida.")

def main():
    while True:
        menu_general()
        

if __name__ == "__main__":
    main()