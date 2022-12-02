import math

'''
 Zaimportuj moduł matematyczny, a następnie napisz skrypt którzy pobierze wartości dla dwóch 
 zmiennych x, y i wyznaczy oraz wyświetli wartość, dla podanej funkcji
'''

x = int(input("Wprowadz x: "))
y = int(input("Wprowadz y: "))

def fun1(x, y):
    result = math.e + math.log10(x**2 + 1) * ((x - 1)/(math.cos(y**3 - 1) + 6))
    return result
res = fun1(x,y)
print(res)