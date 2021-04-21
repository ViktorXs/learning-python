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

# ## Aufgabe: Dictionaries

# **Aufgabe:**
# 
# Lese die ../data/names.csv - Datei ein und berechne, welcher Name insgesamt in den gesamten USA am häufigsten vergeben wurde. 
# 
# **Tipps**:
# 
# - Lies zuerst die Daten in ein Dictionary ein und zähle, wie oft jeder Vorname insgesamt vorgekommen ist.
# - Analysiere dann erst das Dictionary und finde den häufigsten Vornamen heraus.
# - Achte drauf, wenn du 2 Zahlen addieren möchtest, musst du ggf. einen String zuerst in eine Zahl umwandeln.
# - Schreibe den gesamten Code, der die Datei öffnet und durchgeht, in einer Zelle.

# In[3]:





# In[11]:


with open("../data/names.csv", "r") as file:
    for line in file:
        print(line)
        break


# In[ ]:





