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

# In[1]:


def f(**args):
    print(args)
    
f(key="value", key2="Value 2")


# In[4]:


def g(key, param2):
    print(key)
    print(param2)
    
d = {"key": "Ich bin der Schlüssel", "param2": "Ich bin der Parameter"}

g(key=d["key"], param2=d["param2"])
g(**d)


# In[16]:


import matplotlib.pyplot as plt

def create_plot(**plot_params):
    print(plot_params)
    
    plt.plot([1, 2, 3], [5, 6, 5], **plot_params)
    plt.show()
    
create_plot(color="r", linewidth=10, linestyle="dashed")


# In[ ]:





