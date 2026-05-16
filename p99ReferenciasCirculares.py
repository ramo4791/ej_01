class A:
    __b: None
    def __init__(self, unObjetoB):
        print(type(unObjetoB))
        self.__b=unObjetoB
    def __del__(self):
        print('Chau objeto A')
class B:
    __a: None
    def __init__(self):
        self.__a=A(self)
    def __del__(self):
        print('Chau Objeto B')
def funcionCreaB():
    b = B()
    #del b
if __name__=='__main__':
    funcionCreaB()