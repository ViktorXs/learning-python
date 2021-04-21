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

# ## Aufgabe: Sets
# 
# Den Umgang mit einem Set möchten wir jetzt natürlich etwas üben. ;-)
# 
# **Aufgabe:**
# 
# Öffne die ../data/names.csv - Datei als .csv-Datei und berechne die Anzahl der verschiedenen Vornamen, die in dieser Datei aufgelistet sind!
# 
# **Tipps:**
# 
# - Die Dokumentation zum csv-Modul von Python findest du hier: https://docs.python.org/3.6/library/csv.html.
# - Verwende dazu ein Set. Damit geht das ganze ziemlich easy. :-)

# In[7]:


import csv

names = set()

with open('../data/names.csv', newline='') as csvfile:
    namereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    counter = 0
    for row in namereader:
        if counter != 0:
            names.add(row[1])
        counter = counter + 1
print(len(names))


# In[ ]:





# In[ ]:





