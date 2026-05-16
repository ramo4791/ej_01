from p85VariableMetodoClase import TibetanSpaniel
if __name__ == '__main__':
    TibetanSpaniel.verRaza()
    miSpaniel = TibetanSpaniel('Jhon', 7,'hueso')
    otroSpaniel = TibetanSpaniel('Coco',8,'minion')
    print(miSpaniel)
    print('Cambio de una variable de clase')
    TibetanSpaniel.setObediencia(9)
    print(miSpaniel)
    print(otroSpaniel)