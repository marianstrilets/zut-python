#Laboratorium 3
#Zadanie 4

def suma(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum




r = suma(2,4,5,3)
print(r)