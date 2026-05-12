from claseLibro import Libro
from claseManejadorLibro import ManejadorLibros

if __name__=='__main__':
    ml = ManejadorLibros()
    ml.testLibros()
    print('Colección de libros inicial')
    print(ml)
    idLibro = int(input('Ingrese idLibro a Buscar'))
    indice=ml.buscarLibro(idLibro)
    if indice == None:
        print('El idLibro {} no corresponde a un libro de la colección'.format(idLibro))
    else:
        libro = ml.getLibro(indice)
        print ('idLibro: {}, título: {}, autor: {}'.format(idLibro, libro.getTitulo(),libro.getAutor()))
    idLibro = int(input('Ingrese idLibro a Borrar'))
    indice = ml.borrarLibro(idLibro)
    if indice != None:
        libro = ml.buscarLibro(indice)
        print('El libro {} se borró de la colección'.format(libro.getTitulo()))
    else:
        print('El idLibro {}, no corresponde a un libro de la colección'.format(idLibro))
    print('Colección de libros final')
    print (ml)