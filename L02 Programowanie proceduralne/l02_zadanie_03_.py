#Laboratorium 2
#zadanie 3

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


