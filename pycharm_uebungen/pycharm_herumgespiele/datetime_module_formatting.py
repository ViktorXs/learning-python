from datetime import datetime

now = datetime.now()
print(now)

# .strftime() = Formatieren
print(now.strftime("%a, %d.%m.%Y"))

# .strptime() = Einlesen.
d = "Wed, 30.06.2021"

print()
print(datetime.strptime(d, "%a, %d.%m.%Y"))

# timedelta rumgespiele
from datetime import timedelta
a_day = datetime(1987, 7, 5) - timedelta(days=28, hours=13)
print(a_day)
td = now - a_day
print(td)
print(datetime(1980, 5, 15, 12, 35, 55) + td)
