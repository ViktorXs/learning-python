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

# ## Warum macht Numpy so viel Sinn?
# 
# In dieser Lektion geht es darum:
# 
# - Warum du für umfangreiche, numerische Berechnungen auf jeden Fall numpy verwenden solltest.

# In[2]:


import numpy as np
import math

# Anzahl der Einträge, die wir auswerten sollen
N = 1000000

# Liste mit 1 Mio. Einträgen, Zufallszahlen zwischen 0 und 1 (z.B. Messwerte)
entries_np = np.random.random(N)


# In[3]:


entries_np


# ### Beispiel: Wurzel berechnen mit Python (for-Schleife)

# In[4]:


entries = list(entries_np)


# In[5]:




# ### Beispiel: Wurzel berechnen mit Python (List-Comprehension)

# In[6]:




# ### Beispiel: Wurzel berechnen mit Numpy

# In[14]:




# Weitere Informationen:
# 
# - Suchen nach: "Vectorization numpy"
# - SSE: https://de.wikipedia.org/wiki/Streaming_SIMD_Extensions

# In[ ]:





# In[ ]:





