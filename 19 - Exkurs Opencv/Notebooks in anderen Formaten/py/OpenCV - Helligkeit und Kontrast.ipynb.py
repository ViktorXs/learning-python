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

# ## OpenCV: Helligkeit verändern
# 
# In dieser Lektion lernst du:
# 
# - Wie das Bild intern gespeichert wird
# - Wie du die Helligkeit vom Bild verändern kannst

# In[3]:



import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("bild.jpg")


# In[11]:


print(img[0][0])


# In[14]:


r = np.array([1, 2, 3, 100], dtype="uint8")
r = r + 250
print(r)


# In[16]:


increased = img + 50


# In[18]:


print(img[0][0])
print(increased[0][0])


# In[20]:


i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()


# In[21]:


i = cv2.cvtColor(increased, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()


# In[ ]:





