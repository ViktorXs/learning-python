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

# # Abschluss Kontrollstrukturen

# Nimm dir die Zeit, um die Aufgaben sorgfältig zu bearbeiten. :-) Viel Erfolg!
# 
# Wenn du mit diesem Übungsblatt fertig bist, kannst du deine Lösung mit der Musterlösung in Textform (Datei: `Abschluss Kontrollstrukturen (Musterloesung)`) vergleichen. 
# 
# Die Video - Musterlösung (in der nächsten Lektion) ist besonders ausführlich gehalten. Wenn du alles richtig gelöst hast, ist es vollkommen okay, wenn du diese Lektion dann überspringst.

# ### 1. Aufgabe: Kontinente 
# 
# #### a.) Gebe nacheinander alle Kontinente aus der Liste _continents_ aus.

# In[4]:


continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

# Hier deinen Code ergänzen


# Gewünschte Ausgabe:
# 
# ```
# Afrika
# Antarktis
# Asien
# Australien und Ozeanien
# Europa
# Nordamerika
# Südamerika
# ```

# #### b.) Gebe aus der Liste _continents_ nur die bewohnten Kontinente aus
# 
# **Hinweis:**: Antarktis ist nicht bewohnt. Diesen Kontinent kannst du also bei der Ausgabe einfach überspringen

# In[9]:


# Hier deinen Code ergänzen


# Gewünschte Ausgabe:
# 
# ```
# Afrika
# Asien
# Australien und Ozeanien
# Europa
# Nordamerika
# Südamerika
# ```

# #### c.) Gebe aus der Liste _stuff_ nur die Kontinente aus.
# 
# Du kannst dafür die Liste `stuff` mit einer Schleife durchgehen, und dann mit Hilfe der Variable `continents` prüfen, ob ein Element der Liste `stuff` auch in der Liste `continents` vorkommt.

# In[6]:


stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]


# In[10]:


# Hier deinen Code ergänzen


# Gewünschte Ausgabe:
# 
# ```
# Asien
# Antarktis
# ```

# #### d.) Wie viele Kontinente sind in der Liste `stuff` enthalten?
# 
# Schreibe dazu eine Schleife, mit der du die Anzahl der Kontinente in der Liste _stuff_ zählst, und gebe diesen Wert dann aus.

# In[11]:


# Hier deinen Code ergänzen


# Gewünschte Ausgabe:
# 
# ```
# 2 
# ```

# ### 2. Aufgabe: Rabattaktion
# 
# Zurück zur Mathemagierin: Sie möchte in ihrem Shop eine Rabattaktion starten, um das Geschäft anzukurbeln. Natürlich hat sie dabei wieder etwas zu programmieren für dich. Du sollst die Berechnung der reduzierten Preise mit einer if-elif-else-Struktur vereinfachen.
# 
# Dabei ist zu beachten:
# 
# Artikel, die zwischen 0 und 20 (einschließlich) Taler kosten, werden um 20% reduziert; Artikel, die zwischen 20 (nicht einschließlich) und 50 Taler (einschließlich) kosten, werden um 40% reduziert, alle anderen Artikel, also solche die mehr als 50 Taler kosten, werden um 60% reduziert.
# 
# #### a.) Gebe für die Variable _price_ den neuen, rabattierten Preis aus.

# In[15]:


price = 50

# hier kommt deine if-elif-else-Struktur hin

print(price)


# Gewünschte Ausgabe:
# 
# ```
# 30.0
# ```

# #### b.) Berechne nun für jeden der alten Preise aus der Liste _prices_ die passenden reduzierten Preise und speichere sie in der neuen Liste new_prices, gebe diese Liste schließlich aus.

# In[16]:


prices = [2, 50, 70, 30]
new_prices =[]

# schreibe hier deinen Code
    
print(new_prices) 


# Gewünschte Ausgabe (muss nicht farbig sein):
# 
# ```python
# [1.6, 30.0, 28.0, 18.0]
# ```

# #### c.) Zusatzaufgabe (schwierig!)
# Nun überreicht dir die Mathemagierin mit zitternden Händen die Liste _chaos_, in der neue und alte Preise gemischt sind! Angesichts dieser undurchdachten Arbeit schlägst du dir die Hände vor dem Kopf zusammen, aber es hilft ja nichts: Nur du kannst hier wieder Ordnung schaffen, indem du alles zusammenbringst, was du schon gelernt hast!
# 
# Gehe die Elemente in der Liste _chaos_ durch. Bei einem neuen Preis ziehst du bloß den neuen Wert aus dem String und hängst ihn der Liste _order_ an. Bei einem alten Preis hingegen holst du dir den alten Wert, berechnest den neuen Preis und hängst diesen Wert an die Liste _order_.
# 
# Schließlich gibst du die vollständige Liste _order_ aus, in der nur noch neue Preise drinstehen (und nur noch Zahlen!).
# 
# Tipp: Mit Hilfe des `in` - Operators kannst du prüfen, ob `old` oder `new` in einem Listenelement vorkommt (`"old" in "old price: 123"`), und entsprechend entscheiden, ob du die Rabatierung durchführen möchtest oder nicht.

# In[12]:


chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

# hier schreibst du deinen Code hinein
    
print(order)


# Gewünschte Ausgabe (muss nicht farbig sein):
# 
# ```python
# [24.0, 21, 17.4, 30.0, 101]
# ```

# ### Yeah, gut gemacht! :-)

