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

# # Grafiken zeichnen mit Schleifen

# Bevor es an das Plotten geht, importieren wir wieder das Matplolib-Modul in unser Python, das uns zusätzliche Funktionen zur Verfügung stellt.

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


plt.scatter([1, 2], [4, 5])
plt.show()


# Mit zwei for-Schleifen füllen wir schnell drei Listen, die wir dann gegeneinander plotten.

# In[5]:


# In die Liste xs packen wir die ganzzahligen Werte von -10 bis 10
xs = []
for x in range(-10, 11):
    xs.append(x)

# In die Liste ys packen wir die Quadratzahlen zu jedem Wert aus der Liste xs
ys = []
for x in xs:
    ys.append(x * x)
    
# In die Liste ys packen wir die Kubikzahlen zu jedem Wert aus der Liste xs    
ys2 = []
for x in xs:
    ys2.append(x * x * x)

    
# Wir geben die Listen xs, ys, ys2 nacheinander aus    
print(xs)
print(ys)
print(ys2)

# Wir plotten ys und ys2 jeweils gegen xs 
plt.plot(xs, ys)
plt.plot(xs, ys2)
plt.show()


