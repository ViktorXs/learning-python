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

# ## Variable Funktionsparameter übergeben

# In[3]:


def f(a, b, c):
    print(a)
    print(b)
    print(c)
    
l = [1, 2, 3]
f(l[0], l[1], l[2])

f(*l)


# In[9]:


def calculate_max(*params):
    print(params)
    current_max = params[0]
    for item in params:
        if item > current_max:
            current_max = item
    return current_max
    
calculate_max(1, 2, 3)


# In[10]:


def calculate_max(current_max, *params):
    print(current_max)
    print(params)
    for item in params:
        if item > current_max:
            current_max = item
    return current_max
    
calculate_max(1, 2, 3)


# In[ ]:





