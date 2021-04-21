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

# ### Vergleichsoperatoren

# Um die Bedingungen in den if-else-Strukturen besser zu verstehen, schauen wir uns **Vergleichsoperationen** an. Das wird uns helfen, eine Vielfalt an Bedingungen formulieren zu können.

# ### Ungleichheitsoperatoren und Bools

# In[1]:


if 6 < 5:
    print("JA")


# Warum kommt es zu keiner Ausgabe mit print()? Schauen wir uns doch Ausdrücke mit Ungleichheitszeichen (<,>) im Detail an:

# In[5]:


print(6 < 5)
print(5 < 6)


# **True** und **False** (Großschreibung beachten!) sind weitere _feststehende Ausdrücke_ in Python. Neben Strings (Zeichenketten), Ganzzahlen (Integer) und Fließkommazahlen (Floats) bilden sie einen weiteren Datentyp - den **Bool**.

# In[7]:


b = False
print(b)


# Genauer wird eine if-Bedingung also nur dann ausgeführt, wenn nach dem if ein Bool mit dem Wert True steht: 

# In[8]:


result = 5 < 6
if result:
    print("5 ist kleiner als 6")


# In[10]:


print(5 < 6)


# ### Der Gleichheitsoperator

# Neben Ungleichheiten können wir natürlich auch Gleichheiten abfragen, und zwar mit **==**

# In[11]:


print(5 == 5)
print(5 == 4)


# In[19]:


if 5 == 5:
    print("5 ist 5")


# Mittels des Gleichheitsoperators können wir auch die Zustände _größer gleich_ (**>=**) und _kleiner gleich_ (**<=**) abfragen:

# In[18]:


print(5 < 5)
print(5 <= 5)
print(5 >= 5)


# ### Strings vergleichen 

# Wir können nicht nur Zahlen miteinander vergleichen, sondern auch Strings:

# In[15]:


word = "Hallo"
print(word == "Hallo")
print(word == "Welt")


# ### Der Ungleichheitsoperator

# Auf Ungleichheit checken wir mit dem Zeichen **!=**

# In[16]:


word = "Hallo"
print(word != "Hallo")
print(word != "Welt")


# Auch Zahlen kann man auf Ungleichheit hin miteinander vergleichen:

# In[3]:


zahl = 4
print(zahl != 4)
print(zahl != 5.5)


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Formuliere eigene Vergleichsoperationen mit den Operatoren aus dieser Lektion! :-)

# In[ ]:






