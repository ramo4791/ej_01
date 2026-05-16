import sys
def funcion(a):    
    # 3 referencias    
    # variable comidas, argumento formal a, getrefcount y pila de funciones de Python    
    print('Cantidad de referencias de a: ',sys.getrefcount(a))   
if __name__ == '__main__':    
    comidas = []        
    # 2 referencias,  1 por la variable comida y una por getrefcount
    print('Antes de llamar a la función')    
    print('Cantidad de referencias de comidas: ',sys.getrefcount(comidas))   
    funcion(comidas)        
    # 2 referencias, las propias del alcance de la función se destruyen    
    print('Después de llamar a la función')    
    print('Cantidad de referencias de comidas: ',sys.getrefcount(comidas))