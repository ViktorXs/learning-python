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
age2 = str(input("Bitte gebe eine beliebige Zahl ein: "))
print(age2)

print()
print("Dein Alter + deine beliebige Zahl: ")
print(int(age1) + int(age2))

print()
input("Druecke eine beliebige Taste, um das Programm zu beenden.")