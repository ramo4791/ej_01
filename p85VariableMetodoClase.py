class TibetanSpaniel:
    # variables de clase
    '''todos los perros de la raza Spaniel Tibetano
    tienen las mismas características    '''
    __nombreCientifico = "Canis lupus familiaris"
    __familia = "Companion, herding"
    __areaDeOrigen = "Tibet"
    __tasaDeAprendizaje = 9
    __obediencia = 3
    __resolucionDeProblemas = 8
    __nombre: str
    __habilidad: int
    __jugueteFavorito: str

    def __init__(self, nombre, habilidad, jugueteFavorito):
        self.__nombre = nombre
        self.__habilidad = habilidad
        self.__jugueteFavorito = jugueteFavorito

    def __str__(self):
        return 'Nombre %s, habilidad %d, juguete favorito %s, obediencia %d' % (self.__nombre, self.__habilidad, self.__jugueteFavorito, self.getObediencia())
    
    #Métodos de instancia
    def getNombre(self):
        return self.__nombre
    
    def getHabilidad(self):
        return self.__habilidad
    
    def getJugueteFavorito(self):
        return self.__jugueteFavorito
    
    #Métodos de clase
    @classmethod
    def getNombreCientifico(cls):
        return cls.__nombreCientifico
    
    @classmethod
    def getFamilia(cls):
        return cls.__familia
    
    @classmethod
    def getAreaDeOrigen(cls):
        return cls.__areaDeOrigen
    
    @classmethod
    def getTasaDeAprendizaje(cls):
        return cls.__tasaDeAprendizaje
    
    @classmethod
    def getObediencia(cls):
        return cls.__obediencia
    
    @classmethod    
    def setObediencia(cls, valor):   
        cls.__obediencia = valor
        
    @classmethod
    def getResolucionProblemas(cls):
        return cls.__resolucionDeProblemas
    
    @classmethod
    def verRaza(cls):
        print('Características de la Raza')
        print('Nombre Científico: '+cls.getNombreCientifico())
        print('Familia: '+cls.getFamilia())
        print('Área de Origen: '+cls.getAreaDeOrigen())
        print('Tasa de Aprendizaje:'+str(cls.getTasaDeAprendizaje()))
        print('Obediencia: '+str(cls.getObediencia()))
        print('Tasa de Resolución de problemas:'+str(cls.getResolucionProblemas()))