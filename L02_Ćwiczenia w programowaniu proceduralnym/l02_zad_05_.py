

'''
Napisz program drukujący na ekranie trójkąt o wysokośći podanej przez użytkownika. 
Przykładowy trójkąt o wysokości 4
'''

x = int(input("Wprowadz wysokosc: "))


for i in range(x):
    print("*" * (i+1))