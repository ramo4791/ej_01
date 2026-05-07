def main():
    mi_variable = 'uno, dos'
    print('Dirección de memoria {}, valor almacenado: {}'.format(hex(id(mi_variable)), mi_variable))
if __name__== '__main__':
    main()