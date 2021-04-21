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

# ## Laufzeit von eigenen Programmen abschätzen
# 
# Warum ist das wichtiger als z.B. ein paar Variable mehr oder weniger zu verwenden? Warum macht das mehr aus, als die Wahl der Programmiersprache?
# 
# - Die Wahl einer schnelleren Programmiersprache kann definitiv dein Programm beschleunigen
# - Allerdings: Viel wichtiger ist die Wahl der richtigen Datenstruktur. Das macht wirklich sehr viel mehr aus!
# 
# https://wiki.python.org/moin/TimeComplexity
# 
# ### Beispiel 1: Alle Studierenden ausgeben

# In[2]:


def f(students): # O(n)
    for student in students:
        print(student)
    
s = ["Max", "Erik", "Monika", "Tobias"]
f(s)


# ### Beispiel 2: Alle Studierenden sortieren und anschließend ausgeben

# In[5]:


def f(students): # O(n*log(n))
    students.sort() # O(n*log(n))
    for student in students: # O(n)
        print(student)
    
s = ["Max", "Erik", "Monika", "Tobias"]
f(s)


# ### Beispiel 3: Überprüfen, ob ein Studierender bei uns eingeschrieben ist (Liste):

# In[12]:


def f(students): # O(n)
    print("Erik" in students) # O(n)
    
s = ["Max", "Erik", "Monika", "Tobias"]
f(s)


# ### Beispiel 4: Überprüfen, ob ein Studierender bei uns eingeschrieben ist (Set):

# In[11]:


def f(students): # O(1)
    print("Erik" in students) # O(1)
    
s = {"Max", "Erik", "Monika", "Tobias"}
f(s)


# In[13]:


# Dr. Oliver Vornberger, Algorithmen und Datenstrukuren


# In[ ]:





