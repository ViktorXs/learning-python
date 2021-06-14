# Was passiert im Hintergrund?
- Das Programm stellt eine Anfrage an den Server
- Der Server sendet eine HTML Seite
- Aus der HTML können die relevanten Daten ausgelesen und extrahiert werden.

# Benötigte Tools
- Requests Modul: https://docs.python-requests.org/en/master/
An den HTML-Code der Seite rankommen und herunterladen
! In Anaconda ist das Modul schon installiert. Ansonsten manuell installieren.

- Beautifulsoup Modul: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Daten aus HTML-Code extrahieren
! In Anaconda ist das Modul schon installiert. Ansonsten manuell installieren.

- csv Modul: https://docs.python.org/3/library/csv.html#csv.writer
Ergebnisse in eine CSV Datei speichern.

- Generator verwenden (in for-Schleife mit Funktion "yield") um "on the fly" Daten zu schreiben.

## Pycharm
Mit dem Programm "PyCharm" aus dem Python Code ein funktionierendes Programm aus dem Crawler generieren.
(IDE = Integrated Development Environment. Vereinfacht die Entwicklung von Programmen.)

### Beispielprojekt zum Kurs:
- Bei Projekterstellung in PyCharm die Umgebung wechseln von "New environment using ..." zu "Previously configured interpreter" wechseln und die Anaconda Umgebung "Conda" und die python.exe auswählen!

- Python Datei im Projektordner erstellen: crawler.py

- Neuen Modul ("Python Package") erstellen: "crawler" (Es wird eine __init__.py darin erstellt). 

- Die einzelnen Klassen aus dem jupyter notebook in PyCharm als eigene Python-Dateien im "crawler" Modulordner erstellen und benennen, wie die Klassen heißen.

- Dateien, die im selben Modulordner sind in der Datei, die die andere Datei benötigen importieren:
Z.B. "from .Klasse import Klasse" (. <- Punkt steht dafür, dass die Datei im selben Modul liegt)

- In der __init__.py Datei diese Dateien im Modul eintragen: 
__all__ = ["Klasse1", "Klasse2"]
Sowie: 
from .Klasse1 import Klasse1
from .Klasse2 import Klasse2

- In der crawler.py Datei im Hauptverzeichnis das crawler-Modul importieren: Z.B:
    import crawler
    fetcher = crawler.ArticleFetcher()
    for element in fetcher.fetch():
        print(element.emoji + " - " + element.title)

# Wofür ein Crawler?
- Informationsbeschaffung
- Aktuelle Aktienkurse
- Nachrichtenseiten auslesen und Tabelle mit den Überschriften erstellen
- Informationen aus einem umfangreichen Produktkatalog extrahieren

# Darf ich das?
- Gundsätzlich ja, solange die Webseiten öffentlich zugänglich sind und man die Informationen nicht selber neuveröffentlicht.
- Jedoch besteht **immer** ein rechtliches **Risiko**. Es gilt, dieses Risiko von Abmahnungen, Eilverfahren und Klagen niedrig zu halten.

Entscheidende Faktoren:
- Wettbewerbsrecht: Unlauteres Verhalten. Gezielte Behinderung der Mitbewerber
- Wert der Dritt-Datenbank (§§ 87a ff. UrhG)
- Unterschiedlicher Grenzwert unwesentlicher zur wesentlicher Nutzung der Daten
- Rahmenbedingungen in AGB und Nutzungsbedingungen der Drittseiten
- Umgehung technischer Schutzmechanismen der Webseiten

Quelle: _"Screen-Scraping / Web-Crawler - Rechtliche Zulässigkeit und Rahmenbedingungen"_ diro.eu. URL: https://diro.eu/de/screen-scraping-web-crawler-rechtliche-zulaessigkeit-und-rahmenbedingungen. [Stand: 09.06.2021]

Interessant:
Webcrawler-Bots _"...erzeugten nach einer Schätzung von 2002 bis zu 40 % des gesamten Internet-Datenverkehrs"_ (URL: https://de.wikipedia.org/wiki/Webcrawler#Geschichte. [Stand: 09.06.2021])

