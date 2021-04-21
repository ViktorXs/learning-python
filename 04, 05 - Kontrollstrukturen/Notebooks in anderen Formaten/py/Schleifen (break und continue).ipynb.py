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

# # Continue & Break
# 
# Wir können während eines Schleifendurchlaufs den aktuellen Durchlauf vorzeitig abbrechen und unmittelbar mit dem nächsten Schleifendurchlauf fortfahren (**continue**) oder auch die gesamte Schleife abbrechen (**break**).
# 

# ### Continue
# Wir brauchen einfach das Wort **continue** in eine Schleife zu schreiben, wenn an einer bestimmten Stelle zum neuen Schleifendurchlauf gesprungen werden soll:

# In[5]:


for i in range(0, 10):
    if i == 3:
        continue
    print(i)


# In dem obigen Beispiel wird für den Wert 3 der print()-Befehl übersprungen.

# In[3]:


for i in range(1, 10):
    print(i)


# ### Break
# Auch **break** schreiben wir einfach in eine Zeile, und schon wird die ganze Schleife abgebrochen, wenn das Programm diese Stelle erreicht:
# 

# In[4]:


for i in range(0, 10):
    if i == 3:
        break
    print(i)


# In[6]:


liste = [4, 6, 7, 2, 4, 6, 7]

s = 0

for element in liste:
    s = s + element
    if s > 10:
        break
    
print(s)


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Schreibe eine Schleife, bei der mit continue ein Schleifendurchlauf abgebrochen wird und später mit break sogar die gesamte Schleife abgebrochen wird! :-)

# In[ ]:





