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

# ## Daten sortieren
# 
# In dieser Lektion lernst du, was es mit Lambda-Funktionen auf sich hat. Diese sind unglaublich praktisch, weil sie eine kurze Schreibweise sind, wie du eine Funktion als Parameter übergeben kannst:

# In[4]:


students = [
    ("Max", 3),
    ("Monika", 2),
    ("Erik", 3),
    ("Franziska", 1)
]

students.sort(key=lambda student: student[1])
print(students)


# In[5]:


f = lambda student: student[1]
f(("Max", 1))


# In[ ]:





