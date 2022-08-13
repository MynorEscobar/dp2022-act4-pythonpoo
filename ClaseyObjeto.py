class Ejemplo:
    #atributos
    valor1=0
    valor2=0
    resultado=0
    #métodos 
    def asignarValor1(self, v1):
        self.valor1 = v1

    def asignarValor2(self, v2):
        self.valor2 = v2

    def calcularSuma(self):
        self.resultado = self.valor1 + self.valor2
        print("La suma es: ", self.resultado)

    def calcularMulti(self):
        self.resultado = self.valor1 * self.valor2
        return "La multiplicación es: ", self.resultado


#instanciar la clase Ejemplo
objeto = Ejemplo()

objeto.asignarValor1(int(input("ingrese un número: ")))
objeto.asignarValor2(int(input("Ingrese otro número: ")))
objeto.calcularSuma()
print(objeto.calcularMulti())



