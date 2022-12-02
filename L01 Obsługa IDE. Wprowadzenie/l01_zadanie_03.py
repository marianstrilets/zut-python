#Laboratorium 1
#zadanie 3

wzrost_cm = int(input("Wzrost w cm: "))
waga_g = int(input("Waga w gramach: "))
waga_kg = waga_g/1000 
wzrost_m = wzrost_cm / 100 
print("Twoja waga w kg: " + str(waga_kg))
print("Twoj wzrost w kilogramach: " + str(wzrost_m))

bmi = waga_kg / wzrost_m

print("BMI: " + str(bmi))