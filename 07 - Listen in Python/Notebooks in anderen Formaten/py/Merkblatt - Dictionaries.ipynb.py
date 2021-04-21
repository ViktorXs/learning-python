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

# ## Dictionaries in Python
# 
# Dictionaries sind unglaublich praktisch, damit kannst du z. B. folgendes machen:
# 
# - Du kannst Wertezuordnungen speichern (z.B. Telefonbuch: Ein Nachname hat eine Telefonnummer).
# - Du kannst nachträglich Elemente verändern / entfernen / hinzufügen.
# - Dictionaries brauchst du wirklich immer wieder...
# 
# Machen wir mal ein Beispiel...

# In[3]:


d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}


# In[4]:


print(d)


# Zugriff auf ein einzelnes Element:

# In[6]:


print(d["Helsinki"])


# Hiermit überschreibst du ein einzelnes Element:

# In[7]:


d["Budapest"] = "BUD"


# In[8]:


print(d)


# ## Element entfernen

# In[9]:


del d["Budapest"]


# In[10]:


print(d)


# ## Abfrage: Ist ein Element im Dictionary?

# In[11]:


if "Budapest" in d:
    print("Budapest ist im Dictionary enthalten")
if "Saigon" in d:
    print("Saigon ist im Dicionary enthalten")


# ## Auf Elemente zugreifen...

# In[16]:


print(d["Saigon"])
print(d.get("Saigon"))


# In[18]:


print(d["Budapest"])


# In[19]:


print(d.get("Budapest"))


# ## Dictionaries und Schleifen
# 
# Du hast bei Dictionaries 2 Möglichkeiten, diese mit einer for - Schleife durchzugehen.
# 
# Entweder direkt, dann gehst du die Schlüssel durch:

# In[5]:


d = {"München": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}

for key in d: 
    value = d[key]
    print(key)
    print(value)


# Oder über die .items() - Methode, damit kannst du Schlüssel + Wert direkt durchgehen:

# In[8]:


for key, value in d.items():
    print(key + ": " + value)


# In[ ]:





