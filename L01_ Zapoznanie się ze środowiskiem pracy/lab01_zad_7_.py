#LAB 1
#zadania 7
'''
Pobierz od użytkownika następujace informacje: kierunek studiów, rok studiów,
średnią uzyskaną w poprzednim semestrze studiów. Pamiętaj , aby dokonać odpowiedniej kon-
wersji pobranych danych. Wy±wietl pobrane informacje w następującej postaci: "Kierunek: xxx,
Rok studiów: yyy, Średnia: zzz " .
'''

faculty = input("Podaj kierunek studiow: ")
year = int(input("Podaj rok studiow: "))
average = int(input("Średnia ocena: "))

print(f"Kierunek: {faculty}", f"Rok studiów: {year}", f"Średnia: {average}", sep=", ")
