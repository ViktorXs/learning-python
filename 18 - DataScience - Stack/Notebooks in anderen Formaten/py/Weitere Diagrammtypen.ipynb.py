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

# ## Matplotlib unterstützt auch noch weitere Diagrammtypen...
# 
# In dieser Lektion lernst du wie du mit `matplotlib` folgende Diagrammtypen zeichnen kannst:
# 
# - Kreisdiagramme
# - Balkendiagramme
# - Punktediagramme

# In[2]:


import matplotlib.pyplot as plt


# ### Kreisdiagramm
# 
# Für ein `Kreisdiagramm` rufst du die `pie()`-Funktion auf und übergibst ihr als Parameter eine Liste. Die Einträge in der Liste stehen für die Größe der "Kuchenstücke" (im Verhältnis zur Summe aller Listenelemente):

# In[4]:


plt.pie([1, 2, 3])
plt.show()


# ### Balkendiagramm
# 
# `Balkendiagramme` erzeugst du mit der `bar()`-Methode. Ihr musst du als Parameter zwei Listen übergeben: eine für die Werte auf der x-Achse (wo Balken sein sollen), eine für die Werte auf der y-Achse (also die Höhe der Balken). Dementsprechend müssen die beiden Listen gleich viele Elemente beinhalten:

# In[8]:


plt.bar([1, 2, 4], [5, 6, 5])
plt.show


# ### Punktediagramm
# Mit der `scatter()`-Funktion kannst du dir auch einfach nur die Punkte anzeigen lassen:

# In[11]:


plt.scatter([1, 2, 4], [5, 6, 5])
plt.show()


# Alle diese Diagramme kannst du so modifizieren, wie du es in einer früheren Lektion gesehen hast:

# In[3]:


plt.scatter([1, 2, 4], [5, 6, 5], color = "#ff0000", marker = "x")
plt.show()


