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

# ## Weitere Datenstruktur: Queue
# 
# In dieser Lektion lernst du eine weitere Datenstruktur kennen: Queue.
# 
# Diese ist für folgende Operationen optiminiert:
# 
# - Eintrag hinzufügen
# - Eintrag vom Anfang entfernen.

# In[10]:


import queue
q = queue.Queue()

q.put("Hallo")
q.put("Welt")
q.put("Hallo")
q.put("Mars")
q.put("Pluto")

print(q)


# In[12]:


print(q.get())


# In[13]:


print(q.get())


# In[14]:


while not q.empty():
    element = q.get()
    print(element)


# In[ ]:





