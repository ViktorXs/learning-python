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

# ## Das DefaultDict-Modul
# 
# Das DefaultDict-Modul stellt eine ganz besondere Funktionalität zur Verfügung: Du kannst damit ein Dictionary erstellen, welches sich mehr oder weniger automatisch mit initialen Werten befüllt!
# 
# Das möchten wir uns natürlich mal anschauen:

# In[1]:


from collections import defaultdict


# In[8]:


def generate():
    print("generate() wurde aufgerufen!")
    return 0

d = defaultdict(generate)

d["existiertNicht"] = d["existiertNicht"] + 5
print(d)


# In[11]:


p = defaultdict(int)
words = ["Hallo", "Hallo", "Welt"]

for word in words:
    p[word] = p[word] + 1

print(p)


# In[ ]:





