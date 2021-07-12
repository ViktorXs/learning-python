import os


filepath = os.path.join(os.path.dirname(__file__), "umlaute.txt")
with open(filepath, "r") as file1:
    for line1 in file1:
        print(line1)

with open(filepath, "r", encoding="utf-8") as file1:  # ob utf-8 oder UTF-8, ist egal
    for line2 in file1:
        print(line2)

file_write = os.path.join(os.path.dirname(__file__), "umlaute_neu1.txt")
with open(file_write, "w") as file2:  # Umlaute ohne UTF-8 in Datei schreiben
    file2.write("Mญller")  # Decoding Exception
    print("Ok.")

file_write = os.path.join(os.path.dirname(__file__), "umlaute_neu1_utf-8.txt")
with open(file_write, "w", encoding="utf-8") as file3:  # Umlaute mit UTF-8 in Datei schreiben
    file3.write("Müller")
    print("Ok too.")

file_write = os.path.join(os.path.dirname(__file__), "umlaute_neu2_utf-8.txt")
with open(file_write, "w", encoding="utf-8") as file4:
    file4.write("Mญller")
    print("Ok.")

input("Putting the put in.")
# Es ist ratsam das Encoding immer auf utf-8 zu setzen, wenn man dateien liest und schreibt.
