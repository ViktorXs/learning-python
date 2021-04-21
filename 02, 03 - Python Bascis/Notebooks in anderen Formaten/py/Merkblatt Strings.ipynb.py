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

# # Strings
# 
# Wir können in Python nicht nur mit Zahlen, sondern auch mit Zeichenketten, sogenannten **Strings**, arbeiten. Darunter kannst du dir jegliche Abfolgen von Zeichen vorstellen, die in Anführungszeichen stehen. Zum Beispiel ist _"Hallo"_ ein String und _"Hallo Welt"_ ebenso, aber auch _"123.2"_ oder _"!Achtung!"_

# ### Allgemeines
# 
# Auch Strings können wir mit dem print()-Befehl ausgeben.

# In[1]:


print("Hallo Welt")


# Du kannst Strings wie Zahlen in Variablen speichern.

# In[2]:


name = "Max"


# In[3]:


print(name)


# ### Strings zusammenfügen
# 
# Du kannst zwei oder mehrere Zeichenketten auch mittels **+** zusammenfügen.

# In[4]:


print("Ich bin: " + "Max")


# In[5]:


print("Ich bin: " + name + ". Und wer bist du?")


# Allerdings kommt es zu einer Fehlermeldung, wenn du versuchst, Zahlen und Strings zu addieren:

# In[6]:


print("Ich bin: " + 4)


# ### Eine Zahl in einen String umwandeln
# Du kannst diese Fehler korrigieren, indem du die Zahl in einen String umwandelst. Dazu hast du zwei Möglichkeiten:
# 
# 1.) Du setzt Anführungszeichen um die Zahl und machst sie so zu einem String:

# In[7]:


print("Ich bin: " + "4")


# 2.) Du wandelst die Zahl mit dem **str()**-Befehl in einen String um:

# In[8]:


age = 22
print("Ich bin: " + str(age))


# **Beachte, dass du mit "4" oder str(age) nicht mehr rechnen kannst!**

# ### Strings aus einer Liste zu einem String zusammenfügen
# 
# Mit dem  **join()**-Befehl, der auf einen String angewendet wird, verbinden wir die Strings aus einer Liste zu einem neuen String: **string.join(liste)**
# 
# Der String, auf den join() angewendet wird, bildet dabei die Nahtstelle: dieser String wird als Verbindung zwischen den einzelnen Listenelementen im neuen String gesetzt.

# In[9]:


students = ["Max", "Monika", "Erik", "Franziska"]
print(", ".join(students))


# In[10]:


students_as_string = ", ".join(students)
print("An unserer Uni studieren: " + students_as_string)


# In[11]:


students = ["Max", "Monika", "Erik", "Franziska"]
print(" - ".join(students))


# ### Einen String in eine Liste aufspalten
# 
# Mit dem **split()**-Befehl, der auf einen String angewendet wird, wird dieser String an seinen Leerzeichen aufgespalten, und die daraus resultierenden Einzelstrings in einer Liste gespeichert: **string.split()**

# In[12]:


i = "Max, Monika, Erik, Franziska"


# In[13]:


print(i.split())


# In[14]:


print(i.split(", "))


# In[15]:


print(i.split("a"))


# Insbesondere können wir auch mehrere Befehle, die wir schon kennen gelernt haben, miteinander kombinieren:

# In[16]:


# Hier zählen wir die Anzahl der Wörter des Satzes s

s = "Ich bin ein Satz mit vielen Wörtern"
print(len(s.split()))


