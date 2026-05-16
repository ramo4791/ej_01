from p95SobrecargaDerecha import Vector2D
if __name__=='__main__':
    a = Vector2D(4, 5)
    b = Vector2D(2, 7)
    suma = a + b
    resta = a - b
    productoEscalar =  1.5 * a
    print(a)
    print(b)
    print('Suma a+b:',suma)
    print('Resta a-b',resta)
    print('Producto por un escalar  1.5 * a',productoEscalar)
    pe = b * 3
    print('Producto escalar de b * 3', pe)