#LAB 1
#zadania 8

'''
Pobierz od użytkownika: adres zamieszkania, kod pocztowy i miasto. Wy±wietl
pobrane informacje w jednej linii rozdzielając je przecinkami. W tym celu zastosuj wywołanie
funkcji print z odpowiednim parametrem.
'''



adress = input("Podaj adress zamieszkania: ")
postcode = input("Podaj kod pocztowy: ")
city = input("Podaj miasto: ")

print(f"Twój adress: {adress}", f"Twój kod pocztowy: {postcode}", f"Twoje miasto: {city}", sep="\n", end="\n============================================")