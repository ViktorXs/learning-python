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

# # Statische Variablen
# Wir können Variablen auch statt an Instanzen an Klassen binden. Sie heißen statisch, weil sie nicht mehr an einer einzelnen Instanz hängen: 

# In[22]:


class Car:
    # das self von früher fehlt hier
    price = "expensive"

c = Car
print(c.price)


# Auf die Variable price haben wir auch über die Klasse car Zugriff:

# In[23]:


print(Car.price)


# In[20]:


Car.price = "cheap"


# In[21]:


print(c.price)


# Wir haben also die Eigenschaft bei allen Instanzen geändert!

# In[12]:


bobbycar = Car
print(bobbycar.price)


# Wir haben also nachträglich die Eigenschaft price der Klasse geändert. Davon ist im Allgemeinen abzuraten!
# 
# Wie zuvor sollten wir daher Instanzvariablen definieren, die an eine Instanz gebunden sind und unabhängig von der Klasse verändert werden können:

# In[14]:


class CarI:
    def __init__(self):
        self.price = "expensive"
        
c = CarI()
print(c.price)


# In[ ]:





