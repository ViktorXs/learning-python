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

# ## Matplotlib: Einführung
# 
# Du weisst bereits, wie du csv-Dateien und Excel-Dateien mit `pandas` einlesen und dann filtern und sortieren kannst und mit `Numpy` numerische Berechnungen auf Datenmengen ausführen kannst. 
# 
# Jetzt schauen wir uns genauer an, wie wir die Daten dann mit `matplotlib` schön darstellen können.

# In[2]:


# mit diesem Steuerzeichen legen wir fest, dass Grafiken direkt im Notebook angezeigt werden

import matplotlib.pyplot as plt


# In[3]:


plt.plot([1, 2, 3], [5, 4, 3])
plt.show()


# Alternativ können wir auch interaktive Grafiken anzeigen lassen.
# 
# Unter Umständen musst du die nächste Zelle mehrmals ausführen.

# In[4]:


import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [5, 4, 3])


# Wir können Grafiken auch in einem neuen Fenster anzeigen lassen.
# 
# Vor der Ausführung der nachfolgenden Zelle musst du in der Leiste oben auf **Kernel** und dann auf **Restart** gehen.

# In[1]:


import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [5, 4, 3])


