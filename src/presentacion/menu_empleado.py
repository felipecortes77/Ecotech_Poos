from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

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
        menu_empleados()
    elif opcion == "2":
        listar_empleados()
        input("Enter para continuar")
        menu_empleados()
    elif opcion == "3":
        buscar_empleado()
        menu_empleados()
    elif opcion == "4":
        actualizar_empleado()
        menu_empleados()
    elif opcion == "5":
        eliminar_empleado()
        menu_empleados()
    elif opcion == "0":
        print("")
    else:
        print("Opción no válida.")
        menu_empleados()

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
        print("La ID no pertenece a ningún empleado")
