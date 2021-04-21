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




# In[262]:




# In[183]:




# ### 2.) Vergleich von Programmstrukturen (oder der Beweis, warum NumPy cool ist)
# 
# Quelle: https://github.com/tirthajyoti/PythonMachineLearning/blob/master/How%20fast%20are%20NumPy%20ops.ipynb (bearbeitet)

# #### Vorbereitung

# In[2]:


import numpy as np
import time
import matplotlib.pyplot as plt
import random


# In[3]:


N = 1000000 # Einträge, die wir auswerten sollen
speed = [] # hier kommen die Geschwindigkeiten rein, die wir vergleichen wollen


# In[4]:


l1 = list(np.random.random(N) ) # Liste mit 1 Mio. Einträgen, Zufallszahlen zwischen 0 und 1 (z.B. Messwerte)
l1[:3] # schauen wir uns den Anfang der Liste mal an


# #### 2.1) for-Schleife

# In[5]:




# #### 2.2) List Comprehension

# In[6]:




# #### 2.3) Map

# In[228]:


start = datetime.now()

l4 = list(map(lambda x: np.sqrt(x),l1)) 
# ohne lambda-Funktion wäre diese Zelle schneller als die List Comprehension;
# meistens benutzt man aber doch bei map selbst definierte Funktionen
# deswegen sorgt lambda hier für ein praxisnäheres Ergebnis

end = datetime.now()

print("map brauchte {} Sekunden".format(end-start))
speed.append(end - start)


# #### 2.4) Vektorisierung als Numpy-Array

# In[229]:


arr1 = np.array(l1)


start = datetime.now()

arr2 = np.sqrt(arr1)

end = datetime.now()


print("NumPy brauchte nur {} Sekunden".format(end-start))
speed.append(end - start)


# ### Vergleich

# In[241]:


s = [s.total_seconds() for s in speed] # timedelta in floats umrechnen (NumPy-Arrays haben keine solche Funktion)
#plt.figure(figsize=(10,6))
plt.ylabel("Zeit, um die Wurzeln von 1 Mio. Daten auszurechnen",fontsize=12)
plt.xlabel("Programmstruktur",fontsize=14)
plt.grid(True)
plt.bar(left=[1,2,3,4],height=s, align='center',tick_label=['for-Schleife','List Comprehension','Map','NumPy'])


