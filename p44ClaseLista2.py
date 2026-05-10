from p43ClaseLista import Punto
class ManejadorPuntos:
    __puntos: list

    def __init__(self):
        self.__puntos=[]

    def agregarPunto(self, unPunto):
        self.__puntos.append(unPunto)

    def mostrarPuntos(self):
        for punto in self.__puntos:
            punto.mostrarDatos()

    def testListaPuntos(self):
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

    def getUnPunto(self, indice):
        return self.__puntos[indice]
    
    def calcularDistanciasP0(self, unPunto):
        for i in range(len(self.__puntos)):
            distancia = unPunto.distanciaEuclidea(self.__puntos[i])
            print('Distancia del punto {} al punto {} es {}'.format(unPunto, self.__puntos[i], distancia))
            
if __name__ == '__main__':
    listaPuntos = ManejadorPuntos()
    listaPuntos.testListaPuntos()
    punto0 = listaPuntos.getUnPunto(0)
    listaPuntos.calcularDistanciasP0(punto0)
    listaPuntos.mostrarPuntos()