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

# # Vererbung
# 
# Vererbung ist ein fundamentales Konzept der Objektorientierung, mit dem du Daten aufteilen und besser modellieren kannst.

# Die Klasse Student kennen wir schon:

# In[4]:


class Student():
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def name(self):
        return self.firstname + " " + self.surname


# In[7]:


student = Student("Monika", "Mustermann")
print(student.name())


# Wir wollen eine weitere Klasse definieren, die Ähnlichkeiten zu einer bereits bestehenden Klasse aufweist:

# In[29]:


class WorkingStudent():
    
    def __init__(self, firstname, surname, company):
        self.firstname = firstname
        self.surname = surname
        self.company = company
    
    def name(self):
        return self.firstname + " " + self.surname
        


# In[30]:


student = WorkingStudent("Max", "Müller", "ABCDEF GmbH")
print(student.name())


# ### Eine Klasse mit Vererbung definieren
# 
# Wir können uns sparen, gleiche Instanzvariablen und Methoden ein weiteres Mal zu definieren - dank Vererbung. Dazu verweisen wird innerhalb einer Klassendefinition auf eine andere:

# In[44]:


# Als Parameter übergeben wir die Klasse, von der unsere neue Eigenschaften und Methoden vererbt werden soll (Mutterklasse)
class WorkingStudent(Student):
    
    def __init__(self, firstname, surname, company):
        # Die alten Instanzvariablendefinitionen werden unten hinfällig
        # self.firstname = firstname
        # self.surname = surname
        
        # mit super() zeigen wir Python an, dass die init()-Methode der Mutterklasse angewendet werden soll
        super().__init__(firstname, surname)
        self.company = company
    
    def name(self):
        # wieder verweisen wir mit super() auf die Methode der Mutterklasse, die wir für die Klasse WorkingStudent überschreiben
        return super().name() + " (" + self.company + ")"


# In[39]:


student = WorkingStudent("Max", "Müller", "ABCDEF GmbH")
print(student.name())


# In[43]:


students = [
    WorkingStudent("Max", "Müller", "ABCDEF GmbH"),
    Student("Monika", "Mustermann"),
    Student("Erik", "Müller"),
    WorkingStudent("Franziska", "Mustermann", "XYZXYZ GmbH")
]

for student in students:
    print(student.name())


# Hier sehen wir, dass die verschiedenen name()-Methoden verschiedene Ausgaben liefern, obwohl wir mit demselben Namen auf sie zugreifen.

