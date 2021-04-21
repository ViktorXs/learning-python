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

# ## Grundlagen: Regluäre Ausdrücke

# Reguläre Ausdrücke erlauben dir, Strings noch flexibler zu durchsuchen. Beispielsweise kannst du mit einem regulären Ausdruck alle Zahlen in einem String finden oder validieren, dass eine E-Mail-Adresse grundsätzlich existieren könnte.
# 
# Aber wie funkionieren die?

# In[1]:


import re


# In[46]:


sentence = "Ich habe 30 Hunde, die jeweils 4 Liter Wasser brauchen und 2 kg Nahrung."
re.findall("[0-9]+", sentence)


# In[30]:


sentence = "Ich habe 30 Hunde, die jeweils 4 Liter Wasser brauchen und 2 kg Nahrung."
re.search("[0-9]+", sentence)


# In[34]:


re.search("der?", "Hallo der Hallo")


# In[36]:


print(re.search("der*", "Hallo de Hallo"))
print(re.search("der*", "Hallo der Hallo"))
print(re.search("der*", "Hallo derrrrrrrr Hallo"))


# In[37]:


print(re.search("der+", "Hallo de Hallo"))
print(re.search("der+", "Hallo der Hallo"))
print(re.search("der+", "Hallo derrrrrrrr Hallo"))


# In[41]:


print(re.search("[0123456789]+", "Hallo 123 Hallo"))
print(re.search("[0-9]+", "Hallo 123 Hallo"))


# In[44]:


print(re.findall("[0-9]+", "Hallo 123 Hallo 321"))


# In[ ]:





