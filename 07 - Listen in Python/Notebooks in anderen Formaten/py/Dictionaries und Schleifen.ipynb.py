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

# ## Dictionaries und Schleifen
# 
# In dieser Lektion lernst du:
# 
# - Wie du ein Dictionary Eintrag für Eintrag durchgehen kannst
# - Und wie du hierfür das Entpacken von Tupeln benötigst :)

# In[5]:


d = {"München": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}

for key in d: 
    value = d[key]
    print(key)
    print(value)


# In[8]:


for key, value in d.items():
    print(key + ": " + value)


# In[ ]:





