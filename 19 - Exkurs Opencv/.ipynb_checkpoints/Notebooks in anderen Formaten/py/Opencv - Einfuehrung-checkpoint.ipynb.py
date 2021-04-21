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

# ## Opencv: Bilder mit Python bearbeiten
# 
# OpenCV stellt uns für Python diverse Funktionalitäten bereit, mit denen wir mit Bildern arbeiten können. Schauen wir uns das mal genauer an...

# In[ ]:



import matplotlib.pyplot as plt
import numpy as np
import cv2


# In[5]:


img = cv2.imread("bild.jpg")


# In[8]:


img.shape


# In[12]:


a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a)
print(a.shape)


# In[13]:


plt.imshow(img)
plt.show()


# In[ ]:





