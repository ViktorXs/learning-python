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
# In dieser Lektion lernst du:
# 
# - Was genau es mit dem "with"-Konstrukt auf sich hat, welches du in diesem Kurs schon benutzt hast.

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
    


# In[2]:


def do_something():
    with open("existiert.txt", "r") as file:
        print(file)
        return "HALLO"
    
do_something()


# In[ ]:





