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

# ## CSV lesen (und Daten überspringen)
# 
# In dieser Lektion lernst du:
# 
# - Wie du eine CSV-Datei einliest, und Zeilen überspringen kannst.

# In[18]:


with open("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
        
        if int(data[1]) < 2000000:
            continue
        
        if data[2] == "BUD":
            continue
        
        print(data)
        
        #if data[2] == "BER" or data[2] == "BUD":
        #    print(data[2])
        #    print(data)


# In[14]:


int("1800000") >= 2000000


# In[ ]:





