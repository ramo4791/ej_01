def pasajePorValor(x):
    print('En el interior de la función')
    print('Dirección de x antes de incrementar: {}, valor: {} '.format(hex(id(x)),x))
    x = x + 1
    print('Dirección de x incrementado: {}, valor: {} '.format(hex(id(x)),x))
if __name__ == '__main__':
    v = 100
    pasajePorValor(v)
    print('En el programa principal')
    print('Dirección de variable: {}, valor: {} '.format(hex(id(v)), v))