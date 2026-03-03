#con Programacionn Modular-Estructura
import math

#funcion para el promedio
def calcular_promedio(lista):
    suma = sum(lista)
    return suma / 10

#funcion para la desviacion
def calcular_desviacion(lista, promedio):
    suma_cuadrados = 0
    for x in lista:
        #usamos: (xi - promedio)^2
        suma_cuadrados += (x - promedio)**2
    
    #raiz de: (suma / n-1)
    resultado = math.sqrt(suma_cuadrados / 9)
    return resultado

print("Introduce 10 números:")
datos = []
for i in range(10):
    num = float(input(f"Número {i+1}: "))
    datos.append(num)

#llamamos a las funciones una por una
p = calcular_promedio(datos)
d = calcular_desviacion(datos, p)

print(f"El promedio es {p:.2f}")
print(f"La desviación estándar es {d:.5f}")

#######usamos POO#################

import math

#esta clase es como una caja que guarda los numeros
class Estadistica:
    def __init__(self, lista_numeros):
        #guardamos los 10 numeros dentro osea atributo privado
        self.__datos = lista_numeros

    def promedio(self):
        #sumamos los 10 numeros y dividimos entre 10
        suma = sum(self.__datos)
        return suma / 10

    def desviacion(self):
        prom = self.promedio()
        suma_cuadrados = 0
        
        #con esto calculamos la diferencia de cada numero con el promedio
        for x in self.__datos:
            suma_cuadrados = suma_cuadrados + (x - prom)**2
            
        #dividimos entre n-1 que es 9 y sacamos raiz
        resultado = math.sqrt(suma_cuadrados / 9)
        return resultado

print("Introduce 10 números uno por uno:")
mis_numeros = []

#pedimos los 10 números de forma manual
for i in range(10):
    n = float(input("Número: "))
    mis_numeros.append(n)

#creamos el objeto POO
calculadora = Estadistica(mis_numeros)

#mostramos los resultados
print("El promedio es:", calculadora.promedio())
print("La desviación estándar es:", calculadora.desviacion())
