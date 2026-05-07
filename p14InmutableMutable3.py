def mutable():
    mi_lista = [1,2,3,4,5]
    print('Dirección de memoria {}, valor almacenado: {}'.format(hex(id(mi_lista)), mi_lista))
if __name__== '__main__':
    mutable()