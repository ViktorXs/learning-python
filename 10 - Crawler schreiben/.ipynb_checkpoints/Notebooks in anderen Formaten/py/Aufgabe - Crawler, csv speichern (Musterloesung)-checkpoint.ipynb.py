# Diese .py - Datei wurde automatisch aus dem IPython - Notebook (.ipynb) generiert.
# 
# Gelegentlich wurde ich von Teilnehmern gefragt, ob ich die Kursmaterialien nicht 
# auch als normale .py - Datien bereitstellen könne. Dadurch ist es möglich, den Code
# ohne Jupyter zu öffnen, beispielsweise wenn Python-Programme in einem Terminal oder in 
# Eclipse entwickelt werden.
# 
# Dem möchte ich hiermit nachkommen. Ich empfehle dir aber trotzdem, schau' dir lieber die
# IPython - Notebooks direkt an, oder den HTML-Export eben dieser. Dieser reine .py-Export
# ist meiner Meinung nach etwas unübersichtlich.
# 
# Bitte beachte zudem, dass du Pfadangaben ggf. manuell korrigieren musst!
# 
#!/usr/bin/env python
# coding: utf-8

# ## Aufgabe: Ausgabe als Datei speichern
# 
# 
# Jetzt haben wir den ArticleFetcher schon so angepasst, dass er die Daten aus allen Seiten extrahiert. Aber eigentlich wäre es cool, wenn er die Daten direkt als .csv - Datei speichern würde ;)
# 
# Aufgabe:
# 
# - Schaue dir das Modul csv an, und zwar die writer - Funktion: https://docs.python.org/3/library/csv.html#csv.writer
# - Passe dann den Ausgabe-Code so an, dass statt der Ausgabe hier im Notebook eine .csv-Datei gespeichert wird. Verwende als Spaltentrenner (Separator) ein Semikolon, und als "quotechar" die doppelten Anführungszeichen ('"'), dann können wir die Datei später noch mit Excel öffnen :)

# In[2]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


# In[3]:


class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image
        
class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        articles = []
        
        while url != "":
            print(url)
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
            
            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])

                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)

            next_button = doc.select_one(".navigation .btn")
            if next_button:
                next_href = next_button.attrs["href"]
                next_href = urljoin(url, next_href)            
                url = next_href
            else:
                url = ""
        
        return articles


# In[4]:


import csv
fetcher = ArticleFetcher()

with open('crawler_output.csv', 'w', newline='') as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for article in fetcher.fetch():
        articlewriter.writerow([article.emoji, article.title, article.image, article.content])


# In[ ]:





