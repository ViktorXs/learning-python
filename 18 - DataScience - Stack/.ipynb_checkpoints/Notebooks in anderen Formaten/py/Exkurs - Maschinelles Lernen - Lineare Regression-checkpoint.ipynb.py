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

# ## Exkurs: Maschinelles Lernen (Lineare Regression)
# 
# In dieser Lektion machen wir einen kleinen Exkurs: Wir beschäftigen uns ein bisschen mit maschinellem Lernen. Aber keine Sorge, geht ganz easy :)
# 
# In dieser Lektion lernst du:
# 
# - Wie du eine Linie durch die Geburtsstatstik zeichnest, die den Trend der Statistik veranschaulicht
# 
# Indem wir diese Linie verlängern, können wir versuchen Zukunftsprognosen treffen.

# Wir schauen uns nochmal die Häufigkeit des Namens "Anna" für Frauen in Kalifornien an:

# In[43]:


# pandas zum Einlesen der csv-Datei und matplotlib zur grafischen Darstellung einbinden
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/names.csv")
df.head()


# Wir filtern das DataFrame und plotten das Resultat:

# In[40]:


name = "Anna"
gender = "F"
state = "CA"

df2 = df[df["Name"] == name]
df3 = df2[df2["Gender"] == gender]
df4 = df3[df3["State"] == state]

df5 = df4.sort_values("Year")

xs = df5["Year"]
ys = df5["Count"]


# In[2]:


plt.plot(xs, ys)
plt.show()


# ### Maschinelles Lernen mit dem `scikit-learn`-Modul
# 
# Die `LinearRegression()` - Funktion, die eine "passende" Gerade durch unseren Grapfen legt, importieren wir aus dem `scikit-learn` - Modul: 

# In[3]:


from sklearn.linear_model import LinearRegression


# Bevor wir die Funktion anwenden, müssen wir die Parameter vorbereiten: unsere Eingabewerte (die Jahreszahlen) müssen als höherdimensionale Arrays vorliegen, d.h. wir "verpacken" sie:

# In[41]:


xsl = []

for x in xs:
    xsl.append([x])
    
print(xsl)


# Jetzt können wir mit `LinearRegression()` ein Modell mit den vorliegenden Daten trainieren. Bei dem "Modell" handelt es sich hier nur um eine Gerade.

# In[42]:


model = LinearRegression()

model.fit(xsl, ys)


# Welche Voraussagen macht das Modell für bestimmte Jahre (die wir vergleichen könnten, weil dazu ja auch die echten Daten vorliegen)?

# In[28]:


model.predict([[1920], [1950]])


# Wir schauen uns das Modell über die gesamte Vergangenheit an:

# In[29]:


model.predict(xsl)


# Anschaulicher sieht unser Modell (die Gerade) so aus:

# In[30]:


predicted = model.predict(xsl)

plt.plot(xs, ys)
plt.plot(xs, predicted)
plt.show()


# Schauen wir uns zum Schluss doch noch eine Zukunftsprognose an, d.h. welche Häufigkeit für den weiblichen Vornamen "Anna" in Kalifornien liefert die in die Zukunft verlängerte Linie?

# In[31]:


model.predict([[2050]])


