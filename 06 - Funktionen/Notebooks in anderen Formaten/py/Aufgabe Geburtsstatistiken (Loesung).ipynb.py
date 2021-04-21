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

# ## Aufgabe!
# 
# Finde heraus, wie oft der Name "Max" als männlicher Vorname in Kalifornien zwischen 1950 und 2000 (jeweils einschließlich) vergeben wurde! Verwende dazu die bereitgestellte .csv - Datei (../data/names.csv)!

# In[12]:


occurences = 0

with open("../data/names.csv", "r") as file:
    for line in file:
        splitted = line.strip().split(",")
        
        if splitted[2] == "Year":
            continue
        
        year = int(splitted[2])
        
        if splitted[1] == "Max" and year >= 1950 and year <= 2000 and splitted[3] == "M" and splitted[4] == "CA":
            occurences = occurences + int(splitted[5])
           
print(occurences)


# In[ ]:





# In[ ]:





