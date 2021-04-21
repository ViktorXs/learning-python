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

# ## Quiz: Der not - Operator

# #### Aufgabe 1: Wird "Hallo Welt" ausgegeben?
# 
# Quellcode:
# 
# ```python
# age = 25
# if not age > 30:
#     print("Hallo Welt")
# ```
# 
# - A) Ja
# - B) Nein 

# Richtige Antwort: 

# #### Aufgabe 2
# 
# Wann wird `"Hallo Welt"` ausgegeben (`a`, `b` sind `True` / `False` - Werte.)?
# 
# Spiele dazu die gegebenen Antwortoptionen im Kopf durch und überlege, ob der gesamte Ausdruck erfüllt ist, oder nicht. 
# 
# Quellcode:
# 
# ```python
# if a and (not b):
#     print("Hallo Welt")
# ```
# 
# - A) `a = True, b = True`
# - B) `a = True, b = False`
# - C) `a = False, b = False`
# - D) `a = False, b = True`

# Richtige Antwort: 

# #### Aufgabe 3
# 
# Ein kleines `and` bzw. `or` kann einen großen Unterschied machen. Beispielsweise überprüft folgender Ausdruck, ob ein Anruf zu den Geschäftszeiten (9-15:59 Uhr) stattgefunden hat:
# 
# ```python
# hour >= 9 and hour < 16
# ```
# Jetzt ist hier ein Fehler unterlaufen. Aus Versehen steht in unserem Programm folgender Ausdruck:
# 
# ```python
# hour >= 9 or hour < 16
# ```
# 
# Für welche Werte ist der 2. Ausdruck erfüllt?
# 
# - A) Alle Uhrzeiten ab 9 Uhr tagsüber (9-24 Uhr) 
# - B) Alle Uhrzeiten (0-24 Uhr)
# - C) Alle Uhrzeiten bis 16 Uhr tagsüber (0-16 Uhr) 
# - D) Es gibt keinen Unterschied (9-16 Uhr)

# In[ ]:


Richtige Antwort: 


