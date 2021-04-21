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

# # Die for-Schleife
# Neben der while-Schleife, die wir schon kennen gelernt haben, gibt es noch die **for-Schleife**. Hier durchläuft eine Schleifenvariable nacheinander die Werte in einer ebenfalls anzugebenden Sequenz.
# 
# Bei dieser Sequenz kann es sich z. B. um eine Liste handeln.

# In[3]:


liste = [5, 8, 10]
for i in liste:
    print(i)


# In[5]:


liste = ["Max", "Moritz", "Monika"]
for i in liste:
    print(i)


# Wir sehen, dass unsere Schleifenvariable i nacheinander und automatisch die Werte aus der Liste annimmt. 

# ### Das range-Objekt
# Als Sequenz für eine for-Schleife braucht man nicht zwangsläufig eine Liste. Häufig greift man stattdessen auf ein **range**-Objekt zurück:

# In[1]:


print(range(0,10))


# In[2]:


for i in range(0, 10):
    print(i)


# In[8]:


# Hier summieren wir alle Zahlen von 1 bis 10 mithilfe einer for-Schleife und eines range-Objektes auf
sum = 0
for i in range(1, 11):
    sum += i
print(sum)


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Schreibe eine for-Schleife unter Verwendung eines range-Objektes! :-)
# 
# 
# 

# In[ ]:





