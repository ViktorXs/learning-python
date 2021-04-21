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

# ## Pandas + Excel + Matplotlib
# 
# In dieser Lektion lernst du:
# 
# - Wie du Daten aus einer Excel - Datei einliest
# - Und diese dann mit Matplotlib direkt plotten kannst

# ### Mit Pandas eine Excel - Datei einlesen
# 
# Entsprechend zur `read_csv()` - Funktion stellt `pandas` auch die Funktion **`read_exel()`** zur Verfügung:

# In[2]:


import pandas as pd

df = pd.read_excel("daten.xlsx")
df.head()


# Näheres zur `read_excel()` - Funktion findest du in der offizielen Funktion von `pandas` hier: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html

# Mit dem DataFrame gehst du dann wie gewohnt um:

# In[11]:


year = df["Jahr"]

sales = df["Umsatz"]


# In[9]:


print(sales)


# In[8]:


print(year)


# Diese Daten (den Umsatz pro Jahr) wollen wir jetzt grafisch in einem Plot darstellen. :-)

# ### Ein DataFrame plotten
# 
# Zuerst müssen wir wiedermal `matplotlib` einbinden:

# In[15]:


import matplotlib.pyplot as plt


# Die Daten aus den Spalten unseres DataFrames können wir dann der `plot()` - Funktion von matplotlib übergeben.

# In[17]:


plt.plot(year, sales)
plt.show()


