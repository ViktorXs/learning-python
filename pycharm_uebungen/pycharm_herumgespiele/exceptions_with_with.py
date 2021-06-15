# with open()
try:
    print(5 / 0)
    with open("existiert_nicht.txt", "r") as file:
        print(file)
except FileNotFoundError:
    print("No such file found.")
except ZeroDivisionError:
    print("Are you stupdi lol dhas ddolmf")

# file = open()
try:
    file = open("existiert_immernoch_nicht.txt", "r")
    print(file)
    print("Test")
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
