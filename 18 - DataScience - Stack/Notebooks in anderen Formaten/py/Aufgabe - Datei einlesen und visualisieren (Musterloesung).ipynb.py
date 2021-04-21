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

# ## Aufgabe: Datei einlesen und visualisieren
# 
# In den ersten paar Abschnitten des Kurses haben wir eine CSV-Datei eingelesen, und die Daten dann als Grafik angezeigt. In dieser Lektion möchte ich dir die Aufgabe geben, diese CSV-Datei erneut einzulesen und die Daten zu visualisieren - aber diesmal mit Pandas!
# 
# Aufgabe: Lade die ../data/names.csv - Datei, und zeichne eine Grafik für den Namen "Anna", das Geschlecht "F" (female) und den Staat "CA". Auf der X-Achse sollen die Jahre abgetragen werden, auf der Y-Achse, wie oft der Name vergeben wurde.

# In[1]:


name = "Anna"
gender = "F"
state = "CA"


# In[4]:


import pandas as pd

df = pd.read_csv("../data/names.csv")
df.head()


# In[7]:


df2 = df[df["Name"] == name]
df3 = df2[df2["Gender"] == gender]
df4 = df3[df3["State"] == state]

df5 = df4.sort_values("Year")


# In[9]:


import matplotlib.pyplot as plt

plt.plot(df5["Year"], df5["Count"])
plt.show()


# In[ ]:





