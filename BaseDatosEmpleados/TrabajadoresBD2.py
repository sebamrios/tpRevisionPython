import sqlite3
from EmpleadoBD import Empleado
from DB import BaseDatos
#==============================================================================
f=open('DatosBD.txt','a')

BD=BaseDatos()
BD.crearBDEmpleados()
# Crear una carpeta de nombre sqlite3, con un archivo que se llame EmpleadoBD.sqlite
# dentro de ella,la cual funcionara como nuestra base de datos.
#==============================================================================
#                     Inscripcion de Empleados

x=int(raw_input("cuantos empleados quiere cargar?\n\n"))
x=x+1
for i in range (1,x):
    e=Empleado(raw_input("Ingrese el nombre del Empleado:\n"))
    e.ingresarSalario(raw_input("Ingrese el salario:\n"))
    e.ingresarDni(raw_input("Ingrese numero de Dni:\n"))
    e.ingresarDomicilio(raw_input("Ingrese el domicilio:\n"))
    e.ingresarCargo(raw_input("Ingrese cargo del empleado:\n"))

    BD.insertarEmpleado(e.nombre,e.dni,e.cargo,e.salario,e.domicilio)

    EmpleadoDic={'Nombre':e.nombre,'DNI':e.dni,'Domicilio':e.domicilio,'Cargo':e.cargo,'Salario':e.salario}

    f.write(str(EmpleadoDic)+",")

#==============================================================================
BD.mostrarEmpleado()
BD.cerrarBD()
f.close
