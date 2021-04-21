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

# ## Zeitdifferenzen: Rechnen mit Datumswerten
# 
# In dieser Lektion lernst du:
# 
# - Wie du in Python mit Datumswerten rechnen kannst,
# - Und was es mit einem "timedelta" auf sich hat.

# In[1]:


from datetime import datetime, timedelta


# In[2]:


now = datetime.now()


# In[9]:


print(now)
print(now + timedelta(days = 20, hours = 4, minutes = 3, seconds = 1))


# In[17]:


day = datetime(2017, 8, 20)

td = day - now

print(td)


# In[18]:


print(datetime(2018, 1, 1) + td)


# In[ ]:





