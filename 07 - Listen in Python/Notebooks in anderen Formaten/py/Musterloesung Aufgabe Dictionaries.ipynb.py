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
# Lese die ../data/names.csv - Datei ein und berechne, welcher Name insgesamt in den gesamten USA am häufigsten vergeben wurde! 
# 

# In[25]:


file = open("../data/names.csv", "r")

names = {}

for line in file:
    splitted = line.strip().split(",")
    if splitted[0] == "Id":
        continue
        
    name = splitted[1]
    count = int(splitted[5])
    
    if name in names:
        names[name] = names[name] + count
    else:
        names[name] = count


# In[27]:


max_occurences = 0
name = ""

for key, value in names.items():
    if max_occurences < value:
        max_occurences = value
        name = key
        
print(name)


# In[ ]:





