import csv


class NamesCounter:
    path = "C:/Users/PC2020/Arbeitsverzeichnis/Tutorials & Kurse/Udemy Python " \
           "Bootcamp/learning-python/hauptuebungen/data/names.csv"
    try:
        with open(path, newline="") as file:
            namereader = csv.reader(file, delimiter=",")
            counter = 0
            names = set()

            for line in namereader:
                if counter != 0:
                    names.add(line[1])
                counter = counter + 1
            print(len(names))
    except FileNotFoundError:
        print("No such file found! Check directory.")
