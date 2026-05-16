from p77ClasePunto import Punto
if __name__=='__main__':
    unPunto = Punto(3,4)
    print('Direccion de memoria de instancia unPunto: {}'.format(hex(id(unPunto))))
    unPunto.mostrarDatos()