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

# ## Das Requests - Modul
# 
# In dieser Lektion lernst du:
# 
# - Wie du eine Webseite herunterlädst, und dir den HTML-Code davon anzeigen kannst.
# 
# Dazu verwendne wir das requests-Modul (http://docs.python-requests.org/en/master/).
# 
# Wir werden folgende Seite crawlen: http://python.beispiel.programmierenlernen.io/index.php.

# In[2]:


import requests


# In[3]:


r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")


# In[8]:


print(r.status_code)
print(r.headers)
print(r.text)


# In[ ]:





