class Punto:
    __x: int
    __y: str
    def __init__(self, x, y):
        self.__x=x
        self.__y=y
class ManejadorPuntos:
    __puntos: list
    def __init__(self):
        self.__puntos=[]
    def agregar(self, unObjeto: Punto):
     self.__puntos.append(unObjeto)
if __name__=='__main__':
    unPunto=Punto(8, 9)
    unArreglo=ManejadorPuntos()
    unArreglo.agregar(unPunto)
    otroPunto=Punto(4, 5)
    unArreglo.agregar(otroPunto)