from datetime import datetime

now = datetime.now()
print(now)

# .strftime() = Formatieren
print(now.strftime("%a, %d.%m.%Y"))

# .strptime() = Einlesen.
d = "Wed, 30.06.2021"

print()
print(datetime.strptime(d, "%a, %d.%m.%Y"))
