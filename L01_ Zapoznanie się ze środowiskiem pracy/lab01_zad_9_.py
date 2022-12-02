#LAB 1
#zadania 9

'''
Wykorzystujac funkcje konwersji danych (int () , float () ) oraz funkcję input(), utwórz
skrypt , który pobierze od użytkownika jego wzrost w centymetrach oraz wagę w gramach, a na-
stępnie wyswietli wagę w kilogramach i wzrost w metrach wraz ze stosownym komunikatem oraz
obliczy wskażnik BMI i go wy±wietli.
'''


wzrost_cm = int(input("Wzrost w cm: "))
waga_g = int(input("Waga w gramach: "))
waga_kg = waga_g/1000 
wzrost_m = wzrost_cm / 100 
print("Twoja waga w kg: " + str(waga_kg))
print("Twoj wzrost w kilogramach: " + str(wzrost_m))

bmi = waga_kg / wzrost_m

print("BMI: " + str(bmi))