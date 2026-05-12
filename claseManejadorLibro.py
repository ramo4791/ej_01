import csv
from claseLibro import Libro

class ManejadorLibros:
    __listaLibros = list

    def __init__(self):
        self.__listaLibros = []

    def agregarLibro(self,unLibro):
        self.__listaLibros.append(unLibro)
    def getLibro(self, indice):
        return self.__listaLibros[indice]
    def buscarLibro(self, clave):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(self.__listaLibros):
            if self.__listaLibros[indice].getIdLibro()==clave:
                bandera=True
                valorDeRetorno=indice
            else:
                indice+=1
        return valorDeRetorno
    
    def borrarLibro(self, clave):
        indice = self.buscarLibro(clave)
        if indice != None:
            self.__listaLibros.pop(indice)
        return indice
    
    def __str__(self):
        s = ""
        for libro in self.__listaLibros:
            s += str(libro) + '\n'
        return s
    def testLibros(self):
        archivo = open('librosPOO.csv', encoding='utf-8')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera'''
                bandera = not bandera
            else:
                idLibro = int(fila[0])
                titulo = fila[1]
                autor = fila[2]
                edicion = fila[3]
                editorial = fila[4]
                anio = int(fila[5])
                unLibro = Libro(idLibro,titulo,autor,edicion, editorial,anio)
                self.agregarLibro(unLibro)
        archivo.close()