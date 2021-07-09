import os

# Herumgespiele

print()
print(__file__)
print(os.path.dirname(__file__))
print("testz")
print(os.path.dirname("./learning-python"))


with open(os.path.dirname(__file__) + "/Beispieldatei.txt", "r") as file:
    for line in file:
        print(line)

input("Press any key to close.")

