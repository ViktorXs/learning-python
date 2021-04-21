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

# ## Funktionsparameter benennen
# 
# Manchmal arbeitest du mit einer Funktion, die sehr viele Parameter übergeben bekommt. Dann wird der Funktionsaufruf sehr schnell sehr unübersichtlich...
# 
# In dieser Lektion lernst du:
# 
# - Was Standardparameter sind,
# - Und wie du benannte Parameter einer Funktion übergeben kannst.

# In[6]:


def multi_print(number = 3, word = "Hallo"):
    for i in range(0, number):
        print(word)
        
multi_print(5)
multi_print(word = "Welt", number = 5)


# In[ ]:





