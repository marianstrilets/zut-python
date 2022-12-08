
file_path = './files/zad1.txt'

print('-------------1---------------')

file_obj = open(file_path, 'r')
print(file_obj.read())
file_obj.close

print('-------------2---------------')
with open(file_path, 'r') as obj1:
    print(obj1.read())
    
print('--------')
with open(file_path, 'r') as obj2:
    print(obj2.readline())
    
print('--------')
with open(file_path, 'r') as obj3:
    for line in obj3:
        print(line, end='')
        print('---', line, end='')

