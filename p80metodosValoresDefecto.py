from p80claseFecha import Fecha
if __name__=='__main__':
    fecha = Fecha(21,1,2020)
    print('Fecha en formato español {}'.format(fecha.formato()))
    print('Fecha en formato inglés {}'.format(fecha.formato('en')))