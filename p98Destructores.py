class CicloDeVida:
    __nombre: str
    def __init__(self, nombre):
        print('Hola: ',nombre)
        self.__nombre = nombre

    def vida(self):
        print(self.__nombre)

    def __del__(self):
        print('Chau... ',self.__nombre)

def funcion():
    o = CicloDeVida('Violeta')

if __name__=='__main__':
    objeto = CicloDeVida('Carlos')
    objeto.vida()
    del objeto
    funcion()