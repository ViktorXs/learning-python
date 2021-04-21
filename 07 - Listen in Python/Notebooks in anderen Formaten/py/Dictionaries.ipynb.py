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
# In dieser Lektion stelle ich dir Dictionaries vor. Warum benötigst du die?
# 
# - Du kannst Wertezuordnungen speichern (z. B. Telefonbuch: Ein Nachname hat eine Telefonnummer).
# - Du kannst nachträglich Elemente verändern / entfernen / hinzufügen.
# - Dictionaries brauchst du wirklich immer wieder...
# - Wir schauen uns später hier in diesem Kurs auch noch ein paar Beispiele an!

# In[3]:


d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}


# In[4]:


print(d)


# In[6]:


print(d["Helsinki"])


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


# In[ ]:





