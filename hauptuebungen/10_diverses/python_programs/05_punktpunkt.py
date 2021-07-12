import os

# os.path.join und os.listdir
folder = os.path.join(os.path.dirname(__file__), "folder")  # /-Universelles Schrägstrich
print("Test1")
print(folder)
print()

# vs

folder = os.path.dirname(__file__) + "/folder"  # \-Windows Schrägstrich
print("Test2")
print(folder)
print()


# Weiter gehts.
folder = os.path.join(os.path.dirname(__file__), "folder")  # In den ordner "folder" reingehen.
print("Übung")
print(folder)
print(os.listdir(folder))
print()

folder = os.path.join(os.path.dirname(__file__), ".")  # Aktueller Ordner.
print(folder)
print(os.listdir(folder))
print()

# Punktpunkt
folder = os.path.join(os.path.dirname(__file__), "..")  # Gehe einen Ordner hoch.
print(folder)
print(os.listdir(folder))
print()

print("Inhalte anzeigen")
folder = os.path.join(os.path.dirname(__file__), "folder")
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)  # Gesamten Pfad jeder Datei anzeigen

    if os.path.isdir(file_path):  # Abfragen ob es sich um den Dateipfad um einen Ordner handelt, oder nicht.
        print(file + " is an folder.")  # Sinnvoll, wenn z.B. eine Datei keine Dateiendung hat.
    else:
        print(file + " is a file")
    print()
    print(file)
    print(file_path)  # Gesamten Pfad jeder Datei anzeigen

print()

# Im Verzeichnis beliebig navigieren.
filename = os.path.join(os.path.dirname(__file__), "folder", "..", "folder", "subfolder", "..", "subfolder", "Textdatei.txt")
print(filename)
print()
with open(filename, "r") as file1:
    for line in file1:
        print(line)

input("1. Put in your input.")

# Im Verzeichnis beliebig navigieren. Majk's Tipp.
directories = (os.path.dirname(__file__), "folder", "subfolder", "Textdatei.txt")
filename = os.path.join(*directories)  # mit * entpacken

with open(filename, "r") as file1:
    for line in file1:
        print(line)

input("press any key")