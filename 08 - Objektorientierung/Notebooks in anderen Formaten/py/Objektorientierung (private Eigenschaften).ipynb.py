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

# ## Objektorientierung: Private Eigenschaften und Methoden
# 
# In dieser Lektion lernst du:
# 
# - Was private Eigenschaften sind...
# - Was private Methoden sind...
# - ... und wo / wozu du diese einsetzen solltest

# In[2]:


class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = 1
                
    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term = self.__term + 1
        
    def get_term(self):
        return self.__term
    
    def name(self):
        print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")
        
        
erik = Student("Erik", "Mustermann")
erik.increase_term()
erik.name()


# Da die Variable __term mit 2 Unterstrichen beginnt, ist diese Eigenschaft **privat**, d. h. wir können von außen nicht auf sie zugreifen:

# In[3]:


print(erik.__term)


# In[ ]:





