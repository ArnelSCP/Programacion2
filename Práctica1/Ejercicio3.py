import math

class EcuacionCuadratica:
    # atributos privados y constructor
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    # obtenemos el discrimiante
    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    # metodos
    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)

#pedimos los valores a, b y c 
print("Ingrese los coeficientes de la ecuación cuadrática:")
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

#creamos el objeto
ecuacion = EcuacionCuadratica(a, b, c)
discriminante = ecuacion.getDiscriminante()

#mostramos el resultado segun el valor del discriminante
if discriminante > 0:
    # tiene dos raices reales
    print("La ecuación tiene dos raíces", ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())
elif discriminante == 0:
    # tiene una sola raiz real osea que ambas son iguales
    print("La ecuación tiene una raíz", ecuacion.getRaiz1())
else:
    # si el discriminante es negativo
    print("La ecuación no tiene raíces reales")
