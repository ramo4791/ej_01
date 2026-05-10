class Persona:
    __dni: int
    __nombre: str
    __apellido: str
    __telefono: int

    def __init__(self, dni, nombre, apellido, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
    
    def mostrarDatos(self):
        print(f"DNI: {self.__dni}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Teléfono: {self.__telefono}")

if __name__ == '__main__':
    listaPersonas = []
    unaPersona = Persona(11203567,'Nahuel', 'Alfaro', 9963)
    listaPersonas.append(unaPersona)
    otraPersona = Persona(1234533,'Liza', 'Laine', 45678)
    listaPersonas.append(otraPersona)
    #componente a componente como si fuera un arreglo
    for i in range(len(listaPersonas)):
        listaPersonas[i].mostrarDatos()
    #iterador
    for objeto in listaPersonas:
        objeto.mostrarDatos()