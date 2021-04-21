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

# ## Listen verschachteln
# 
# In Python ist es erlaubt, Listen ineinander zu verschachteln. Das erlaubt uns z. B. eine Matrix zu modellieren.
# 
# In dieser Lektion lernst du:
# 
# - Wie du Listen ineinander verschachtelst
# - und auf die Elemente dann entsprechend zugreifst.

# In[1]:


liste = [
    ["Berlin", "München", "Köln"],
    ["Budapest", "Pécs", "Sopron"]
]


# In[5]:


liste[0][0]


# ## Listen in Dictionaries

# In[8]:


students = {
    "Informatik": ["Max", "Monika"],
    "BWL": ["Erik", "Franziska"]
}

print(students["Informatik"])
print(students["BWL"])


# In[ ]:





