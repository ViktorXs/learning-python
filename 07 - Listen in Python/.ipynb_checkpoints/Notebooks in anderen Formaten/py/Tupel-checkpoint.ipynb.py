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

# ## Tupel
# 
# Tupel sind sowas ähnliches wie eine Liste... werden aber für andere Zwecke verwendet.
# 
# - Hier geht's jetzt darum, was Tupel sind, ...
# - wie sich diese von einer Liste unterschieden
# - und wie du diese in Python verwenden kannst

# In[2]:


t = (1, 2, 3)
print(t)


# In[3]:


liste = [1, 2, 3]
liste.append(5)
print(liste)


# ## Exkurs Informatik: Mutable (veränderlich) vs. Immutable (unveränderlich)
# 
# - **Liste:** Veränderliche Datenstruktur
# - **Tupel:** Unveränderliche Datenstruktur

# In[11]:


person = ("Max Müller", 55)

def do_something(p):
    p[0] = "Max Mustermann"
    
do_something(person)

print(person)


# In[ ]:





# In[ ]:





