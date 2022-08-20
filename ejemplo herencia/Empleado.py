from Personas import Persona
#(nombre de la clase padre)
class Empleado(Persona):
    codigo=0
    nivelAcademico=""
    sueldoBase=0.0
    
    def obtenerSueldoBase(self):
        return self.sueldoBase
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print("Código: ", self.codigo)
        print("Nivel academico: ", self.nivelAcademico)
        print("Sueldo base: ", self.sueldoBase)
        #return super().mostrarDatos(), "Código: ", self.codigo, ", nivelAcademico: ", self.nivelAcademico, " Sueldo base: ", self.sueldoBase