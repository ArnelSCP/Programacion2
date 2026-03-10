import math

class MiPunto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancia(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def distanciaXY(self, x, y):
        dx = self.x - x
        dy = self.y - y
        return math.sqrt(dx*dx + dy*dy)


p1 = MiPunto()
p2 = MiPunto(10, 30.5)

d = p1.distancia(p2)

print("Punto 1:", p1.getX(), p1.getY())
print("Punto 2:", p2.getX(), p2.getY())
print("Distancia:", d)
