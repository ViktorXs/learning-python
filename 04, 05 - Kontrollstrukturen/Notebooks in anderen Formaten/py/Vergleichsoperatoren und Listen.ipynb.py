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

# In[2]:


students = ["Max", "Monika", "Erik", "Franziska"]

print("Monika" in students)
print("Moritz" in students)


# In[5]:


if "Monika" in students:
    print("Ja, die Monika studiert hier!")
else:
    print("Nein, die Monika studiert hier nicht!")
    
if "Moritz" in students:
    print("Ja, die Moritz studiert hier!")
else:
    print("Nein, der Moritz studiert hier nicht!")


# ### Übrigends: Das klappt auch auf Strings!

# In[7]:


sentence = "Ja, die Monika studiert hier!"

if "!" in sentence:
    print("JA")
else:
    print("NEIN")


# In[ ]:





