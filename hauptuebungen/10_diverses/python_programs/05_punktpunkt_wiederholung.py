import os


with open(os.path.dirname(__file__) + "/folder/Test.txt") as file2:  # Windoof
    for line2 in file2:
        print(line2)
        print("ich glaub, es klappt")

with open(os.path.join(os.path.dirname(__file__), "folder", "subfolder", "Textdatei.txt"), "r") as file1:  # Unix
    for line1 in file1:
        print(line1)
        print("ich glaub, es klappt auch")

filevar = os.path.dirname(__file__) + "/folder/Test.txt"  # Windoof
print(filevar)

filevar = os.path.join(os.path.dirname(__file__), "folder", "Test.txt")  # Unix
print(filevar)

filevar = os.path.join(os.path.dirname(__file__), "folder")  # Unix
print(filevar)

#for file in os.listdir(filevar):
#    file_path = os.path.join(filevar, file)
#    if os.path.isdir(file_path):
#        print(file + " is an folder")
#    else:
#        print(file + " is a file")
#    print(file_path)
#    print("was los")

# Wiederholung

file_directory = os.path.join(os.path.dirname(__file__), "folder")
for file in os.listdir(file_directory):
    show_path = os.path.join(file_directory, file)
    if os.path.isdir(show_path):
        print(file + " is an folder")
    else:
        print(file + " is a file")

input("Put in ze input")
