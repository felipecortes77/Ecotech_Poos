from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO
import sys 

crear_tablas()

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
        print("no encontrado")
