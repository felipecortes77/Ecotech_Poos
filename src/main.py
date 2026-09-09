# src/main.py
from dominio.empleado import Empleado
from dominio.registrotiempo import RegistroTiempo
empleado = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@ecotech.cl"
)

empleado2 = Empleado("Juanito Torres","juanito.torres@ecotech.cl")

horas = RegistroTiempo("06/07/2013",25)

print(empleado.mostrar_datos())
print(empleado2.mostrar_datos())
print(horas.mostrar_horas())