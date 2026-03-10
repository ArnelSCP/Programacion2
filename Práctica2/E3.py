import math

class Vector3D:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def suma(self,v):
        return Vector3D(
            self.x + v.x,
            self.y + v.y,
            self.z + v.z
        )


    def escalar(self,r):
        return Vector3D(
            r*self.x,
            r*self.y,
            r*self.z
        )


    def longitud(self):
        return math.sqrt(
            self.x**2 +
            self.y**2 +
            self.z**2
        )


    def normal(self):
        l = self.longitud()

        return Vector3D(
            self.x/l,
            self.y/l,
            self.z/l
        )


    def productoEscalar(self,v):
        return (
                self.x*v.x +
                self.y*v.y +
                self.z*v.z
        )

    def productoVectorial(self,v):

        cx = self.y*v.z - self.z*v.y
        cy = self.z*v.x - self.x*v.z
        cz = self.x*v.y - self.y*v.x

        return Vector3D(cx,cy,cz)

a = Vector3D(1,2,3)
b = Vector3D(4,5,6)

c = a.suma(b)

print("Suma:", c.x, c.y, c.z)

print("Producto escalar:", a.productoEscalar(b))

pv = a.productoVectorial(b)

print("Producto vectorial:", pv.x, pv.y, pv.z)
