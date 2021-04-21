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

# ## Weitere Datenstruktur: PriorityQueue
# 
# In dieser Lektion lernst du eine weitere Datenstruktur kennen: PriorityQueue.
# 
# Das ist eine Warteschlange, die die Einträge für uns automatisch sortiert!

# In[2]:


import queue
q = queue.PriorityQueue()

q.put((10, "Hallo Welt"))
q.put((15, "Mars"))
q.put((5, "Wichtig"))


# In[3]:


q.get()


# In[4]:


q.get()


# In[15]:


text = "A A A A A B B B C C C C C D D D D D D D D E E E E E E E"
d = {}
for word in text.split(" "):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

pq = queue.PriorityQueue()
for word, number in d.items():
    pq.put((-number, word))

print(pq.get())
print(pq.get())
print(pq.get())


# In[ ]:





