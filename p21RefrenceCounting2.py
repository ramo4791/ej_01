def ejemploRefcount():
    uno = 1
    dos = uno
    tres = uno
    cuatro = 1
    #print('Direccion de {}, {}'.format(hex(id(uno)),'uno'))
    for k, v in locals().items():
        print('Direccion de {}, {}'.format(k, hex(id(v))))
    """lista=[1,2,3,4,1]
    for i in range(len(lista)):
        print('Dirección de valor {}, {}'.format(lista[i], hex(id(lista[i]))))"""

if __name__ == '__main__':
    ejemploRefcount()