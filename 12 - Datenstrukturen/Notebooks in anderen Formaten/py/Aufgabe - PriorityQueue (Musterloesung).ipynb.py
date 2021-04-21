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

# ## Aufgabe: PriorityQueue
# 
# 
# Ermittle den 5.-häufigsten Vornamen, der in den USA vergeben wurde! Lies dazu die ../data/names.csv - Datei ein. Verwende dazu zuerst ein Dictionary, mit dem du die Häufigkeit der Vornamen zählst und anschließend eine PriorityQueue, um die Top 5 Vornamen zu ermitteln.

# In[6]:


import csv

names = {}

with open('../data/names.csv', newline='') as csvfile:
    namereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    counter = 0
    for line in namereader:
        if counter != 0:
            number = int(line[5])
            name = line[1]
            
            if name in names:
                names[name] = names[name] + number
            else:
                names[name] = number
        counter = counter + 1


# In[12]:


import queue

pq = queue.PriorityQueue()

for name, number in names.items():
    pq.put((-number, name))
    
for i in range(0, 50):
    print(pq.get())


# In[ ]:





