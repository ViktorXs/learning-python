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

# ## Elemente im HTML finden
# 
# In dieser Lektion lernst du:
# 
# - Wie du aus einer .html-Datei Informationen extrahieren kannst.
# 
# Dazu zerlegen wir mit BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) die .html-Datei!

# In[1]:


# Zuerst holen wir uns unsere Seite, die wir eigentlich einlesen wollten...

import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")


# In[2]:


from bs4 import BeautifulSoup


# In[4]:


doc = BeautifulSoup(r.text, "html.parser")


# In[25]:


for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text
    title = card.select(".card-title span")[1].text
    image = card.select_one("img").attrs["src"]
    
    print(image)
    print(emoji)
    print(content)
    print(title)
        


# In[ ]:





