class Cuadrado:
    __lado: int

    def __init__(self, lado):
        self.__lado = lado

    def __str__(self):
        return  "%4d   %6.2f   %8.2f" % (self.__lado, self.perimetro(), self.superficie())
    
    def setLado(self, lado):
        self.__lado = lado

    def getLado(self):
        return self.__lado

    def perimetro(self):
        return self.__lado * 4

    def superficie(self):
        return self.__lado**2