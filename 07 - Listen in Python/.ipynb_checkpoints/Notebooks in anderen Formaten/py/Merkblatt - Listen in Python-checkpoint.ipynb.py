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

# ## Listen
# 
# Listen ermöglichen es dir, direkt mehrere Einträge auf einmal zu speichern. Hier z. B. erfassen wir eine Liste von 4 Studierenden:

# In[ ]:


students = ["Max", "Monika", "Erik", "Franziska"]

last_student = students.pop()
print(last_student)
print(students)


# Über den `+` - Operator kannst du 2 Listen miteinander verknüpfen!

# In[1]:


students = ["Max", "Monika", "Erik", "Franziska"] + ["ABCDEF"]
print(students)


# Der `del` - Befehl entfernt einen Eintrag aus einer Liste. Hierbei wird ein Element mit einem bestimmten Index (hier: 4. Element, weil das 4. Element wird über `[3]` angesprochen, weil ja bei 0 angefangen wird zu zählen)

# In[3]:


students = ["Max", "Monika", "Erik", "Franziska", "ABCDEF"]
del students[3]
print(students)


# Der `.remove()` - Befehl entfernt einen Eintrag nach Wert. Sprich, hier wird dann der Eintrag "Monika" aus der Liste entfernt.

# In[12]:


students = ["Max", "Monika", "Erik", "Franziska", "ABCDEF"]
students.remove("Monika")
print(students)


# ## List Comprehensions
# 
# Mit Hilfe von List Comprehensions kannst du recht einfach eine Liste in eine andere Liste umwandeln:

# In[2]:


xs = [1, 2, 3, 4, 5, 6, 7, 8]

ys = [x * x for x in xs]
# ys = []
# for x in xs:
#    ys.append(x * x)
    
print(xs)
print(ys)


# ### List Comprehensions können aber noch viel mehr!

# In[4]:


students = ["Max", "Monika", "Erik", "Franziska"]

lengths = [len(student) for student in students]

#lengths = []
#for student in students:
#    lengths.append(len(student))
    
print(lengths)


# ### Praktisch auch für's Zeichnen von Grafiken!

# In[2]:


import matplotlib.pyplot as plt


# In[4]:


xs = [x / 10 for x in range(0, 100)]
ys = [x * x for x in xs]

print(len(xs))
print(len(ys))

plt.plot(xs, ys)
plt.show()


# ## Listen verschachteln
# 
# In Python ist es erlaubt, Listen ineinander zu verschachteln. Das erlaubt uns z. B. eine Matrix zu modellieren:

# In[1]:


liste = [
    ["Berlin", "München", "Köln"],
    ["Budapest", "Pécs", "Sopron"]
]


# In[5]:


liste[0][0]


# In[ ]:





