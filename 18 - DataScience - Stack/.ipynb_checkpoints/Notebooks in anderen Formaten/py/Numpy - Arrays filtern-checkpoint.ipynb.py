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

# ## Numpy: Arrays filtern
# 
# In dieser Lektion lernst du:
# 
# - Wie du `Numpy` - Arrays filtern kannst

# Zuerst laden wir natürlich wieder das `Numpy`-Modul:

# In[1]:


import numpy as np


# ### Ein Array mit einem anderen Array filtern
# 
# Wir können ein Array mit Boolean - Einträgen dazu verwenden, ein anderes Array zu filtern.

# In[3]:


a = np.array([1, 2, 3, 4])
print(a)


# Ein Array braucht nicht notwendigerweise nur aus Zahlen bestehen:

# In[14]:


b = np.array([False, True, True, False])
print(b)


# Mithilfe der `[ ]-Schreibweise`, die du schon vom _Zugriff auf Listen_ und vom _list slicing_ her kennst, können wir ein Numpy-Array einem anderen Numpy-Array übergeben, das dann gefiltert wird:

# In[15]:


a[b]


# Beim zu filternden Array bleiben also nur die Werte stehen, an deren Index im Filter-Array ein True-Boolean steht.

# ### Mit Vergleichen filtern

# Wir können spezifischer filtern, indem wir Vergleiche für Arrays formulieren. Wie die Rechenoperationen werden auch die Vergleichsoperationen auf jeden Wert eines Arrays angewendet - jeder Wert wird einzeln verglichen:

# In[22]:


c = a >= 3
print(c)


# Einen solchen Array, den wir mithilfe einer Vergleichsoperation erzeugt haben, können wir dann als Filter-Array verwenden:

# In[24]:


a[c]


# Oder kurz:

# In[25]:


a[a >= 3]


# Somit steht uns eine kompakte Schreibweise für das Filtern von Arrays zur Verfügung. :-)

