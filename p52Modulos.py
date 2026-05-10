import sys
if __name__ == '__main__':
    print(dir(sys))
    print(sys.path)
    print(sys.winver)
    print(sys.version)
    print(sys.version_info)
print(sys.getrefcount(100))