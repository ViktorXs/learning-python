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

# ## Datenstrukturen in Python
# 
# Du hast jetzt schon 2 Datenstrukturen in Python kennengelernt:
# 
# - Listen: `liste = ["Hallo", "Welt"]`
# - Dictionaries: `d = {"Hallo": 5, "Welt": 4}`
# 
# Es gibt aber auch noch weitere... In dieser Lektion lernst du das Set kennen!

# In[7]:


s = ["Hallo", "Welt"]
s.append("Mars")
print(s)


# In[9]:


s = {"Hallo", "Welt"}
s.add("Mars")
print(s)


# In[11]:


s.add("Mars")
print(s)


# In[12]:


if "Mars" in s:
    print("Mars ist im Set")


# In[17]:


text = "Hallo Welt Hallo Mars Hallo Welt"
words = set()
for word in text.split(" "):
    words.add(word)
print(words)
print(len(words))


# In[ ]:





