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

# ### Hinführung: O-Notation

# In[11]:




# ### Idee: Wir ignorieren konkrete Laufzeiten

# In[15]:


import matplotlib.pyplot as plt
import numpy as np


plt.plot(np.arange(1, 600), np.arange(1, 600), label="f(n) = n")
plt.plot(np.arange(1, 600), np.arange(1, 600) * 2, label="f(n) = 2n")
plt.legend()

plt.xlabel("n")
plt.ylabel("Anzahl print() - Befehle")
plt.show()


# In[21]:



plt.plot(np.arange(1, 6), np.repeat(100, 5), label="f(n) = 100")
plt.plot(np.arange(1, 6), np.arange(1, 6), label="f(n) = n")
plt.legend()

plt.xlabel("n")
plt.show()


# In[22]:


# Konstante Laufzeit vs. Lineare Laufzeit

plt.plot(np.arange(1, 600), np.repeat(100, 599), label="f(n) = 100")
plt.plot(np.arange(1, 600), np.arange(1, 600), label="f(n) = n")
plt.legend()

plt.xlabel("n")
plt.show()


# In[23]:


# Konstante Laufzeit vs. Lineare Laufzeit

plt.plot(np.arange(1, 600), np.repeat(1, 599), label="f(n) = 1")
plt.plot(np.arange(1, 600), np.arange(1, 600), label="f(n) = n")
plt.legend()

plt.xlabel("n")
plt.show()


# In[ ]:





