from datetime import datetime


def request_time():
    print(datetime.now())


request_time()

print(datetime.now())
datetime.now()

# Einen Tag bestimmen
a_day = datetime(2022, 2, 24, 13,)  # Minuten und Sekunden werden als Nullen angezeigt, wenn kein Wert
print(a_day)
now = datetime.now()
print(now)

# Einzelne Werte
print("The date is "
      + str(a_day.day) + "."
      + str(a_day.month) + "."
      + str(a_day.year) + " and the time is "
      + str(a_day.hour) + ":"
      + str(a_day.minute) + " o' clock.")

# Unix timestamp
print("Unix Timestamp: "
      + str(a_day.timestamp()))

# Differenz ausrechnen
a_day = datetime(2022, 2, 24, 13,)  # Minuten und Sekunden werden als Nullen angezeigt, wenn kein Wert
now = datetime.now()

difference_unix = a_day.timestamp() - now.timestamp()
diff_for_humans = a_day - now

print(difference_unix)
print(diff_for_humans)

# Einzelne datetime Funktionen
from datetime import date, time


my_day = date(1987, 2, 24)
my_time = time(7, 13, 0, 123456)

print("Day: " + str(my_day) + ". Time: " + str(my_time))

# Weitere Möglichkeiten mit den Modulen
print(date(2012, 5, 15) < date(2018, 3, 8))  # True
print(date(2012, 5, 15) > date(2018, 3, 8))  # False
print(date(2012, 5, 15) != date(2018, 3, 8))  # True
print(date(2012, 5, 15) == date(2018, 3, 8))  # False
print(date(2012, 5, 15) == date(2012, 5, 15))  # True
print(datetime(2012, 5, 15, 12, 30, 25) == date(2012, 5, 15))  # False
print(datetime(2012, 5, 15, 0, 0, 0) == date(2012, 5, 15))  # False
print(datetime(2012, 5, 15, 0, 0, 0) == datetime(2012, 5, 15))  # True

# Datum angeben und mit den date und time modulen abrufen
dt = datetime(2050, 10, 20, 20, 30, 40)
print(dt)
print(dt.time())
print(dt.date())

# date und time kombinieren
print("Combined: " + str(datetime.combine(date(2020, 12, 20), time(10, 12, 13))))

# Wiederholungsübung
some_day = date(2013, 5, 22)
some_time = time(13, 37)

print(str(some_day) + " " + str(some_time))
print("date und time: ")

right_now = datetime.now()
print(datetime.now())

dt = datetime(1234, 5, 6, 7, 8, 9, 10)
print(dt)
print(dt.date())
print(dt.time())

datetime_example = datetime(1995, 8, 12)
print("Timestamp Beispiel: " + str(datetime_example.timestamp()))

ausjerechnet = right_now.timestamp() - datetime_example.timestamp()
print("Ausgerechnet: " + str(ausjerechnet))
print("Calculated in Strings:")
print(right_now - datetime_example)

print(some_day.year)
print(some_day.month)
print(some_day.day)

print(datetime.combine(date(1234, 5, 6), time(7, 8, 9, 10)))
