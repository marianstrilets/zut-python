#Laboratorium 3
#Zadanie 5

#Nie do końca zrobiłem zadania!!!

import math as m

def volume(type, **kwargs):
    print(type)
    print(kwargs)
    if type == "kula":
        print(4/3 * m.pi + kwargs['k']**3)
    elif type == "prostopadloscianu":
        print(kwargs['a'] * kwargs['b'] * kwargs['v'])
