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

# # Hinführung: O-Notation
# 
# Schauen wir uns mal ein paar Beispiele an, wie sich die Anzahl der Aufrufe des print() - Befehles in Abhängigkeit zu `n` verhalten könnte:

# ### Konstante Laufzeit

# In[3]:


def f(n):
    print("--- nächstes n: " + str(n) + "---")
    for i in range(1, 6): 
        print(str(i) + ". Durchlauf von 5")

for n in range(1, 6):
    f(n)


# ### Lineare Laufzeit

# In[4]:


# wir schauen uns an, wie sich die Ausgabe der Funktion f in Abhängigkei vom Parameter n verändert

def f(n):
    print("--- nächstes n: " + str(n) + "---")

    for i in range(1, n + 1): 
        print(str(i) + ". Durchlauf von " + str(n))

for n in range(1,6):
    f(n)


# ### Quadratische Laufzeit

# In[6]:


def f(n):
    print("--- nächstes n: " + str(n) + "---")
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            print("(i = " + str(i) + ", j = " + str(j) + ") - Durchlauf, n = " + str(n))

for n in range(1, 6):
    f(n)


# ### Vergleich plotten

# In[7]:


import matplotlib.pyplot as plt
import numpy as np



# In[10]:


plt.plot(np.arange(1, 6), np.repeat(5, 5), label="Konstante Laufzeit")
plt.plot(np.arange(1, 6), np.arange(1, 6), label="Lineare Laufzeit")
plt.plot(np.arange(1, 6), np.arange(1, 6) ** 2, label="Quadratrische Laufzeit")
plt.legend()

plt.xlabel("n")
plt.ylabel("Anzahl print() - Befehle")
plt.show()


# In[ ]:





