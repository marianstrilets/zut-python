#Laboratorium 3
#Zadanie 8

n = int(input("Podaj liczbe: "))

def fibonaciego(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaciego(n-1)+fibonaciego(n-2)+fibonaciego(n-3)

result = fibonaciego(n)
print(result)

