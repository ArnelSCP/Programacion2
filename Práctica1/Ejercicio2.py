class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        #introducimos los atributos privados
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def tieneSolucion(self):
        #calculamos la parte de abajo de la formula
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        if denominador != 0:
            return True
        else:
            return False

    def getX(self):
        #aplicamos la formula de x
        numerador = (self.__e * self.__d) - (self.__b * self.__f)
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        return numerador / denominador

    def getY(self):
        #aplicamos la formula de y
        numerador = (self.__a * self.__f) - (self.__e * self.__c)
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        return numerador / denominador

#pedimos datos
print("Introduce los valores de la ecuación:")
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))

#creamos la ecuacion
ecuacion = EcuacionLineal(a, b, c, d, e, f)

#mostramos resultados
if ecuacion.tieneSolucion() == True:
    valor_x = ecuacion.getX()
    valor_y = ecuacion.getY()
    print("x =", valor_x, ", y =", valor_y)
else:
    print("La ecuación no tiene solución")
