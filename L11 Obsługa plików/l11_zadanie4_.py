

filePath = r'./files/iris.txt'
lista = []

file1 = open(filePath, 'r')

for line in file1.readlines():
    line = line.replace('\n', '')
    lista.append(line.split(','))
    for i in range(0, len(lista[-1])):
        try:
            lista[-1][i] = float(lista[-1][i])
        except:
            pass  
    
print(lista)
file1.close()

file2 = open('./files/zad4.txt', 'w')
cnt = 0

for row in lista:
    if row[0] > 5:
        cnt += 1
        s = ''
        for elem in row:
            s += str(elem) + ' '
        s += '\n'
        file2.write(s)
file2.close()

