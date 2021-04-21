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
# - Wie du aus einer .html-Datei Informationen extrahieren kannst
# 
# Dazu zerlegen wir mit BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) die .html-Datei!

# In[8]:


# Zuerst holen wir uns unsere Seite, die wir eigentlich einlesen wollten...

import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")


# In[10]:


from bs4 import BeautifulSoup


# In[26]:


html = """
    <html>
        <body>
            <p class="something">Ich bin ein Absatz!</p>
            <p>Ich bin noch ein Absatz</p>
        </body>
    </html>
"""

doc = BeautifulSoup(html, "html.parser")


# In[29]:


for p in doc.find_all("p"):
    print(p.attrs)
    print(p.text)


# In[ ]:





