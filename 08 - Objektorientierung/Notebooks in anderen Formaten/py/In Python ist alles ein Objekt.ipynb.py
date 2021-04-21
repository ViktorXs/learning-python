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

# ## In Python ist alles ein Objekt

# ### Zahlen sind Objekte
# Wenden wir doch die type()-Funktion mal auf Variablen an, in die wir Zahlen gespeichert haben:

# In[6]:


a = 13

print(type(a))


# In[7]:


a = 12.5

print(type(a))


# Wir sehen also, dass es sich bei den Variabletypen int und float um Klassen handelt!

# ### Verschiedene Darstellungen von Rechenperationen

# In[10]:


12.5 + 5


# Intern wird bei Python in diesem Fall aber die **\__add__()**-Funktion ausgerufen. Eine Addition sieht in objektorientierter Schreibweise etwas so aus:

# In[3]:


a = 12.5
a.__add__(5)


# In[9]:


(12.5).__add__(5)


# Weitere Rechenoperationen sehen in objektorientierter Schreibweise wie folgt aus:

# In[3]:


(12.5).__sub__(7)


# In[6]:


(12.5).__mul__(5)


# In[8]:


(12.5).__truediv__(6.25)


# ### Strings sind Klassen

# In[11]:


s = "Hallo Welt"
print(type(s))


# Wie du es dir schon gedacht hast, handelt es sich auch bei str um eine Klasse.

# In[12]:


len(s)


# Intern führt hier Python entsprechend die **\__len__()**-Methode aus:

# In[14]:


s.__len__()


# Aufgrund dieser internen Struktur können wir Funktionen wie len selbst implementieren und somit steuern:

# In[21]:


class A:
    def __len__(self):
        return 6

instance = A()
len(instance)


# In[ ]:





