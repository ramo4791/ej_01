class Punto:
    __x: int
    __y: int

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def setX(self, v):
        self.__x = v

    def getX(self):
        return self.__x
    def setY(self, v):
        self.__y = v

    def getY(self):
        return self.__y

    def mostrarDatos(self):
        print("(x,y) = (",self.__x,',', self.__y,")")

if __name__=='__main__':
    unPunto = Punto(3,4)
    otroPunto = Punto(4,7)
    unPunto.mostrarDatos()
    otroPunto.mostrarDatos()
    #tercerPunto = Punto()
    #tercerPunto.mostrarDatos()


