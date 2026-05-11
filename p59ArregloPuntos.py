#Arreglo de Puntos (I)
import numpy as np

from clasePunto import Punto

class arregloNumPy:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __puntos: np.ndarray

    def __init__(self, dimension, incremento=5):
        self.__puntos = np.empty(dimension, dtype=Punto)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarPunto(self, unPunto):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__puntos.resize(self.__dimension, refcheck=False)
        self.__puntos[self.__cantidad]=unPunto
        self.__cantidad += 1

    def getUnPunto(self, indice):
        return self.__puntos[indice]
    
    def mostrarPuntos(self):
        for i in range(self.__cantidad):
            self.__puntos[i].mostrarDatos()
    
    def calcularDistanciasP0(self, unPunto):
        for i in range(self.__cantidad):
            distancia = unPunto.distanciaEuclidea(self.__puntos[i])
            print('Distancia del punto {} al punto {} es {:.2f}'.format(unPunto, self.__puntos[i], distancia))
            
    def testArregloPuntos(self):
        p1 = Punto(4, 5)
        p2 = Punto(3, 4)
        p3 = Punto(-9, 5)
        p4 = Punto(3, 2)
        p5 = Punto(1, 7)
        self.agregarPunto(p1)
        self.agregarPunto(p2)
        self.agregarPunto(p3)
        self.agregarPunto(p4)
        self.agregarPunto(p5)

if __name__ == '__main__':
    arregloPuntos = arregloNumPy(3,10)
    arregloPuntos.testArregloPuntos()
    punto0 = arregloPuntos.getUnPunto(0)
    arregloPuntos.calcularDistanciasP0(punto0)
    arregloPuntos.mostrarPuntos()