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

# ## Pandas: Daten filtern, Schleifen, ...
# 
# In dieser Lektion lernst du: 
# 
# - Wie du das DataFrame mit einer for - Schleife betrachten kannst
# - Wie du nach bestimmten Werten filtern kannst

# Zuerst laden wir wieder das pandas-Modul und dann die csv-Datei als DataFrame:

# In[1]:


import pandas as pd
df = pd.read_csv("../data/astronauts.csv")

df.head()


# ### Mit einer Schleife durch ein DataFrame gehen 
# 
# Mit der `iterrows()`- Methode wird ein DataFrame in eine Form umgewandelt, die es erlaubt, leicht mit einer `for`-Schleife darüber zugehen.

# In[7]:


for row in df.iterrows():
    print(row)


# Genauer werden quasi mit `iterrows()` für jeden Eintrag zweielementige Tupel gebildet, die aus dem Index des Eintrags und den Daten bestehen).

# In[8]:


for pos, d in df.iterrows():
    print(pos)


# In[9]:


for pos, d in df.iterrows():
    print(d["Name"])


# ### Daten mit Vergleichen filtern
# 
# Daten zu filtern kennst du schon von Numpy. :-) Da pandas auf Numpy aufbaut, gehst du mit pandas genauso vor bei den Arrays von Numpy.

# In[10]:


df["Year"] < 1990


# In[17]:


df[df["Year"] < 1990]


# Beachte, dass dabei nur eine Kopie des DataFrames gefiltert wird! df bleibt bei solchen Operationen unverändert.

# ### Mehrfache Filter
# Natürlich kannst du auch mehrere Filter an ein DataFrame anlegen. Achte darauf, wenn du in mehrfachen Stufen filtern möchtest, gefilterte DataFrames zwischenzuspeichern:

# In[16]:


df2 = df[df["Year"] < 1990]
df3 = df2[df2["Gender"] == "Male"]
df3


