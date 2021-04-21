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

# # Objektorientierung: Constructor, Eigenschaften abändern
# 
# In dieser Lektion lernst du, wie du:
# 
# - mit Hilfe eines Constructors Eigenschaften einer Klasse definieren kannst
# - Eigenschaften einer Instanz abänderst.

# Wir haben die bereits die Klasse Students ein wenig erweitert:

# In[13]:


class Student():
    
    # Das ist unser sogenannter Constructor: hier definieren wir die Variablen für die Klasse
    # self ist obligatorisch und bezieht sich immer auf das Objekt, das gerade angelegt wird
    # bei der Erzeugung der Instanz taucht self aber nicht als Parameter auf!
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def name(self):
        print(self.firstname + " " + self.lastname)

erik = Student("Erik", "Mustermann")
erik.name()


# Die Klassendefinition mit Constructor liefert also dieselben Ergebnisse wie die vorherige, umständlichere Definition.

# Wir ergänzen eine weitere Methode:

# In[17]:


class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # Hier initialisieren wir die neue Variable term (Eigenschaft)
        self.term = 1
        
         # Mit dieser Methode erhöhen wir die Variable term um 1
    def increase_term(self):
        self.term = self.term + 1
    
        # name() gibt nunmehr zusätzlich die Anzahl der Semester aus
    def name(self):
        print(self.firstname + " " + self.lastname + " (Semester: " + str(self.term) + ")")
        


# In[19]:


erik = Student("Erik", "Mustermann")
erik.name()


# In[20]:


erik.increase_term()
erik.name()


