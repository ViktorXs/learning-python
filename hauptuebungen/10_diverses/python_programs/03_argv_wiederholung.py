import sys

print("Der Zeilenzaehler Deluxe Light Demo Freeware")

if len(sys.argv) >= 2:
    filename = sys.argv[1]

    with open(filename, "r") as file:
        counter = 0

        for line in file:
            counter = counter + 1
        print("The file has " + str(counter) + " lines of code.")
else:
    print("File not found.")

input("Press any key to close.")
