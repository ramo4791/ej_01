class Billetera_Virtual:
    __titular : str
    __num_celular : str
    __alias : str
    __saldo : float
    __fecha : str

    def __init__ (self, t,n,a,s):
        self.__titular = t
        self.__num_celular = n
        self.__alias = a
        self.__saldo = s
    
    def __str__(self):
        return 'Nombre : ' + self.__titular
    def mostrar_datos (self):
        print ( 'Titular {}, Num Celular : {}, Alias : {}, Saldo : {}', format(self.__titular, self.__num_celular,
        self.__alias, self.__saldo))
    