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

# ## Probleme mit relativen URLs
# 
# In dieser Lektion lernst du, wie du:
# 
# - mit Verlinkungen umgehen kannst
# - es schaffst, die richtigen Bild-URLs zu ermitteln.

# In[9]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# In[10]:


class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image
        
class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")
        
        articles = []
        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            image = urljoin(url, card.select_one("img").attrs["src"])

            crawled = CrawledArticle(title, emoji, content, image)
            articles.append(crawled)
        return articles


# In[11]:


fetcher = ArticleFetcher()
articles = fetcher.fetch()

for article in articles:
    print(article.image)


# In[ ]:





