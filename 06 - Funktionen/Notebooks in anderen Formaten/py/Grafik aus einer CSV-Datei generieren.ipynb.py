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

# In[17]:


xs = []
ys = []

name = "Anna"
gender = "F"
state = "CA"

with open("../data/names.csv", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1
        
        line_splitted = line.strip().split(",")
        if line_splitted[1] == name and line_splitted[3] == gender and line_splitted[4] == state:
            xs.append(line_splitted[2])
            ys.append(line_splitted[5])
            # print(line_splitted)
            # break
            
print(xs)
print(ys)
# 12345,Anna,1910,F,CA,999
# 32345,Anna,1911,F,CA,555


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


plt.plot(xs, ys)
plt.show()


# In[ ]:





# In[ ]:





