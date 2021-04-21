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

# ## Exkurs: Wie funktioniert Numpy überhaupt?
# 
# In dieser Lektion werden wir die Klasse `Array` nachbauen, um zu verstehen was bei Numpy im Hintergrund passiert.

# In[1]:


import numpy as np

a = np.array([1, 2, 3])
print(a ** 2)

print(a[0])


# Dieses Verhalten eines Array-Objektes wollen wir mit einer eigenen Klasse rekonstruieren.

# ### Wir bauen die `Array`-Klasse nach
# 
# Dazu erstellen wir neue Klasse `MyArray` mit einer überschriebenen Methode für die Multiplikation, die dafür sorgt, dass nicht die ganze Liste, sondern jedes Element aus der Liste einzeln multipliziert wird.

# In[2]:


class MyArray():
    
    # im Constructor übergeben wir lediglich die Liste
    def __init__(self, liste):
        self.liste = liste
        
    # die Multiplikationsfunktion überschreiben wir hier derart, dass sie für jedes Element aus der Liste aufgerufen wird    
    def __mul__(self, other):
        nliste = []
        for element in self.liste:
            nliste.append(element * other)
        # oder alternativ: nliste = [element * other for element in self.liste]
        return MyArray(nliste)
        
a = MyArray([1, 2, 3])
b = a * 2

print(a.liste)
print(b.liste)


