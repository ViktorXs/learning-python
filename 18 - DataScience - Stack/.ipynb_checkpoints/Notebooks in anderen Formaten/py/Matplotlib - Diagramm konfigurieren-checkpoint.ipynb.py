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

# ## Matplotlib: Diagramm konfigurieren
# 
# In dieser Lektion lernst du:
# 
# - Wie du die Farbe der Linie beeinflussen kannst
# - Wie du eine Legende zur Grafik hinzufügen kannst
# 
# Wirf auch mal einen Blick in die offizielle Dokumentation: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot :-)

# In[2]:


import matplotlib.pyplot as plt


# Bislang sehen unseren Grafiken noch etwas eintönig aus:

# In[5]:


plt.plot([1, 2, 3], [4, 5, 4])
plt.show()


# ### Farbe eines Diagramm verändern & Farbwerte als Hexadezimalzahlen
# 
# Die Farbe eines Graphen stellst du mit dem `color` - Attribut der `plot()` - Funktion ein. Du musst allerdings beachten, dass du die Farbwerte in **Hexadezimaldarstellung** angibst! 
# 
# Farbwerte in Hexadezimaldarstellungen beginnen mit `#`, haben dann `sechs Ziffern` und beinhalten die Zahlen `0-9` sowie die Buchstaben von `a-f`. Im Hexadezimalsystem kommt nach `9` die Ziffer `a`, dann `b`, dann `c` usw. So zählt man bis `f` und dann erst kommt die `10`, die also eigentlich die "normale" `16` bezeichnet. Das klingt umständlich, aber so kann man gößere Zahlen mit weniger Zeichen ausdrücken. Beispielsweise brauchen wir für `100` eigentlich drei Zeichen, in Hexadezimaldarstellung reichen noch zwei Zeichen. Genauer lassen sich alle Zahlen bis einschließlich `255` noch mit zwei Zeichen darstellen!
# 
# Bei der Farbcodierung in Hexadezimalzahlen stehen die ersten zwei Ziffern für den Rot-Anteil, die nächsten zwei für den Grün-Anteil und die letzten beiden für den Blau-Anteil. So kannst du quasi Farben mit Hexadezimalzahlen mischen. 
# 
# Was passiert wohl, wenn wir Rot und Blau mischen?

# In[9]:


plt.plot([1, 2, 3], [4, 5, 4], color = "#ff00ff")
plt.show()


# Wenn du wissen möchtest, wie der Hexadezimalwert einer bestimmten Farbe ist, googlest du einfach nach "color picker", stellst die gewünschte Farbe ein und kopierst die Hexadezimalzahl.

# ### Die Linie im Graphen verändern
# 
# Mit dem `linestyle` - Attribut können wir z.B. einstellen, dass die Linie im Graphen gestrichelt sein soll.

# In[11]:


plt.plot([1, 2, 3], [4, 5, 4], color="#f27126", linestyle="dashed")
plt.show()


# Schau doch in der Dokumentation nach, welche Linientypen es noch gibt: **https://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D.set_linestyle**

# Du kannst auch über das `marker` - Attribut das Symbol festlegen, mit dem Werte im Diagramm markiert sein sollen.

# In[13]:


plt.plot([1, 2, 3], [4, 5, 4], color="#f27126", linestyle="dashed", marker="o")
plt.show()


# Hier findest du eine Übersicht über alle möglichen Marker: **https://matplotlib.org/api/markers_api.html#module-matplotlib.markers**

# ### Eine Legende hinzufügen
# Eine Legende hinzuzufügen erfordert zwei Schritte:
# - das `label` - Attribut der `plot()` - Funktion mit einem Wert versehen
# - diesen Wert mit der `legend()` - Funktion von matplotlib anzeigen 

# In[14]:


plt.plot([1, 2, 3], [4, 5, 4], color="#f27126", linestyle="dashed", marker="o", label="Umsatz")
plt.legend()
plt.show()


# Bei `pandas` braucht man keinen `label` - Parameter festlegen, die passende Beschriftung des Graphen wird automatisch ausgewählt, wenn man die `legend()` - Methode aufruft (im Hintergrund wird der Titel der Spalte, die man plotten lassen möchte, mit an `plot()` übergeben und passenderweise als Beschriftung verwendet).

# In[19]:


import pandas as pd

df = pd.read_excel("daten.xlsx")

year = df["Jahr"]
sales = df["Umsatz"]

plt.plot(year, sales)
plt.legend()
plt.show()


