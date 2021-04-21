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

# ## Arbeiten mit Tupeln
# 
# In dieser Lektion lernst du:
# 
# - Wie du Tupel verwenden kannst, um mehrere Rückgabewerte einer Funktion zu modellieren
# - Wie du Tupel entpacken kannst

# In[4]:


student = ("Max Müller", 22, "Informatik")

name, age, subject = student

# name = student[0]
# age = student[1]
# subject = student[2]

print(name)
print(age)
print(subject)


# In[5]:


def get_student():
    return ("Max Müller", 22, "Informatik")

name, age, student = get_student()

print(name)
print(age)
print(subject)


# In[9]:


students = [
    ("Max Müller", 22),
    ("Monika Mustermann", 23)
]

for name, age in students:
    print(name)
    print(age)


# In[ ]:





