import sqlite3

class BaseDatos():
    #metodos
    def __init__(self):
        self.conexion=sqlite3.connect("sqlite3/EmpleadosBD.sqlite")# Primero se establece la conexion a la base de datos
        self.consulta=self.conexion.cursor() # luego se crea un cursor el que nos permitira hacer el trabajo dentro de la base de datos

    def crearBDEmpleados(self):#se crea la tabla
        sql="""
        CREATE TABLE IF NOT EXISTS Empleados(
        id INTEGER PRYMARY KEY AUTO_INCREMENT NOT NULL,
        nombre VARCHAR(50) NOT NULL,
        dni VARCHAR(50) NOT NULL,
        cargo VARCHAR(50) NOT NULL,
        sueldo VARCHAR(50) NOT NULL)
        """

        if (self.consulta.execute(sql)):
            print ("Tabla Empleado creada con exito")
        else:
            print ("Ha ocurrido un error")

    def insertarEmpleado(self,Nombre,DNI,Cargo,Sueldo,Domicilio):#se ingresa un registro

        param=(Nombre,DNI,Cargo,Sueldo,Domicilio)
        sql2="INSERT INTO Empleados VALUES(?,?,?,?,?)"

        if (self.consulta.execute(sql2,param)):
            print ("se acaba de insertar un registro")
        else:
            print ("Ha ocurrido un error")

    def mostrarEmpleado(self): #se muestra la tabla
        self.consulta=self.conexion.cursor()

        sql="""
        SELECT * FROM Empleados
        """
        self.consulta.execute(sql)
        data=self.consulta.fetchall() #se almacena todo lo que se consulta en la variable data
        print ("\n\nTabla Empleados\n\n")
        for fila in data:
            print (str(fila[0])+"\t"+str(fila[1])+"\t"+str(fila[2])+"\t"+str(fila[3])+"\t"+str(fila[4]))

    def cerrarBD(self): #Se cierra la base de datos
        self.consulta.close()
        self.conexion.commit()
        self.conexion.close()
        print ("\n\nse cerro la base de datos")
