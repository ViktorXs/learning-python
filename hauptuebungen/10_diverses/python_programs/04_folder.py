# 1. In Python mit relativen Ordnern arbeiten
import os  # Durch das os-Modul mit dem Betriebssystem kommunizieren

print("Der Auflister von Dateien direkt um deine Ecke.")
print(os.listdir("."))  # Der aktuelle Pfad bezieht sich auf den Ort aus dem das Python Programm gestartet wurde.
# z.B. im cli ist der aktuelle Ort der Desktop und man öffnet von dort aus die python.exe und damit dieses Programm.


# 2. Eine Datei öffnen.
with open("Beispieldatei.txt", "r") as file1:  # relativer Pfad. Sucht dort, von wo aus das Programm gestartet wird.
    for line1 in file1:
        print(line1)

with open("C:/Users/PC2020/Arbeitsverzeichnis/Tutorials & Kurse/Udemy Python Bootcamp/learning-python/hauptuebungen/"
          "10_diverses/python_programs/Beispieldatei.txt", "r") as file2:  # Absoluter Pfad.
    for line2 in file2:
        print(line2)

# 3. Wenn absolut zu genau und relativ zu ungenau ist, muss der Standort der Programmdatei ermittelt werden.
print(__file__)  # Enthält den absoluten Pfad zum Standort der Programmdatei.
print(os.path.dirname(__file__))  # damit wird der absolute Pfad bis einschl. des Ordners ohne Datei angezeigt.

with open(os.path.dirname(__file__) + "/Beispieldatei2.txt", "r") as file3:  # Datei aus ermittelten Pfad öffnen.
    for line3 in file3:
        print(line3)

# 3.1 Plattformübergreifend freundlich gestalten, weil bei Windows \-Schrägstrich und in unix /-Schrägstriche sind.
# .join setzt den entsprechenden Schrägstrich ran.
with open(os.path.join(os.path.dirname(__file__), "Beispieldatei3.txt"), "r") as file4:
    for line4 in file4:
        print(line4)

input("Press any key to close.")
