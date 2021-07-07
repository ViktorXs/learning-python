print("Sinnlosrechner")


age1 = int(input("Bitte gebe dein Alter ein: "))
if age1 >= 30:
    print()
    print(str(age1) + " Jahre??? Uff, das ist alt.")
else:
    print()
    print('Die 30 ist die Schwelle zwischen "Jung" und "Uralter Sack".')
    print("Sieh zu, dass du dein Leben bis dahin genießt. Ab da an geht es nur noch bergab!")

print()
number = str(input("Bitte gebe eine beliebige Zahl ein: "))
print(number)

print()
print("Dein Alter + deine beliebige Zahl: ")
combined = int(age1) + int(number)
print(combined)

print()
input("Drücke eine beliebige Taste, um das Programm zu beenden.")