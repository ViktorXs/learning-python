print("Lektion: Python Programmen Parameter übergeben")

## Bisher gelernt, wie Benutzereingaben mit input() funktionieren.
s = input("Benutzereingabe: ")
print()
print(str(len(s)) + " Benutzereingaben")

## Wenn ich Python Programme ausführe, kann ich in der CLI weitere Parameter übergebe:
# C:\Users\...\10_diverses\python_programs>C:\ProgramData\Anaconda3\python.exe argv.py "Hallo Welt!"

# Man kann diese Parameter abfangen mit dem Modul:
import sys

print(sys.argv)
## In der Ausgabe wird das Verzeichnis mit des auszufrührenden Programms angezeigt:
# ['C:/Users/.../10_diverses/python_programs/argv.py']

## Mit "Hallo Welt!" am Schluss in der CLI:
# 3 Benutzereingaben
# ['argv.py', 'Hallo Welt!']

## Sinn davon ist der, dass man über dem CLI dem Server Parameter übergeben kann

## Eine Datei als Parameter übergeben:
## Z.B. eine Beispiel.txt in die Kommandozeile ziehen

## Mit folgendem Code zählt das Programm die Zeilen in der Datei

if len(sys.argv) >= 2:  # gibt an, dass zwei Parameter übergeben werden. Den Pfad der Python Datei und der erwünschten Datei
    filename = sys.argv[1]  # der zweite Parameter ist die Datei

# Ab hier programmieren, was man mit der Datei gemacht werden soll, die man per CLI übergibt.
    file = open(filename, "r")

    counter = 0
    for line in file:
        counter = counter + 1
    print("The file has " + str(counter) + " lines of code.")
else:
    print("No valid file found.")

input("close me")

## Dadurch kann ich nun jede beliebige Datei dem Programm übergeben, und dieser zählt die Zeilen durch :)