

'''
 Napisz skrypt , który pobierze od użytkownika trzy wartości x, y, z oraz numer
opcji c. Jeśli c == 1 zwróć ich sumę, jeżeli c == 2 różnicę, dla c == 3 iloczyn, a w przeciwnym
razie iloraz . Upewnij się, że nie dojdzie do dzielenia przez 0 , jeśli taka sytuacja miała by miejsce,
wyświetl odpowiedni komunikat.

'''


x = int(input("Wprowadz X: "))
y = int(input("Wprowadz Y: "))
z = int(input("Wprowadz Z: "))

opcja = int(input("Wprowadz opcje: "))

if opcja == 1:
    print(x + y + z)
elif opcja == 2:
    print(x - y - z)
elif opcja == 3:
    print(x * y * z)
else:
    if y != 0 and z != 0:
        print(x / y / z)
    else: 
        print("Dzilelenie przez zero!!!")


