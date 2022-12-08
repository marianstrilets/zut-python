
filePath = r'./files/iris.txt'
lista = []

file1 = open(filePath, 'r')


for line in file1.readlines():
    line = line.replace('\n', '')
    lista.append(line.split(','))

print(lista)

file1.close()