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

# # Operatoren und Listen
# Wir können mit **in** checken, ob ein Element in einem anderen Element enthalten ist.

# ### Der in-Operator und Listen

# Operatoren gibt es auch in Bezug auf Listen; wir können etwa mit dem **in**-Operator prüfen, ob ein Element in einer Liste enthalten ist. 
#  
# 
# Formal sieht die Syntax so aus: **Element <span style="color:green">in</span> Liste**
# 

# In[2]:


students = ["Max", "Monika", "Erik", "Franziska"]

print("Monika" in students)
print("Moritz" in students)


# Das Resultat einer solchen Abfrage ist ein Bool, d. h., dass der Wert entweder True oder False ist. Somit können wir Ausdrücke mit dem in-Operator auch in if-else-Strukturen verwenden:

# In[3]:


if "Monika" in students:
    print("Ja, die Monika studiert hier!")
else:
    print("Nein, die Monika studiert hier nicht!")
    
if "Moritz" in students:
    print("Ja, der Moritz studiert hier!")
else:
    print("Nein, der Moritz studiert hier nicht!")


# ### Der in-Operator und Strings
# Tatsächlich lässt sich der in-Operator auch auf Strings anwenden. Wir können also z. B. checken, ob ein Buchstabe bzw. ein Zeichen in einem Wort enthalten ist, oder ein Wort in einem Satz, usw.

# In[5]:


sentence = "Ja, die Monika studiert hier!"

if "!" in sentence:
    print("JA")
else:
    print("NEIN")


# In[4]:


word = "Studium"

if "udi" in word:
    print("JA")
else:
    print("NEIN")


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Checke ein paar Strings mit dem in-Operator! :-)
# 

# In[ ]:





