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

# ## Pandas: Daten sortieren
# 
# Oft möchtest du die Daten noch in einer Spalte sortieren lassen. Das zeige ich dir hier in dieser Lektion!

# In[6]:


import pandas as pd
df = pd.read_csv("../data/astronauts.csv")

df.head()


# ### Daten sortieren mit `sort_values()`
# 
# Mit **`sort_values()`** kannst du das DataFrame nach den Einträgen in einer bestimmten Spalte, die du als Parameter übergibst, sortieren.

# In[8]:


df2 = df.sort_values("Name")
df2


# Standardmäßig wird dann aufsteigend sortiert. Mit dem `ascending` - Attribut kannst du dieses Verhalten auch umstellen:

# In[9]:


df2 = df.sort_values("Name", ascending = False)
df2


# Wenn du z.B. alle Namen in absteigender Reihenfolge durchgehen möchtest, empfiehlt es sich erst das ganze DataFrame zu sortieren und dann mit den sortierten Namen zu arbeiten.

# In[ ]:


for name in df2["Name"]:
    print(name)


