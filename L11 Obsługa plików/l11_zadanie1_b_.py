
filePath = r'./files/zad1.txt'
lista = []

file1 = open(filePath, 'r')
line = file1.readline()
while line != '':
    lista.append(line)
    line = file1.readline()
file1.close()

print(lista)
