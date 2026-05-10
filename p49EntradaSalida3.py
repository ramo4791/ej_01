#### FUNCIONES PARA CARGA DE DATOS DE PERSONA Y LISTA
from p48EntradaSalida2 import Persona

def crearPersona():
    print('Ingrese los siguientes datos:')
    dni = int(input('DNI:'))
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    sueldo = float(input('Sueldo: '))
    persona = Persona(dni, nombre, apellido, sueldo)
    return persona

def cargarPersonas(lista):
    for i in range(5):
        p = crearPersona()
        print(p)
        lista.append(p)
def calcularMaximoSueldo(lista):
    maximo = 0.0
    indiceMaximo = -1
    for i in range(len(lista)):
        if(lista[i].getSueldo()>maximo):
            maximo = lista[i].getSueldo()
            indiceMaximo = i
    return indiceMaximo

if __name__ == '__main__':
    listaPersonas = []
    cargarPersonas(listaPersonas)
    for i in range(len(listaPersonas)):
        listaPersonas[i].mostrarDatos()
    indice = calcularMaximoSueldo(listaPersonas)
    print('La persona que posee el mayor sueldo es {}, con un sueldo de {}'.format(listaPersonas[indice],
    listaPersonas[indice].getSueldo()))