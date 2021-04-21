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

# ## Die O-Notation

# ### Laufzeit: O(1)

# In[2]:


def f(n):
    print("Hallo Welt")
    print("Hallo Welt")
    print("Hallo Welt")
    
f(10)


# ### Laufzeit: O(n)

# In[4]:


def f(n):
    for i in range(0, n):
        print("Hallo Welt")
        print("Hallo Welt")
    
f(4)


# ### Laufzeit: O(n)

# In[5]:


def f(n):
    print("Hallo Welt")
    print("Hallo Welt")
    for i in range(0, n):
        print("Hallo Welt")
    
f(4)


# In[12]:


import matplotlib.pyplot as plt
import numpy as np


plt.plot(np.arange(0, 25000), np.arange(0, 25000), label="n")
plt.plot(np.arange(0, 25000), np.arange(0, 25000) + 2, label="n + 2")
plt.legend()
plt.show()


# ### Laufzeit: O(n^2)

# In[13]:


def f(n):
    for i in range(0, n): # O(n*n)
        for j in range(0, n): # O(n)
            print("Hallo Welt") # O(1)
    
f(4)


# ### Laufzeit: O(n^2)

# In[15]:


def f(n):
    for i in range(0, int(n / 2)): # O(n*n)
        for j in range(0, int(n / 2)): # O(n) 
            print("Hallo Welt") # O(1)
    
f(4)


# In[ ]:





# In[ ]:





