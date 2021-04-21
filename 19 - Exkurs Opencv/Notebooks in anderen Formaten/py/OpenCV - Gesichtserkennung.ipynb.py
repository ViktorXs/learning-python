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

# ## Gesichtserkennung mit OpenCV
# 
# In dieser Lektion lernst du:
# 
# - Wie du OpenCV beauftragen kannst, ein Gesicht in einem Bild zu finden

# In[81]:



import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("bild.jpg")


# In[82]:


i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()


# In[84]:


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, "gray")
plt.show()


# In[86]:


classifier = cv2.CascadeClassifier("../data/haarcascades/haarcascade_frontalface_alt2.xml")


# In[97]:


faces = classifier.detectMultiScale(gray, minNeighbors=10)


# In[98]:


print(faces)


# In[99]:


c = img.copy()
for face in faces:
    x, y, w, h = face
    cv2.rectangle(c, (x, y), (x + w, y + h), (0, 255, 0), 10)
    print(face)

i = cv2.cvtColor(c, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()


# In[ ]:





