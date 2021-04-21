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

# # Variablen

# <strong>Variablen</strong> sind ein generell wesentliches Konzept von Programmiersprachen. Du kannst dir eine Variable als eine Art Behälter vorstellen, in dem du z. B. eine Zahl ablegen kannst, um sie später wiederzuverwenden. <br>
# 
# In Python kannst du eine Variable einführen und ihr einen Wert zuweisen, indem du schreibst: **Variablenname = Zahl**
# 
# Beachte, dass ein Variablenname **nicht** mit einer Zahl anfangen darf!
# 
# Konkret kann die Definition einer Variablen etwa so aussehen:

# In[2]:


a = 5


# Statt eines Wertes darf rechts vom Gleichheitszeichen auch eine Rechnung stehen, die als Ergebnis eine Zahl liefert: 

# In[1]:


a = 5 + 6


# An einer anderen Stelle im Programm greifst du dann über den Variablennamen auf die Zahl zu. Du kannst die Variable etwa in einem print()-Befehl verwenden:

# In[5]:


print(a)


# Du kannst auch mit Variablen, in denen Zahlen gespeichert sind, rechnen:

# In[11]:


print(a * a)


# In[4]:


b = 5
print(b * b * b)


# In[2]:


# das Durchschnittsalter berechnen

age = 21
age2 = 18

print((age + age2) / 2)


# In[5]:


# Statt in print() zu rechnen, können wir das Ergebnis auch erst in einer Variablen zwischenspeichern

average_age = (age + age2) / 2


# In[4]:


print(average_age)


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Gib einige Rechenergebnisse per print() aus, aber speichere Zahlen und Teilergebnisse in Variablen! :-)

# In[ ]:





