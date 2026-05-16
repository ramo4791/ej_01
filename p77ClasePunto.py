class Punto:
    __x = -1
    __y = 0
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    def __str__(self):
        return '({}, {})'.format(self.__x, self.__y)
    def mostrarDatos(self):
        print("(x,y) = (",self.__x,',', self.__y,")")
        print('Dirección de memoria de self en mostrarDatos:{}'.format(hex(id(self))))