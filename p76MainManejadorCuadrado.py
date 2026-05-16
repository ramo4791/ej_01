from p75ClaseManejadorCuadrado import ManejadorCuadrados
if __name__ == '__main__':
    mCuadrados = ManejadorCuadrados(3,5)
    mCuadrados.testManejadorCuadrados()
    print(mCuadrados)
    print('Cantidad de Cuadrados con perímetro > que perímetro promedio: {}'.format(mCuadrados.cantidadCuadrados()))