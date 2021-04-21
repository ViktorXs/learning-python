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

# ## Numpy: Mehrdimensionale Arrays
# 
# In Numpy kannst du auch mit **mehrdimensionalen Arrays** (**Matrizen**) arbeiten.

# In[3]:


import numpy as np


# Eindimensionale Arrays kennst du schon:

# In[11]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a)


# Arrays können aber auch weitere Arrays enthalten, dann sprechen wir von **mehrdimensionalen Arrays**:

# In[13]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)


# Bei einem zweidimensionalen Array liegt ein Array in einem Array vor, bei einem dreidimensionalen Array schon ein Array in einem Array in einem Array. Doch das klingt komplizierter als es ist. Du brauchst einfach die `[` vor dem ersten Element (oder nach dem letzten Element) des Arrays zu zählen, um zu sehen, wie viele Dimensionen/Ebenen das Array besitzt.

# ### Die Form eines Arrays mit `reshape()` verändern
# Mit der **`reshape()`**-Methode kannst du einen Array restrukturieren, sodass innerhalb des Arrays Unter-Arrays gebildet werden und die Werte auf diese neuen Unter-Arrays aufgeteilt werden. Dazu übergibst du `reshape()` als Parameter ein Tupel mit Zahlen, um die Maße für die neue Gestalt des Arrays festzulegen. 
# 
# Jede der Zahlen in dem Tupel steht dafür, wie viele Elemente es in einer Dimension geben soll.

# In[10]:


a.reshape((2, 4))


# Mit dem Parameter `(2, 4)` sagen wir also, dass der äußere Array zwei Elemente enthalten soll (d.h. zwei Unter-Arrays), und die Arrays der zweiten Stufe jeweils vier Elemente enthalten sollen (d.h. die Werte).
# 
# Bei zwei Dimensionen, d.h. einem Tupel mit zwei Elementen als Parameter, kannst du dir den ersten Wert des Tupels als Anzahl der Zeilen und den zweiten Wert als die Anzahl der Spalten vorstellen.

# Auf die Elemente in einem solchen mehrdimensionalen Array kannst du mit mehrfacher Verwendung der `[ ]-Schreibweise` zugreifen.

# In[22]:


reshaped = a.reshape((2, 4))

print(reshaped[0])
print(reshaped[0][0])
print(reshaped[1])
print(reshaped[1][3])


# Natürlich kannst du mit `reshape()` nur Verschachtelungen erzeugen, die zur Gesamtzahl der Einträge passen, d.h. das Produkt über alle Werte aus dem Tupel, das du als Parameter übergibst, und die Anzahl der Elemente aus dem Array müssen übereinstimmen.
# 
# Sonst passiert das:

# In[23]:


c = np.array([1, 2, 3, 4, 5, 6, 7])
c.reshape((4, 2))


# ### Parameter-Platzhalter: Anzahl von Einträgen in einer Dimension offen lassen

# Du kannst auch **-1** als Platzhalter für die Anzahl der Einträge in einer Ebene benutzen, statt sie zu spezifizieren; Numpy füllt dann die neuen Unter-Arrays automatisch mit Einträgen auf.

# In[13]:


a.reshape((-1, 4))


# In[16]:


a.reshape((4, -1))


# So können wir schnell ein eindimensionales Array erzeugen:

# In[17]:


b = np.array([[1, 2, 3], [4, 5, 6]])
b.reshape(-1)


# ### Die Dimensionen eines Arrays abfragen
# Die Maße eines Arrays können wir mit der `shape`-Eigenschaft des Array-Objektes abfragen.

# In[21]:


b.shape


