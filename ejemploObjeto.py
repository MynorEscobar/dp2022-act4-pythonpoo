#llamar al archivo y llamar la clase
from Ejemplo import Ejemplo

#instanciar la clase Ejemplo
objeto = Ejemplo()

objeto.asignarValor1(int(input("ingrese un número: ")))
objeto.asignarValor2(int(input("Ingrese otro número: ")))
objeto.calcularSuma()
print(objeto.calcularMulti())

