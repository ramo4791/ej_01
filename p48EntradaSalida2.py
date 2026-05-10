class Persona:
    __dni: int
    __nombre: str
    __apellido: str
    __sueldo: float

    def __init__(self, dni, nombre, apellido, sueldo = 35000.0):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = sueldo

    def getSueldo(self):
        return self.__sueldo
    
    def __str__(self):
        return 'Apellido y nombre: '+self.__apellido+', '+self.__nombre
    
    def mostrarDatos(self):
        print('Nombre {}, Apellido {}, DNI {}, sueldo {}'.format(self.__nombre, self.__apellido, self.__dni, self.__sueldo))
