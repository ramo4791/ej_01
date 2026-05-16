class Fecha:
    __dia: int
    __mes: int
    __anio: int
    def __init__(self, d=1,m=1,a=1900):
        self.__dia=d
        self.__mes=m
        self.__anio=a
        
    def formato(self, tipo='es'):
        '''por defecto genera  la fecha en formato español, dd/mm/aaaa,
            si se pasa el parámetro tipo con el valor ‘en’, lo hará en formato
            inglés, aaaa/mm/dd'''
        formato = None
        if tipo=='en':
            formato =  '{}/{}/{}'.format(self.__anio, self.__mes, self.__dia)
        else:
            formato = '{}/{}/{}'.format(self.__dia, self.__mes, self.__anio)
        return formato