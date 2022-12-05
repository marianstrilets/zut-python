#Laboratorium 3
#Zadanie 7

n = int(input("Podaj liczbe: "))

def silnia_rec(n):
    if n>1:
        return n * silnia_rec(n-1)
    elif n in (0,1):
        return 1

def silnia_iter(n):
    tmp = 1
    if n in (0,1):
        return 1
    else:
        for i in range(2,n+1):
            tmp *= i
        return tmp

result1 = silnia_rec(n)
result2 = silnia_iter(n)
print("Suma : ", result1)
print("Suma : ", result2)