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

# ## Exceptions in Python
# 
# In dieser Lektion lernst du, wie du:
# 
# - nach einem Fehler sauber "aufräumen" kannst,
# - dies mit einem "finally" korrekt erzwingen kannst.

# In[9]:


try:
    file = open("existiert.txt", "r")
    print(file)
    print(5 / 0)
except FileNotFoundError:
    print("Datei wurde nicht gefunden")
finally:
    print("FINALLY!!!")
    file.close()


# In[ ]:





