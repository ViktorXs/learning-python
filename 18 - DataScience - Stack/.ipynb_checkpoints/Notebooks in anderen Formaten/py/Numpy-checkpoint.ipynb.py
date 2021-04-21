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

# ## Numpy
# 
# In dieser Lektion lernst du den ersten Baustein des `DataScience - Stacks` in Python kennen: **Numpy**. Wir setzen Numpy dann ein, wenn wir bereits Daten eingelesen haben und nun weiterverarbeiten wollen, z.B. sie filtern oder mathematische Berechnungen mit ihnen durchführen. Das Numpy-Modul ist nämlich auf numerische Berechnungen hin optimiert.
# 
# Insbesondere stellt Numpy die Datenstruktur **Array** bereit: Arrays verhalten sich ähnlich wie Listen, man kann mit ihnen aber komfortabler rechnen.

# ### `Numpy-Arrays` vereinfachen das Rechnen mit Daten

# Mal ein Beispiel ohne Numpy, d.h. ohne Arrays:

# In[2]:


import matplotlib.pyplot as plt

xs = []
for x in range(0, 10):
    xs.append(x)

ys = []
# wir müssen hier eine Schreife schreiben (oder eine list comprehension), um aus der Liste xs die Liste ys zu erzeugen
for x in xs:
    ys.append(x ** 2)

plt.plot(xs, ys)
plt.show()


# Nun benutzen wir die Array-Datenstruktur aus dem Numpy-Modul:

# In[1]:


import matplotlib.pyplot as plt

# wir importieren das numpy-Modul; als Abkürzung besteht die Konvention, np zu verwenden
import numpy as np

# wir erzeugen einen Array mit den ganzen Zahlen von 0 bis 9 und speichern es in der Variable xs
xs = np.arange(10)

# auf ein Numpy-Array-Objekt können wir ohne Weiteres elementweise Rechenoperationen anwenden, z.B. jedes Element quadrieren
ys = xs ** 2

plt.plot(xs, ys)
plt.show()


# In[8]:


type(ys)


# ### Arrays erzeugen

# Mit dem `array()` - Befehl können wir Python-Listen in Arrays umwandeln.

# In[18]:


np.array([1, 2, 3, 4, 5, 10])


# Mit der `arange()` - Funktion wird ein Array zu einem beliebigen Zahlenbereich erstellt.

# In[13]:


np.arange(1, 11)


# In[12]:


np.arange(10)


# Es gibt auch einen eigenen Befehl um einen beliebig langen Array zu erzeugen (hier: 10 Elemente), der nur mit Nullen gefüllt ist: die `zeros()`-Funktion.

# In[20]:


np.zeros(10)


# Mit `ones()` gibt es eine entsprechende Funktion auch für Einsen:

# In[21]:


np.ones(10)


# ### Mit Arrays rechnen
# Rechenoperationen auf einem Array-Objekt werden für jeden Wert des Arrays ausgeführt, ohne dass diese Werte in einer _Schleife_ oder _list comprehension_ ausdrücklich durchlaufen werden müssen.

# In[15]:


np.arange(10) + 3


# In[14]:


np.arange(10) * 3


# Daneben gibt es auch vorgefertigte Methoden für Arrays:

# In[4]:


# Mittelwert
print(np.array([1, 2, 3, 4, 5, 10]).mean())

# Minimum
print(np.array([1, 2, 3, 4, 5, 10]).min())

# Maximum
print(np.array([1, 2, 3, 4, 5, 10]).max())

# Standardabweichung
print(np.array([1, 2, 3, 4, 5, 10]).std())


# In[ ]:





