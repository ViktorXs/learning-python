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

# ## Exkurs: CSV - Datei schreiben
# 
# In dieser Lektion gehen wir nochmal kurz darauf ein, wie du mit Python eine .csv-Datei erstellen kannst.
# 
# (Link: https://docs.python.org/3.6/library/csv.html)

# In[7]:


import csv
with open('students.csv', 'a', newline='') as f:
    writer = csv.writer(f, delimiter=";")
    
    writer.writerow(["Spalte 1", "Spalte 2", "Spalte 3"])
    writer.writerow(["Zeile 2: Spalte 1", "Spalte 2", "Spalte 3"])


# In[ ]:





