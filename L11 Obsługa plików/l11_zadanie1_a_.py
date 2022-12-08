
filePath = r'./files/zad1.txt'
lista = []

file1 = open(filePath, 'r')
for line in file1:
    lista.append(line)
file1.close()


#---------------- Wyświetłanie --------------------
print('------------ 1 ------------')
print(lista)
print('------------ 2 ------------')
print(*(i for i in lista), sep='')
print('------------ 3 ------------')
for i in lista:
    print(i, end='')