#Laboratorium 2
#zadanie 8

n = int(input(" Podaj liczbe n: "))
suma = 0
for i in range(n):
    if i % 10 == 3 or i % 100 == 14:
        suma += i
print(suma)
