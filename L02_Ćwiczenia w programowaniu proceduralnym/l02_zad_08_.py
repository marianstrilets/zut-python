

'''
Napisz program, który wyznaczy i wyświetli na ekranie sumę liczb naturalnych
mniejszych od n (liczba n podawana jest przez użytkownika) , które są zakończone liczbą 3 lub 14
'''

n = int(input(" Podaj liczbe n: "))
suma = 0
for i in range(n):
    if i % 10 == 3 or i % 100 == 14:
        suma += i
print(suma)
