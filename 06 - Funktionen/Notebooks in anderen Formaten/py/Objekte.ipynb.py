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

# ### Funktionen
# Bei ihrem Aufruf stehen Funktionen "für sich" und das, worauf sie sich beziehen steht ggf. als Argument in den Klammern hinter ihnen:

# In[1]:


liste = [1, 2, 3]


# In[2]:


print(liste)


# In[3]:


print(len(liste))


# ### Methoden
# Daneben kennen wir aber auch schon Befehle, die mit einem Punkt an Objekte angehängt werden. Eine Liste ist ein solches **Objekt**. Jedes Objekt hat Methoden, auf die wir zurückgreifen können. Diese Methoden können wir aber nicht auf ein Objekt eines anderen Typs anwenden (meistens zumindest).
# 
# Schauen wir uns einige nützliche Methoden des Listen-Objektes an :-) (du brauchst sie dir nicht alle merken)

# In[4]:


# ein Element anhängen
liste.append(4)

print(liste)


# Genauso bieten auch andere "Objekte" in Python Methoden an. Beispielsweise ist der `.split()` - Aufruf auch ein Methodenaufruf:

# In[5]:


"Hallo,Welt".split(",")


# In[ ]:





# In[ ]:





# In[ ]:





