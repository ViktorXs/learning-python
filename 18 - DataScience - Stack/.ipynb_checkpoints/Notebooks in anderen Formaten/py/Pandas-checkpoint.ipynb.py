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

# ## Pandas: Tabellarische Daten einlesen
# 
# Mit `Numpy` haben wir in den letzten Lektionen ein nützliches Modul kennen gelernt, um mit Daten in Form von `Arrays` zu arbeiten. 
# 
# Jetzt gehen wir im _DataScience-Workflow_ einen Schritt zurück und schauen uns an, wie wir an diese Daten kommen: Mit dem Paket `pandas`, das auf `Numpy` aufbaut, kannst du sehr komfortabel CSV / Excel - Dateien einlesen und sie dann sortieren und filtern.

# ### Das `pandas`-Paket einbinden

# Für das `pandas`-Paket hat sich die Abkürzung `pd` etabliert. Auch du solltest dir angewöhnen sie der Einfachheit halber zu verwenden. :-)

# In[3]:


import pandas as pd


# ### Eine `csv`-Datei als `DataFrame` einlesen
# 
# Mit `pandas` geht das Einlesen einer csv-Datei dann ganz schnell:

# In[5]:


df = pd.read_csv("../data/astronauts.csv")
df


# Die Variable `df` ist vom `pandas`-spezifischen Datentyp **DataFrame**

# In[14]:


type(df)


# Beim Öffnen einer csv-Datei mit `read_ csv()` kannst du auch noch den `delimiter`-Parameter festlegen: er gibt an, welches Zeichen einen Dateneintrag abschließt (in unserem Fall hier ein `,`). Wenn also der `delimiter` das Komma - Zeichen ist, dann müssen Daten, in denen ebenfalls Kommata auftauchen, wie z.B. "Inglewood, CA" innerhalb der csv-Datei in " " gesetzt werden. Andernfalls würde Python hier Inglewood und CA als zwei Dateneinträge auffassen, da zwischen ihnen das `delimiter` - Zeichen steht.

# In[13]:


df = pd.read_csv("../data/astronauts.csv", delimiter=",")
df


# ### Sich mit `head()` und `len()` einen ersten Überblick über die Daten verschaffen

# Das DataFrame ist sehr umfangreich und in seiner gesamten Darstellung geradezu erschlagend. Um dir einen Überblick über ein DataFrame zu verschaffen, reicht es, wenn du dir zunächst die Beschriftung der Spalten und die ersten Zeilen anschaust. Mit der `head()`-Methode wird dir nur dieser obere Abschnitt aus einem DataFrame angezeigt.

# In[20]:


df.head()


# Mit `len()` kannst du die Anzahl der Einträge in einem `DataFrame` abfragen - du gehst dazu wie gewohnt vor.

# In[6]:


len(df)


# Da die Zeile mit der Beschriftung mitgezählt wird, sehen wir also, dass es in unserem DataFrame `df` insgesamt 356 Einträge gibt.

# ### Auf eine Spalte eines `DataFrames` zugreifen
# 
# Mit der `[ ] - Schreibweise` können wir über den Titel auf die Inhalte einer Spalte zugreifen - so wie bei einem dictionary über den Schlüssel.

# In[23]:


df["Name"]


# In[7]:


for name in df["Name"]:
    print(name)


# ### Auf eine Zeile eines `DataFrames` zugreifen
# 
# Für den Zugriff auf eine bestimmte Spalte brauchen wir die **`iloc()`**-Methode (die `[ ] - Schreibweise` ist ja schon mit dem Zugriff auf die Spalten belegt).

# In[24]:


df.iloc[0]


# Natürlich können wir auch auf einzelne Spalten in einem Zeileneintrag zugreifen.

# In[1]:


entry = df.iloc[0]
print(entry["Birth Date"])


# Oder kurz:

# In[10]:


print(df.iloc[0]["Birth Date"])


# Mittels der `list slicing` - Notation können wir auch Bereiche von Zeilen auswählen, z.B. die letzten fünf Zeilen des DataFrames:

# In[12]:


df.iloc[-5:]


# In[ ]:





