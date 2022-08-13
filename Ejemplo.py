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
