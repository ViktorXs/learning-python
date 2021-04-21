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

# ## Python Wissen: Generatoren
# 
# In dieser Lektion geht's um ein weiteres Python-Konzept, welches unseren Crawler etwas vereinfachen kann: Generatoren. 
# 
# Problem: Manchmal interessieren dich nur die ersten 5 Einträge, manchmal möchtest du alle Einträge einlesen. Wie bekommen wir es hin, dass die .fetch()-Methode automatisch erkennt, wie viele Einträge mich interessieren?
# 
# In dieser Lektion lernst du:
# 
# - Was Generatoren sind
# - Und wie du diese in Python verwenden kannst.

# In[6]:


def gen_list():
    liste = []
    for i in range(0, 10):
        print("liste: " + str(i))
        liste.append(i)
    return liste

for element in gen_list():
    print("for: " + str(element))


# In[5]:


def gen_generator():
    for i in range(0, 10):
        print("gen: " + str(i))
        yield i

for element in gen_generator():
    print("for: " + str(element))


# In[7]:


for element in gen_generator():
    if element == 4:
        break
    print("for: " + str(element))


# In[ ]:





