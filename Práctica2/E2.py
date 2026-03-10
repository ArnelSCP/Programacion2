import math

class AlgebraVectorial:

    def __init__(self, a1,a2,a3,b1,b2,b3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3


    def productoEscalar(self):
        return (self.a1*self.b1 +
                self.a2*self.b2 +
                self.a3*self.b3)


    def perpendicular(self):
        if self.productoEscalar() == 0:
            return True
        else:
            return False


    def paralela(self):
        cx = self.a2*self.b3 - self.a3*self.b2
        cy = self.a3*self.b1 - self.a1*self.b3
        cz = self.a1*self.b2 - self.a2*self.b1

        if cx == 0 and cy == 0 and cz == 0:
            return True
        else:
            return False


    def normaB(self):
        return math.sqrt(self.b1**2 + self.b2**2 + self.b3**2)


    def proyeccion(self):
        pe = self.productoEscalar()
        nb = self.normaB()

        return pe/(nb**2)


    def componente(self):
        pe = self.productoEscalar()
        nb = self.normaB()

        return pe/nb

v = AlgebraVectorial(1,2,3,4,5,6)

print("Producto escalar:", v.productoEscalar())

if v.perpendicular():
    print("Vectores perpendiculares")
else:
    print("No son perpendiculares")

if v.paralela():
    print("Vectores paralelos")
else:
    print("No son paralelos")

print("Proyeccion:", v.proyeccion())
print("Componente:", v.componente())
