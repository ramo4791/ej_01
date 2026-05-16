from p80claseFecha import Fecha
if __name__=='__main__':
    fecha = Fecha()
    print('Fecha en formato español {}'.format(fecha.formato()))
    print('Fecha en formato inglés {}'.format(fecha.formato('en')))