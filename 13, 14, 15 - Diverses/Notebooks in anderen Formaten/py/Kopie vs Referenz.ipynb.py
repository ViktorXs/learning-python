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

# ## Wie werden in Python Funktionsparameter übergeben?
# 
# Man unterscheidet in Python zwischen 2 verschiedenen Arten von Variablen:
# 
# - Primitive Datentypen (Zahl, String, Booleans, ...)
# - Datenstrukturen / Datenstruktur.

# In[2]:


a = 5

def f(x):
    x = 3
    print(x)

f(a)
print(a)


# In[4]:


l = ["Hallo", "Welt"]

def f(x):
    x.append("!!!")
    print(x)
    
f(l)
print(l)


# In[5]:


l = ["Hallo", "Welt"]

def f(x):
    x = ["Hallo", "Welt", "!!!"]
    print(x)
    
f(l)
print(l)


# In[ ]:





