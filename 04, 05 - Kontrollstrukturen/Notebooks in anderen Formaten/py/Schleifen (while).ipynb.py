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

# # Die while-Schleife
# Ein Code-Block innerhalb einer if-elif-else-Struktur wird jeweils nur einmal ausgeführt. Bei Schleifen wie der **while-Schleife** wird ein Code-Block so lange mehrmals hintereinander ausgeführt, bis eine Abbruchbedingung erfüllt ist.

# In[1]:


counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1
    
print("Hallo Welt")


# Innerhalb einer Schleife **muss** sich **unbedingt** ein Zustand in jedem Schritt verändern, damit die Schleifenbedingung nicht dauerhaft erfüllt ist, und das Programm die Schleife auch wieder verlassen kann:

# In[3]:


students = ["Moritz", "Klara", "Monika", "Max"]
i = 0
while i < len(students):
    print(students[i])
    i = i + 1


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Baue selbst eine while-Schleife und achte darauf, dass die Bedingung irgendwann nicht mehr erfüllt ist, indem du in dem eingerückten Codeblock einen passenden Zustand veränderst!  :-)

# In[ ]:





