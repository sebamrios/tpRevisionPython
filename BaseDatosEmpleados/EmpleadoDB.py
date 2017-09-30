class Empleado():
    #atributos
    empCount=0;
    nombre="";
    dni=0;
    cargo="";
    salario=0;
    domicilio="";

    #metodos
    def __init__(self,nombre):
        self.nombre=nombre
        self.empCount +=1

    def ingresarDni(self,dni):
        self.dni=dni

    def ingresarSalario(self,salario):
        self.salario=salario

    def ingresarCargo(self,cargo):
        self.cargo=cargo

    def ingresarDomicilio(self,domicilio):
        self.domicilio=domicilio

    def mostrarCount(self):
        print("\n Total de empleados %d",self.empCount);

    def mostrar(self):
        print("Nombre:"+ self.nombre)
        print("Dni:"+ str(self.dni))
        print("domicilio:"+self.domicilio)
        print("Cargo:"+self.cargo)
        print("Salario:" + str(self.salario))
