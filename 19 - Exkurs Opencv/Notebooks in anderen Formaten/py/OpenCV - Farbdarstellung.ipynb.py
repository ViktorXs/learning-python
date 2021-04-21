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

# ## OpenCV: Farbdarstellung
# 
# In dieser Lektion lernst du:
# 
# - Wie die Farben repräsentiert werden können
# - Wie du die Grafik mit echten Farben anzeigen kannst
# - Wann & Warum du Graustufen-Bilder verwenden solltest

# In[1]:



import matplotlib.pyplot as plt
import numpy as np
import cv2


# In[18]:


img = cv2.imread("bild.jpg")

print(img[0][0])

i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(i[0][0])
plt.imshow(i)
plt.show()


# In[16]:


g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(g, "gray")
plt.show()


# In[ ]:





