def pasajePorReferencia(l):
    print('En el interior de la función')
    print('Dirección de l: {}, valor: {} '.format(hex(id(l)), l))
    l[0] = 100
    l[1] = 200
    l[2] = 300
    print('Dirección de l: {}, valor: {} '.format(hex(id(l)), l))
if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print('En el programa principal')
    print('Dirección de lista: {}, valor: {} '.format(hex(id(lista)), lista))
    pasajePorReferencia(lista)
    print('Luego de probar función pasajePorRerencia')
    print('Dirección de lista: {}, valor: {} '.format(hex(id(lista)), lista))