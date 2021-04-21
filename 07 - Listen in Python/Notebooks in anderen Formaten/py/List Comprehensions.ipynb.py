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

# ## List Comprehensions
# 
# In dieser Lektion lernst du:
# 
# - List Comprehensions
# - Wie du damit Listen einfacher in eine neue Liste umwandeln kannst
# - Und wir nutzen eine List Comprehension, um einfacher eine Grafik zu zeichnen

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

# In[6]:


import matplotlib.pyplot as plt


# In[13]:


xs = [x / 10 for x in range(0, 100)]
ys = [x * x for x in xs]

print(xs)
print(ys)

plt.plot(xs, ys)
plt.show()


# In[ ]:





