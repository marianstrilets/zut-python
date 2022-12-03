#Laboratorium 3
#Zadanie 2

from cmath import log
import math as m

def f(x, n = 10, k =2):
    return log(x**2 + 5) * (k + 1) * x

r = f (x= 2, k =7)
print(r)
