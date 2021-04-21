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

# # Erste Schritte: Objektorientierung
# 
# In dieser Lektion lernst du:
# 
# - Wie du Objektorientierung in Python verwendest
# - Wie du eine Klasse erstellst
# - Was Methoden sind

# Wir haben schon mit Objekten gearbeitet, z. B. mit dem Listen-Objekt von Python, auf das wir Methoden wie die append()-Methode angewendet haben:

# In[3]:


students = ["Max", "Monika"]
students.append("Erik")

print(students)


# ### Eine Klasse definieren

# Wir wollen eigene Objekte mit eigenen Methoden erzeugen. Dafür brauchen wir Klassen, das sind Baupläne für Objekte. Die entsprechend dieser Anleitungen erzeugten Objekte nennt man Instanzen dieser Klasse.

# In[2]:


# Wir definieren die Klasse Student mit der Methode name(), Klassennamen beginnen gemäß Konvention mit Großbuchstaben

class Student():
    
    # self ist ein Schlüsselwort, es fungiert gewissermassen als Platzhalter für die jeweilige Instanz
    def name(self):
        print(self.firstname + " " + self.lastname)


# ### Eine Instanz erstellen

# Mittels dieser Klasse als Vorlage erstellen wir uns nun eine Student-Instanz und speichern sie in einer Variable:

# In[8]:


erik = Student()


# Wir definieren zwei Variablen für das Objekt, auf díe wir über das Objekt per Punktschreibweise zugreifen können:

# In[15]:


erik.firstname = "Erik"
erik.lastname = "Mustermann"

print(erik.lastname)


# In[16]:


monika = Student()
monika.firstname = "Monika"
monika.lastname ="Müller"

print(monika.firstname)
print(monika.lastname)


# ### Die Methode eines Objektes benutzen
# Wie gewohnt funktioniert so auch der Zugriff auf die Methode des Objektes:

# In[17]:


erik.name()


# In[19]:


monika.name()


# Insbesondere kann es auch weitere Objekte mit einer Methode desselben Namens geben:

# In[31]:


class Company():
    
    def name(self):
        print(self.legal_name + ": " + self.legal_type)

c = Company()
c.legal_name = "Max Müller"
c.legal_type = "GmbH"

c.name()


# In[32]:


def name_5x(v):
    for i in range(0,5):
         v.name() 
    
name_5x(c)
name_5x(erik)
name_5x(monika)


# In der Funktion name_5x() wird jeweils die zum Objekt gehörige Methode name() ausgeführt. Dafür müssen die Objekte natürlich eine name()-Methode enthalten.

