#Cuando se conocen los elementos que hay dentro de un módulo, se pueden importar los que se utilizarán, 
#haciendo uso de la sentencia from:

from sys import path, winver, version, version_info, getrefcount
if __name__ == '__main__':
    print(path)
    print(winver)
    print(version)
    print(version_info)
    print(getrefcount(100))

#Con la misma sentencia from, puede asignarse un alias a los elementos importados:
""" from p43ClaseLista import Punto as p
if __name__ == '__main__':
    print(dir(p))
    unPunto = p(2,3)
    unPunto.mostrarDatos() """