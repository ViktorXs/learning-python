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

# # Listen
# 
# Bislang haben wir in einer Variable jeweils nur ein Element (Zahl oder String) gespeichert. 

# In[ ]:


student1 = "Max"
student2 = "Monika"
student3 = "Erik"
student4 = "Franziska"


# ### Eine Liste erstellen
# **Listen** hingegen können mehrere Elemente enthalten. Man erzeugt eine Liste und füllt sie mit Elementen wie folgt:
# 
# **Listenname = [Element1, Element2, Element3]** 
# 
# Natürlich kann eine Liste nicht nur drei, sondern beliebig viele Elemente enthalten.
# 
# Konkret kann das dann so aussehen:

# In[3]:


students = ["Max", "Monika", "Erik", "Franziska"]


# In[2]:


marks = [4, 3, 2, 1]


# Listen kannst du wie Zahlen und Strings per print()-Befehl ausgeben.

# In[3]:


print(students) 


# In einer Liste dürfen auch Strings und Zahlen nebeneinander vorkommen, doch davon ist abzuraten! Wir werden dafür später geeignetere Strukturen kennenlernen. :-)

# ### Ein Element aus einer Liste auswählen
# Du kannst auch auf die Elemente aus einer Liste einzeln zugreifen. Stell dir vor, dass alle Elemente in einer Liste durchnummeriert sind, aufsteigend von 0 an. Per **Index** kannst du ein Element über seine Position in der Liste anwählen: 
# 
# **Listenname[Position]**
# 
# Konkret sieht das so aus:

# In[7]:


print(students[0])


# In[9]:


print(students[1])


# In[10]:


print(students[2])


# In[16]:


print(students[3])


# Die ausgewählten Elemente aus einer Liste kannst du dann weiterverarbeiten wie du das von Variablen schon kennst. Dabei solltest du beachten, ob es sich bei den Elementen um Zahlen oder Strings handelt.

# In[29]:


print(students[0] + " & " + students[3])


# In[5]:


# den Notendurchschnitt ausrechnen
print((marks[0] + marks[1] + marks[2] + marks[3]) / 4)


# ### Ein weiteres Element an eine Liste anhängen
# Möchtest du ein weiteres Element an deine Liste anhängen, verwendest du den **append()**-Befehl. Anders als die Befehle, die du schon kennst, wie den print()-Befehl, steht append() nicht für sich, sondern mit einem Punkt _hinter_ dem Objekt, auf den append() angewendet wird: 
# 
# **Listenname.append(Element)**
#  
# Du wirst im Zuge dieses Kurses ganz automatisch lernen, welche Befehle für sich stehen und welche angehängt werden, und was genau das jeweils bedeutet. :-) 

# In[6]:


students.append("Moritz")


# Jetzt schauen wir uns an, ob der Befehl auch funktioniert hat ;-):

# In[7]:


print(students)


# ### Die Länge einer Liste abfragen
# Mit dem len-Befehl kannst du herausfinden, wie viele Elemente eine Liste enthält: **len(Listenname)**

# In[38]:


print(len(students))


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Erstelle ein paar Listen! :-)

# In[ ]:





