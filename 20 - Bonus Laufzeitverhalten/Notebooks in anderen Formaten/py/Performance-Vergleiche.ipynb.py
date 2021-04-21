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

# # Exkurs Performance

# ### 1.) Laufzeitmessung

# In[176]:


from datetime import datetime

start = datetime.now()

N = 100 # hier gehört für mich die Erklärung hin, was N bedeutet ;-)

odds = []
# s = 0

for i in range(N):
    # s += 1
    if (i % 2 != 0): # Prüfen, ob die Zahl mit Rest durch 2 teilbar ist 
        odds.append(i)
    
print("Alle ungeraden Zahlen bis " + str(N - 1) + ": ", odds)

end = datetime.now()

print(end - start)


# In[76]:




# In[19]:




# In[18]:




# ### 2.) Vergleich von Python vs. Python mit Numpy

# #### Vorbereitung

# In[21]:


import numpy as np
import math


# In[24]:


N = 1000000 # Anzahl der Einträge, die wir auswerten sollen
entries = list(np.random.random(N) ) # Liste mit 1 Mio. Einträgen, Zufallszahlen zwischen 0 und 1 (z.B. Messwerte)


# #### 2.1) for-Schleife

# In[27]:




# #### 2.2) List Comprehension

# In[28]:




# #### 2.3) Als Numpy - Array

# In[30]:


np_entries = np.array(entries)


# In[32]:




