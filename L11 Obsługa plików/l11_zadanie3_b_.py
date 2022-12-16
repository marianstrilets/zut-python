def isFloat(value):
    try:
        tmp = float(value)
        return tmp
    except ValueError:
        return value

def convertFloat(file):
    lista = []
    with open(file, 'r') as file1:
        for line in file1.readlines():
            line = line.replace('\n', '')
            lista.append(line.split(','))
            for i in range(0, len(lista[-1])):
                lista[-1][i] = isFloat(lista[-1][i])
        return lista
            
lista = []            
lista = convertFloat('./files/iris.txt')
print(lista)