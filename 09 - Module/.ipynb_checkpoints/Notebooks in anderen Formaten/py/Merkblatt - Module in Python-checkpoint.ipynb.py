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

# ## Module in Python
# 
# In Python hast du die Möglichkeit, Code in Module zu packen, die du dann in verschiedenen Stellen verwenden kannst.
# 
# Die Datei `hallo.py` besteht hierbei aus folgendem Inhalt:
# 
# ```python
# # hallo.py
# 
# def welt():
#     print("Hallo Welt")
#     
# def mars():
#     print("Hallo Mars")
# ```

# Wie können wir diese Datei jetzt einbinden?

# In[1]:


import hallo

hallo.welt()
hallo.mars()


# In[3]:


from hallo import welt, mars

welt()
mars()


# In[4]:


from hallo import *

welt()
mars()


