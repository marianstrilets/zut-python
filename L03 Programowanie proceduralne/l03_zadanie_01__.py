#Laboratorium 3
#Zadanie 1

def secondsConverter(seconds):
    hours = 0
    minutes = 0
    if seconds >=60:
        minutes = int(seconds / 60)
        seconds = seconds % 60
        if minutes >= 60:
            hours = int(minutes / 60)
            minutes = minutes % 60
    return f"    {hours} godzin\n    {minutes} minut\n    {seconds} sekund"

print('-------------------------')
seconds = int(input("Podaj ilość sekund do obliczenia: "))
result = secondsConverter(seconds)
print(result)
print('-------------------------')
