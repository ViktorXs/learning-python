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

# # Vorstellung weiteres Modul: CSV
# 
# In dieser Lektion lernst du, wie du:
# 
# - mit dem Python Module - Index umgehst (https://docs.python.org/3/py-modindex.html)
# - mit Moduls noch komfortabler .csv-Dateien einlesen kannst am Beispiel des CSV. 

# In[3]:


import sys
print(sys.version)


# In[7]:


import csv
with open("datei.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=",")
    for line in csv_file:
        print(line)


# In[14]:


import csv
with open("fromexcel.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=";", quotechar='"')
    for line in csv_file:
        print(line)


# In[ ]:





