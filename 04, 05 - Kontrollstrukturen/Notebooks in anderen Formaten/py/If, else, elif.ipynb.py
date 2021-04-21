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

# # Kontrollstrukuren in Python

# ### if
# Bislang haben wir nur Code gesehen, der von oben nach unten ausgeführt wird. In einer **If-Else-Struktur** werden bestimmte Abschnitte des Codes nur dann ausgeführt, wenn auch bestimmte Bedingungen erfüllt sind. Damit können wir Entscheidungen programmieren!
# 
# Schauen wir uns ein Beispiel an:

# In[5]:


n = 30

if n < 42:
    print("Die Zahl n ist kleiner als 42")

print("Ich bin nicht mehr eingerückt!")


# Es ist wichtig, dass der Code unterhalb der Bedingung eingerückt ist! 

# ### else
# Diese if-Struktur lässt sich um ein **else** erweitern, sodass auch in dem Fall, dass die Bedingung nicht zutrifft, ein bestimmter Code ausgeführt wird. Falls die if-Bedingung erfüllt ist, wird natürlich der else-Block nicht mehr ausgeführt.

# In[6]:


m = 10

if m < 5:
    print("m ist kleiner als 5")
else:
    print("ist nicht der Fall")


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Schreibe deine eigene if-else-Bedingung! :-)

# In[ ]:





