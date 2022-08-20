from Empleado import Empleado

class Ventas(Empleado):
    tipoContratacion=""
    comisionVentas=1.0
    igss = 0.0
    sueldoLiquido = 0.0
    
      
    def mostrarDatos(self):
        super().mostrarDatos()
        self.igss= super().obtenerSueldoBase() * 4.83 / 100
        self.sueldoLiquido= super().obtenerSueldoBase() + self.comisionVentas - self.igss
   
        print("Tipo de Contratación: ", self.tipoContratacion)
        print("Comisión de Ventas: ", self.comisionVentas)
        print("Sueldo liquido: ", self.sueldoLiquido)
    
    