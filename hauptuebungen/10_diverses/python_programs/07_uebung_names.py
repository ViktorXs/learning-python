# Aufgabe:
#
# Im Ordner "names" gibt es einige Textdateien, die Namen von Personen enthalten (zufällig generiert).
#
# Aufgabe:
#   Schreibe ein Programm, welches alle Textdateien aus dem Ordner "names" einliest, und ermittelt, wie oft der Vorname
#   "Max" insgesamt in allen Dateien vorkommt.
#
# Beispiel:
#   Käme der Name "Max" in der Datei "1.txt" 1x vor, und in der Datei "2.txt" 2x, sonst aber nie, soll das Programm
#   die Zahl 3 ausgeben.

import os


names_folder = os.listdir(os.path.join(os.path.dirname(__file__), "names"))  # Lösung zur Hilfe genommen: os.listdir
counter = 0
print(names_folder)
print("öh")
for files in names_folder:
    # with open(files, "r", encoding="utf-8") as names: #  Dies wäre mein Weg, aber es funktioniert leider nicht.

    #  Folgendes ist der Lösungsansatz der Musterlösung mit meinem Code als Vorlage:
    f = os.path.join(os.path.dirname(__file__), "names", files)

    # Ab hier wieder mein Code:
    with open(f, "r", encoding="utf-8") as names:
        for lines in names:
            # if "Max" in lines:
            #     counter = counter + 1
            # Ergebnis: 31 = Falsch. Maximilians und überall sonst, wie Nachnamen werden auch mitgezählt!

            # Nach Musterlösung, weil nur Vorname "Max" gesucht wird.
            stripped = lines.strip().split(" ")  # Namen aufteilen
            firstname = stripped[0]  # Nur erste Spalte

            if firstname == "Max":  # Wenn erste Spalte == "Max", zähle hoch. Keine Maximilians, weil ==
                counter = counter + 1

print("There are: " + str(counter) + " Maxes out there!")
input("Put me in!")

# Schwere Geburt ^^

# Der Code nun sauber:
names_folder = os.listdir(os.path.join(os.path.dirname(__file__), "names"))
counter = 0

for files in names_folder:
    f = os.path.join(os.path.dirname(__file__), "names", files)
    with open(f, "r", encoding="utf-8") as names:
        for lines in names:
            firstname = lines.strip().split(" ")[0]
            if firstname == "Max":
                counter = counter + 1

print("The files are containing: " + str(counter) + " Maxes.")
input("Put it in like its hot.")
