#Laboratorium 3
#Zadanie 3

import math as m

f = lambda x : m.sin(x + 1) + m.cos(x**4)

lista = [f(x) for x in range(-5, 3)]

print(lista)