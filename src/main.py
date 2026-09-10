# src/main.py
from dominio.empleado import Empleado
from dominio.registrotiempo import RegistroTiempo
from dominio.departamento import Departamento

empleado = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@ecotech.cl"
)

empleado2 = Empleado(
    nombre = "Juanito Torres",
    correo ="juanito.torres@ecotech.cl"
)

empleado3 = Empleado(
    nombre = "Pepe Tapia",
    correo ="pepe.tapia@ecotech.cl"
)

horas = RegistroTiempo("06/07/2013",3)
horas2 = RegistroTiempo("18/12/2014",2)
horas3 = RegistroTiempo("25/03/2011",7)

print(empleado.mostrar_datos())
print(empleado2.mostrar_datos())
desarrollo = Departamento("DEP Desarrollo")

# Uso desde main.py
empleado.registrar_tiempo(horas)
empleado2.registrar_tiempo(horas2)
empleado3.registrar_tiempo(horas3)

desarrollo.agregar_empleado(empleado)
desarrollo.agregar_empleado(empleado2)
desarrollo.agregar_empleado(empleado3)



for empleado in desarrollo._empleados:
    for horas in empleado.horas_registradas:
        print("El empleado " + empleado.nombre + " trabajó " + horas.mostrar_horas())


print(desarrollo.cantidad_empleados())

for empleado in desarrollo._empleados:
    print(empleado.mostrar_datos())