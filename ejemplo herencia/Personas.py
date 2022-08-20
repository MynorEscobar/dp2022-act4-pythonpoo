class Persona:
    #atributos
    nombre=""
    apellido=""
    telefono=0
    direccion=""
    
    #métodos
    def mostrarDatos(self):
        print ("Nombre: ", self.nombre )
        print ("Apellido: ", self.apellido)
        print ("Dirección: ", self.direccion)
        #return "Nombre: ", self.nombre, ", Apellido: ", self.apellido, ", Teléfono: ", self.telefono, ", Dirección", self.direccion