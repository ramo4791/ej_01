def main():
    i = 200
    j = 200
    print('dirección del objeto apuntado por i = ', hex(id(i)))
    print('dirección del objeto apuntado por j =', hex(id(j)))
    i = i + 1
    print('dirección del objeto apuntado por i incrementado en 1 =', hex(id(i)))
    print('dirección del objeto apuntado por j antes de incrementar =', hex(id(j)))
    j = j + 1
    print('dirección del objeto apuntado por j incrementado en 1 = ', hex(id(j)))
if __name__ == '__main__':
    main()
